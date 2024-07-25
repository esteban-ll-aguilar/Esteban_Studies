from flask import Blueprint, request, render_template, redirect
from datetime import datetime
from flask_cors import CORS
from controls.parqueDaoControl import ParqueDaoControl

router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito
#RUTAS

@router.route('/')
def home():
    return render_template('template.html')

@router.route('/parque')
def ver_parque():
    return render_template('parque/guardar.html')

@router.route('/lista_parque')
def listar_parques():
    pdc = ParqueDaoControl()

    return render_template('parque/lista.html', parque=pdc.to_dict())

@router.route('/editar_parque/<int:pos>')
def editar_parque(pos):
    pd = ParqueDaoControl()
    parque = pd._list().get(pos-1)
    return render_template('parque/editar.html', data=parque)


@router.route('/guardar_parque', methods=['POST'])
def guardar_parque():
    data = request.form
    pdc = ParqueDaoControl()
    if pdc._lista.__exist__(data['nombre']) != True:
        pdc._parque._nombre = data['nombre']
        pdc._parque._direccion = data['direccion']
        pdc._parque._latitud = data['latitud']
        pdc._parque._longitud = data['longitud']
        pdc._parque._detalle = data['detalle']
        pdc.save
    return redirect('/lista_parque', 302)


@router.route('/editar_parque/guardar', methods=['POST'])
def editar_parque_guardar():
    pdc = ParqueDaoControl()
    data = request.form
    pos = int(data['id'])-1
    parque = pdc._list().get(pos)
   
    
    pdc._parque = parque
    pdc._parque._nombre = data['nombre']
    pdc._parque._direccion = data['direccion']
    pdc._parque._latitud = data['latitud']
    pdc._parque._longitud = data['longitud']
    pdc._parque._detalle =data['detalle']
    
    pdc.merge(pos)
    return redirect('/lista_parque', code=302)


#eliminar
@router.route('/eliminar_parque/<int:pos>')
def eliminar_parque(pos):
    pdc = ParqueDaoControl()
    pdc.delete(pos)
    return redirect('/lista_parque', code=302)