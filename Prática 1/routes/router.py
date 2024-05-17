from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.personaDaoControl import PersonaDaoControl
from controls.facturaDaoControl import FacturaDaoControl
from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito
#RUTAS
@router.route('/')
def home():
    return render_template('template.html')

@router.route('/factura')
def factura():
    return render_template('facturacion/factura.html')





@router.route('/factura/generar', methods=['POST'])
def generar_factura():
    data = request.form
    factura = FacturaDaoControl()
    persona = PersonaDaoControl()
    factura._factura._fecha = data['fecha']
    factura._factura._NComprobante = data['NComprobante']
    factura._factura._subtotal = data['subtotal']
    factura._factura._iva = data['iva']
    factura._factura._total = data['total']
    factura._factura._clienteId = data['dni']
    factura.save
    
    if persona._lista.__exist__(data['dni']):
        print('Persona ya existe')
        persona._persona = persona._lista.get(persona._persona._id)
    else:
        print('Persona no existe y fue creada')
        persona._persona._nombre = data['nombre']
        persona._persona._apellidos = data['apellidos']
        persona._persona._telefono = data['telefono']
        persona._persona._dni = data['dni']
        persona._persona._direccion = data['direccion']
        persona._persona._tipoIdentificacion = data['tipoIdentificacion']
        persona.save
        
    
    
    return redirect('/factura', code=302)


@router.route('/factura/lista/<int:pos>')
def lista_factura(pos):
    persona = PersonaDaoControl()
    factura = FacturaDaoControl()
    persona._persona = persona._lista.get(pos-1)
    lista = factura._lista._filter(persona._persona._dni)
    
    return render_template('facturacion/listaFactura.html', lista=lista, persona=persona._persona.serialize)
    
    pass





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





