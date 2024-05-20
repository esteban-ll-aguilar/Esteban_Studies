from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort, flash
from controls.personaListControl import PersonaListControl
from controls.facturaListControl import FacturaListControl
from controls.retencionListDaoControl import RetencionListDaoControl
from datetime import datetime
from flask_cors import CORS

array_version = Blueprint('array_version', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito
#RUTAS
RETENCION = RetencionListDaoControl(False,25)

@array_version.route('/')
def home():
    return render_template('template.html')

@array_version.route('/cliente/detalle/factura/<int:pos>')
def guardar_factura(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('facturacion/guardar_factura.html', data=nene)

@array_version.route('/retencion/<int:pos>', methods=['POST'])
def generarRetencion(pos):
    fdc = FacturaListControl()
    fdc._factura = fdc._lista.get(pos-1)
    data = request.form
    RETENCION._retencion._clienteId = data['dni']
    RETENCION._retencion._facturaId = data['NComprobante']
    RETENCION._retencion._baseImponible =float(data['subtotal'])
    RETENCION._retencion._fechaEmicion = datetime.today().strftime("%Y-%m-%d %H:%M")
    print(data['tipoIdentificacion'])
    if data['tipoIdentificacion'] == 'RUC EDUCATIVO':
        RETENCION._retencion._porcentajeRetencion = 0.08
    elif data['tipoIdentificacion']  == 'RUC PROFESIONAL':
        RETENCION._retencion._porcentajeRetencion = 0.10
    
    

    RETENCION._retencion._totalRetenido = float(data['subtotal']) * RETENCION._retencion._porcentajeRetencion
    RETENCION.save
    
    fdc._detele(pos)
    #fdc.delete(pos)
    
    return redirect(f'/cliente/detalle/historial_retencion/{data['clienteId']}', code=302)

@array_version.route('/clientes')
def ver_clientes():
    pd = PersonaListControl()
    print(pd.to_dict())
    return render_template('cliente/lista.html', lista=pd.to_dict())

@array_version.route('/cliente/editar/<int:pos>')
def ver_editar(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/editar.html', data=nene)



@array_version.route('/nuevo_cliente')
def ver_guardar():
    return render_template('cliente/guardar.html')

@array_version.route('/cliente/detalle/factura/generar/<int:pos>', methods=['POST'])
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


@array_version.route('/cliente/detalle/lista_factura/<int:pos>')
def lista_factura(pos):
    persona = PersonaListControl()
    factura = FacturaListControl()
    persona._persona = persona._lista.get(pos-1)
    lista = factura._lista._filter(persona._persona._dni)
    if lista == None or len(lista) == 0:
        flash('No hay facturas registradas', 'info')
        return redirect(f'/cliente/detalle/{pos}', code=302, )
    return render_template('facturacion/listaFactura.html', lista=lista, persona=persona._persona.serialize)

@array_version.route('/cliente/detalle/historial_retencion/<int:pos>')
def lista_retencion(pos):
    persona = PersonaListControl()
    persona._persona = persona._lista.get(pos-1)
    print(persona._persona._dni)
    lista = RETENCION._lista._stack._class._filter(persona._persona._dni)
    if lista == None or len(lista) == 0:
        flash('No hay retenciones registradas', 'info')
        return redirect(f'/cliente/detalle/{pos}', code=302)
    
    
    return render_template('retencion/historial_retencion.html', lista=lista, persona=persona._persona.serialize)


@array_version.route('/nuevo_cliente/guardar', methods=['POST'])
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

@array_version.route('/cliente/detalle/<int:pos>')
def ver_detalle_cliente(pos):
    pd = PersonaListControl()
    nene = pd._list().get(pos-1)
    return render_template('cliente/detalle.html', data=nene)








@array_version.route('/cliente/modificar/<int:pos>', methods=['POST'])
def modificar_persona(pos):
    pd = PersonaListControl()
    data = request.form
    nene = pd._list().get(pos-1)
   
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
    pd._persona._tipoIdentificacion = data['tipoIdentificacion']
    pd._persona._correo = data['correo']
    pd.merge(pos)
    return redirect('/clientes', code=302)

