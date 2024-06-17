from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, flash
from controls.retencionListDaoControl import RetencionListDaoControl
from controls.retencionDaoControl import RetencionDaoControl
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
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

@router.route('/cliente/detalle/factura/<int:pos>')
def guardar_factura(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(pos-1)
    return render_template('facturacion/guardar_factura.html', data=nene)

@router.route('/retencion/<int:pos>', methods=['POST'])
def generarRetencion(pos):
    fdc = FacturaDaoControl()
    retencion = RetencionDaoControl()
    fdc._factura = fdc._lista.get(pos-1)
    data = request.form
    retencion._retencion._clienteId = data['dni']
    retencion._retencion._facturaId = data['NComprobante']
    retencion._retencion._baseImponible =float(data['subtotal'])
    retencion._retencion._fechaEmicion = datetime.today().strftime("%Y-%m-%d")
    print(data['tipoIdentificacion'])
    if data['tipoIdentificacion'] == 'RUC EDUCATIVO':
        retencion._retencion._porcentajeRetencion = 0.08
    elif data['tipoIdentificacion']  == 'RUC PROFESIONAL':
        retencion._retencion._porcentajeRetencion = 0.10
    
    

    retencion._retencion._totalRetenido = float(data['subtotal']) * retencion._retencion._porcentajeRetencion
    retencion.save
    
    fdc.delete(pos)
    #fdc.delete(pos)
    
    return redirect(f'/cliente/detalle/historial_retencion/{data['clienteId']}', code=302)

@router.route('/clientes')
def ver_clientes():
    pd = PersonaDaoControl()
    return render_template('cliente/lista.html', lista=pd.to_dict())

@router.route('/clientes/<string:atrr>/<int:tipoOrden>/<int:isAcendent>')
def clientes_ordenar(atrr,tipoOrden, isAcendent):
    pd = PersonaDaoControl()
    pd._lista.sort_models(atrr,tipoOrden, isAcendent)

    return make_response(jsonify({'data': pd.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))

@router.route('/clientes/search/<string:elemento>/<string:attr>/<int:isLineal>', methods=['GET'])
def clientes_buscar(elemento,attr, isLineal):
    print(elemento,attr, isLineal)
    pd = PersonaDaoControl()
    
    pd._lista.search_models_equals(elemento,attr, isLineal)
    return make_response(jsonify({'data': pd.to_dict_list(), 'code': 200, 'message': 'Ordenado'}))

@router.route('/cliente/editar/<int:pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/editar.html', data=nene)


@router.route('/nuevo_cliente')
def ver_guardar():
    return render_template('cliente/guardar.html')

@router.route('/cliente/detalle/factura/generar/<int:pos>', methods=['POST'])
def generar_factura(pos):
    factura = FacturaDaoControl()
    data = request.form
    if factura._lista.__exist__(data['NComprobante']) != True:
        print('se guardo') 
        factura._factura._fecha = data['fecha']
        factura._factura._clienteId = data['dni']
        factura._factura._NComprobante = data['NComprobante']
        factura._factura._subtotal = float(data['subtotal'])
        factura._factura._iva = float(data['iva'])
        factura._factura._total = float(data['total'])
        factura._factura._clienteId = data['dni']
        factura.save
    return redirect(f'/cliente/detalle/lista_factura/{pos}', code=302)


@router.route('/cliente/detalle/lista_factura/<int:pos>')
def lista_factura(pos):
    persona = PersonaDaoControl()
    factura = FacturaDaoControl()
    persona._persona = persona._lista.get(pos-1)
    lista = factura._lista._filter(persona._persona._dni)
    list = factura.to_dict_list()
    if list == None or len(list) == 0 or list == 'List is Empty':
        flash('No hay facturas registradas', 'info')
        return redirect(f'/cliente/detalle/{pos}', code=302 )
    return render_template('facturacion/listaFactura.html', lista=factura.to_dict_list(), persona=persona._persona.serialize)


@router.route('/cliente/detalle/lista_factura/<int:pos>/<string:atrr>/<int:tipoOrden>/<int:isAcendent>')
def lista_factura_ordenar(pos,atrr,tipoOrden, isAcendent):
        persona = PersonaDaoControl()
        factura = FacturaDaoControl()
        persona._persona = persona._lista.get(pos-1)
        factura._lista._filter(persona._persona._dni)
        factura._lista.sort_models(atrr,tipoOrden, isAcendent)
        return make_response(jsonify({'data': factura.to_dict_list(), 'persona':persona._persona.serialize, 'code': 200, 'message': 'Ordenado'}))


@router.route('/cliente/detalle/lista_factura/search/<int:pos>/<string:elemento>/<string:attr>/<int:isLineal>')
def lista_factura_buscar(pos,elemento,attr, isLineal):
    persona = PersonaDaoControl()
    factura = FacturaDaoControl()
    persona._persona = persona._lista.get(pos-1)
    factura._lista._filter(persona._persona._dni)
    factura._lista.search_models_equals(elemento,attr, isLineal)
    return make_response(jsonify({'data': factura.to_dict_list(), 'persona':persona._persona.serialize, 'code': 200, 'message': 'Ordenado'}))



@router.route('/cliente/detalle/historial_retencion/<int:pos>')
def lista_retencion(pos):
    persona = PersonaDaoControl()
    retencion = RetencionDaoControl()
    persona._persona = persona._lista.get(pos-1)
    retencion._lista._filter(persona._persona._dni)
    if retencion.to_dict_list() == None or len(retencion.to_dict_list()) == 0 or retencion.to_dict_list() == 'List is Empty':
        flash('No hay retenciones registradas', 'info')
        return redirect(f'/cliente/detalle/{pos}', code=302)
    
    return render_template('retencion/historial_retencion.html', lista=retencion.to_dict_list(), persona=persona._persona.serialize)


@router.route('/cliente/detalle/historial_retencion/<int:pos>/<string:atrr>/<int:tipoOrden>/<int:isAcendent>')
def lista_retencion_ordenar(pos,atrr,tipoOrden, isAcendent):
        persona = PersonaDaoControl()
        retencion = RetencionDaoControl()
        persona._persona = persona._lista.get(pos-1)
        retencion._lista._filter(persona._persona._dni)
        retencion._lista.sort_models(atrr,tipoOrden, isAcendent)
        return make_response(jsonify({'data': retencion.to_dict_list(), 'persona':persona._persona.serialize, 'code': 200, 'message': 'Ordenado'}))


@router.route('/cliente/detalle/historial_retencion/search/<int:pos>/<string:elemento>/<string:attr>/<int:isLineal>')
def lista_retencion_buscar(pos,elemento,attr, isLineal):
    persona = PersonaDaoControl()
    retencion = RetencionDaoControl()
    persona._persona = persona._lista.get(pos-1)
    retencion._lista._filter(persona._persona._dni)
    retencion._lista.search_models_equals(elemento,attr, isLineal)
    return make_response(jsonify({'data': retencion.to_dict_list(), 'persona':persona._persona.serialize, 'code': 200, 'message': 'Ordenado'}))
















@router.route('/nuevo_cliente/guardar', methods=['POST'])
def guardar_cliente():
    data = request.form
    pd = PersonaDaoControl()
    if not 'nombre' in data.keys() or not 'apellidos' in data.keys() or not 'telefono' in data.keys() or not 'dni' in data.keys() or not 'direccion' in data.keys():
        abort(400)
    if pd._lista.__exist__(data['dni']) != True:
        pd._persona._nombre = data['nombre']
        pd._persona._apellidos = data['apellidos']
        pd._persona._telefono = data['telefono']
        pd._persona._correo = data['correo']
        pd._persona._dni = data['dni']
        pd._persona._direccion = data['direccion']
        pd._persona._tipoIdentificacion = data['tipoIdentificacion']
        pd.save
        
    
    return redirect('/clientes', code=302)

@router.route('/cliente/detalle/<int:pos>')
def ver_detalle_cliente(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/detalle.html', data=nene)




@router.route('/cliente/modificar/<int:pos>', methods=['POST'])
def modificar_persona(pos):
    pd = PersonaDaoControl()
    data = request.form
    pos = pos - 1
    nene = pd._list().get(pos)
    print(nene)
   

    if not 'nombre' in data.keys() or not 'apellidos' in data.keys() or not 'telefono' in data.keys() or not 'dni' in data.keys() or not 'direccion' in data.keys():
        abort(400)
    #TODO validar
    pd._persona = nene
    pd._persona._nombre = data['nombre']
    pd._persona._apellidos = data['apellidos']
    pd._persona._telefono = data['telefono']
    pd._persona._dni = data['dni']
    pd._persona._direccion = data['direccion']
    pd._persona._tipoIdentificacion = data['tipoIdentificacion']
    pd._persona._correo = data['correo']
    pd.merge(pos)
    return redirect('/clientes', code=302)

