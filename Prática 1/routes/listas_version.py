from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.personaListControl import PersonaListControl
from controls.facturaListControl import FacturaListControl
from controls.retencionListDaoControl import RetencionListDaoControl
from datetime import datetime
from flask_cors import CORS

listas_version = Blueprint('listas_version', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito
#RUTAS
@listas_version.route('/')
def home():
    return render_template('template.html')

@listas_version.route('/cliente/detalle/factura/<int:pos>')
def guardar_factura(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('facturacion/guardar_factura.html', data=nene)

@listas_version.route('/retencion/<int:pos>', methods=['POST'])
def generarRetencion(pos):
    fdc = FacturaListControl()
    fdc._factura = fdc._lista.get(pos-1)
    generar_retencion = RetencionListDaoControl()
    data = request.form
    generar_retencion._retencion._clienteId = data['dni']
    generar_retencion._retencion._facturaId = data['NComprobante']
    generar_retencion._retencion._baseImponible =float(data['subtotal'])
    generar_retencion._retencion._fechaEmicion = datetime.today().strftime("%Y-%m-%d %H:%M")
    if data['tipoIdentificacion'] == 'RUC EDUCATIVO':
        generar_retencion._retencion._porcentajeRetencion = 0.08
    elif data['tipoIdentificacion']  == 'RUC PROFESIONAL':
        generar_retencion._retencion._porcentajeRetencion = 0.1
    
    
    
    generar_retencion._retencion._totalRetenido = float(data['subtotal']) * generar_retencion._retencion._porcentajeRetencion
    print(generar_retencion._retencion.serialize)
    generar_retencion.save
    fdc._detele(pos)
    #fdc.delete(pos)
    
    return redirect(f'/cliente/detalle/historial_retencion/{data['clienteId']}', code=302)

@listas_version.route('/clientes')
def ver_clientes():
    pd = PersonaListControl()
    print(pd.to_dict())
    return render_template('cliente/lista.html', lista=pd.to_dict())

@listas_version.route('/cliente/editar/<int:pos>')
def ver_editar(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/editar.html', data=nene)



@listas_version.route('/nuevo_cliente')
def ver_guardar():
    return render_template('cliente/guardar.html')

@listas_version.route('/cliente/detalle/factura/generar/<int:pos>', methods=['POST'])
def generar_factura(pos):
    factura = FacturaListControl()
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


@listas_version.route('/cliente/detalle/lista_factura/<int:pos>')
def lista_factura(pos):
    persona = PersonaListControl()
    factura = FacturaListControl()
    persona._persona = persona._lista.get(pos-1)
    lista = factura._lista._filter(persona._persona._dni)
    print(lista)
    return render_template('facturacion/listaFactura.html', lista=lista, persona=persona._persona.serialize)

@listas_version.route('/cliente/detalle/historial_retencion/<int:pos>')
def lista_retencion(pos):
    persona = PersonaListControl()
    retencion = RetencionListDaoControl()
    persona._persona = persona._lista.get(pos-1)
    print(persona._persona._dni)
    lista = retencion._lista._stack._class._filter(persona._persona._dni)
    return render_template('retencion/historial_retencion.html', lista=lista, persona=persona._persona.serialize)


@listas_version.route('/nuevo_cliente/guardar', methods=['POST'])
def guardar_cliente():
    data = request.form
    pd = PersonaListControl()
    data = request.form
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

@listas_version.route('/cliente/detalle/<int:pos>')
def ver_detalle_cliente(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/detalle.html', data=nene)








@listas_version.route('/personas/modificar', methods=['POST'])
def modificar_persona():
    pd = PersonaListControl()
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

