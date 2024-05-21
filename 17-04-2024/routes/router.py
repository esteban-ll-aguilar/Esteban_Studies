from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.personaDaoControl import PersonaDaoControl
from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito

@router.route('/')
def home():
    return render_template('template.html')

# RENDERS A LOS TEMPLATES
@router.route('/personas')
def ver_personas():
    pd = PersonaDaoControl()
    return render_template('nene/lista.html', lista=pd.to_dict())

@router.route('/personas/formulario')
def ver_guardar():
    return render_template('nene/guardar.html')

@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('nene/editar.html', data=nene)


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
    pd._persona._tipoIdentificacion = "CEDULA"
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







