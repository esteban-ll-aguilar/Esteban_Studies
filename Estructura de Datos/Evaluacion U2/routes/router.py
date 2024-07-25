from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, flash
from controls.restauranDaoControl import RestautanDaoControl
from controls.menuDaControl import MenuDaoControl

from datetime import datetime
from flask_cors import CORS



router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito
#RUTAS

@router.route('/')
def home():
    return render_template('template.html')


@router.route('/restaurantes')
def ver_clientes():
    restaurant = RestautanDaoControl()
    return render_template('restaurante/lista.html', lista=restaurant.to_dict())

@router.route('/restaurantes/<string:atrr>/<int:tipoOrden>/<int:isAcendent>')
def restaurantes_ordenar(atrr,tipoOrden, isAcendent):
    restaurant = RestautanDaoControl()
    restaurant._lista.sort_models(atrr,tipoOrden, isAcendent)
    return make_response(jsonify({'data': restaurant.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))

@router.route('/restaurantes/search/<string:elemento>/<string:attr>/<int:isLineal>', methods=['GET'])
def restaurantes_buscar(elemento,attr, isLineal):
    print(elemento,attr, isLineal)
    restaurant = RestautanDaoControl()
    restaurant._lista.search_models_equals(elemento,attr, isLineal)
    return make_response(jsonify({'data': restaurant.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))

@router.route('/restaurantes/editar/<int:pos>')
def ver_editar(pos):
    restaurant = RestautanDaoControl()
    restaurant = restaurant._list().get(pos-1)
    return render_template('restaurante/editar.html', data=restaurant)


@router.route('/restaurantes/menu/<string:atrr>/<int:tipoOrden>/<int:isAcendent>')
def menu_ordenar(atrr,tipoOrden, isAcendent):
    menu = MenuDaoControl()
    menu._lista.sort_models(atrr,tipoOrden, isAcendent)
    return make_response(jsonify({'data': menu.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))
    
    
    
    
    
@router.route('/restaurantes/menu/search/<string:elemento>/<string:attr>/<int:isLineal>', methods=['GET'])
def menu_buscar(elemento,attr, isLineal):
    menu = MenuDaoControl()
    menu._lista.search_models_equals(elemento,attr, isLineal)
    return make_response(jsonify({'data': menu.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))
    






@router.route('/nuevo_restaurant')
def ver_guardar():
    return render_template('restaurante/guardar.html')




@router.route('/restaurantes/vermenus/<int:idRestaurant>')
def ver_menus(idRestaurant):
    menu = MenuDaoControl()
    menu._lista._filter(idRestaurant)
    print(menu.to_dict())
    return render_template('menu/listaMenu.html', lista=menu.to_dict_list())


@router.route('/restaurantes/crearmenu/<int:pos>')
def ver_guardar_menus(pos):
    return render_template('menu/guardar_menu.html', data=pos)
    

@router.route('/restaurantes/crearmenu/guardar/<int:pos>', methods=['POST'])
def guardar_menus(pos):
    
    data = request.form
    menu = MenuDaoControl()
    menu._menu._nombre = data['nombre']
    menu._menu._precio = float(data['precio'])
    menu._menu._restauranteId = pos
    menu.save
    return redirect(f'/restaurantes/vermenus/{pos}', code=302)













@router.route('/nuevo_restaurante/guardar', methods=['POST'])
def guardar_restaurantes():
    data = request.form
    restaurant = RestautanDaoControl()

    restaurant._restaurant._nombre = data['nombre']
    restaurant._restaurant._codigoDePermiso = data['codigoDePermiso']
    restaurant._restaurant._estrellas = int(data['estrellas'])
    restaurant.save
        
    
    return redirect('/restaurantes', code=302)

@router.route('/restaurantes/detalle/<int:pos>')
def ver_detalle_restaurantes(pos):
    restaurant = RestautanDaoControl()
    nene = restaurant._list().get(pos-1)
    return render_template('restaurante/detalle.html', data=nene)




@router.route('/restaurantes/modificar/<int:pos>', methods=['POST'])
def modificar_restaurantes(pos):
    restaurant = RestautanDaoControl()
    data = request.form
    pos = pos - 1
    nene = restaurant._list().get(pos)
    print(nene)
    print(data)

    
    restaurant._restaurant = nene
    restaurant._restaurant._nombre = data['nombre']
    restaurant._restaurant._codigoDePermiso = data['codigoDePermiso']
    restaurant._restaurant._estrellas = data['estrellas']
    restaurant.merge(pos)
    return redirect('/restaurantes', code=302)

