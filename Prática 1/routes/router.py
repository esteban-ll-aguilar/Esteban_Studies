from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from controls.retencionDaoControl import RetencionDaoControl
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
    generar_retencion = RetencionDaoControl()
    fdc._factura = fdc._lista.get(pos-1)
    data = request.form
    cliente = data['dni']
    identificacion = data['tipoIdentificacion']
    print(identificacion)
    generar_retencion._retencion._clienteId = cliente
    generar_retencion._retencion._facturaId = fdc._factura._NComprobante
    generar_retencion._retencion._baseImponible = fdc._factura._subtotal
    generar_retencion._retencion._fechaEmicion = datetime.today().strftime("%Y-%m-%d %H:%M")
    if identificacion == 'RUC EDUCATIVO':
        generar_retencion._retencion._porcentajeRetencion = 0.08
    elif identificacion == 'RUC PROFESIONAL':
        generar_retencion._retencion._porcentajeRetencion = 0.1
    
    generar_retencion._retencion._totalRetenido = float(generar_retencion._retencion._baseImponible) * float(generar_retencion._retencion._porcentajeRetencion)
    generar_retencion.save
    
    #fdc.delete(pos)
    
    return redirect(f'/cliente/detalle/historial_retencion/{data['clienteId']}', code=302)

@router.route('/clientes')
def ver_clientes():
    pd = PersonaDaoControl()
    return render_template('cliente/lista.html', lista=pd.to_dict())

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
        factura._factura._subtotal = data['subtotal']
        factura._factura._iva = data['iva']
        factura._factura._total = data['total']
        factura._factura._clienteId = data['dni']
        factura.save
    return redirect(f'/cliente/detalle/lista_factura/{pos}', code=302)


@router.route('/cliente/detalle/lista_factura/<int:pos>')
def lista_factura(pos):
    persona = PersonaDaoControl()
    factura = FacturaDaoControl()
    persona._persona = persona._lista.get(pos-1)
    lista = factura._lista._filter(persona._persona._dni)
    
    return render_template('facturacion/listaFactura.html', lista=lista, persona=persona._persona.serialize)

@router.route('/cliente/detalle/historial_retencion/<int:pos>')
def lista_retencion(pos):
    persona = PersonaDaoControl()
    retencion = RetencionDaoControl()
    persona._persona = persona._lista.get(pos-1)
    lista = retencion._lista._stack._filter(persona._persona._dni)
    return render_template('retencion/historial_retencion.html', lista=lista, persona=persona._persona.serialize)


@router.route('/nuevo_cliente/guardar', methods=['POST'])
def guardar_cliente():
    data = request.form
    pd = PersonaDaoControl()
    data = request.form
    if not 'nombre' in data.keys() or not 'apellidos' in data.keys() or not 'telefono' in data.keys() or not 'dni' in data.keys() or not 'direccion' in data.keys():
        abort(400)
    if pd._lista.__exist__(data['dni']) != True:
        pd._persona._nombre = data['nombre']
        pd._persona._apellidos = data['apellidos']
        pd._persona._telefono = data['telefono']
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




# RENDERS A LOS TEMPLATES
#ClIENTE
""" @router.route('/cliente')
def ver_cliente():
    return render_template('cliente/index.html')

#ADMINISTRADOR
@router.route('/admin')
def ver_administrador():
    return render_template('admin/index.html')


@router.route('/personas')
def ver_personas():
    pd = PersonaDaoControl()
    return render_template('cliente/lista.html', lista=pd.to_dict())

@router.route('/personas/formulario')
def ver_guardar():
    return render_template('cliente/guardar.html')

@router.route('/personas/editar/<int:pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(pos-1)
    print(nene)
    return render_template('cliente/editar.html', data=nene)


@router.route('/cliente/factura')
def ver_factura():
    return render_template('facturacion/factura.html')






#LOGICAS
# GUARDAR PERSONA POST
@router.route('/personas/guardar', methods=['POST'])
def guardar_persona():
    pd = PersonaDaoControl()
    data = request.form
    print(data['direccion'])
    if not 'nombre' in data.keys() or not 'apellidos' in data.keys() or not 'telefono' in data.keys() or not 'dni' in data.keys() or not 'direccion' in data.keys():
        abort(400)
    #TODO validar
    pd._persona._nombre = data['nombre']
    pd._persona._apellidos = data['apellidos']
    pd._persona._telefono = data['telefono']
    pd._persona._dni = data['dni']
    pd._persona._direccion = data['direccion']
    pd._persona._tipoIdentificacion = data['tipoIdentificacion']
    pd.save
    return redirect('/personas', code=302)







@router.route('/personas/modificar', methods=['POST'])
def modificar_persona():
    pd = PersonaDaoControl()
    data = request.form
    pos = int(data['id'])-1
    nene = pd._list().get(pos)
   
    print('----------------------------------')
    print(nene)
    print('----------------------------------')
    print(pos)
    if not 'nombre' in data.keys() or not 'apellidos' in data.keys() or not 'telefono' in data.keys() or not 'dni' in data.keys() or not 'direccion' in data.keys():
        abort(400)
    #TODO validar
    pd._persona = nene
    pd._persona._nombre = data['nombre']
    pd._persona._apellidos = data['apellidos']
    pd._persona._telefono = data['telefono']
    pd._persona._dni = data['dni']
    pd._persona._direccion = data['direccion']
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.merge(pos)
    return redirect('/personas', code=302)

 """





