from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.personaDaoControl import PersonaDaoControl
from controls.liquido.negocioDaoControl import NegocioDaoControl
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.liquido.negocioGrafo import NegocioGrafo
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



#NEGOCIO
@router.route('/negocio')
def lista_negocios():
    pd = NegocioDaoControl()
    list = pd._lista
    if not list.isEmpty:
        list.sort_models('_nombre')
    return render_template('liquido/lista.html', lista=pd.to_dict_lista())

@router.route('/negocio/editar/<pos>')
def ver_negocio_editar(pos):
    pd = NegocioDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('liquido/editar.html', data=nene)

@router.route('/negocio/formulario')
def ver_negocio_guardar():
    return render_template('liquido/guardar.html')


@router.route('/mapa')
def mapa():
    return render_template('mapa/grafo.html')

@router.route('/negocio/grafo_negocio')
def grafo_negocio():
    ng = NegocioGrafo()
    ng.get_graph
    return render_template('mapa/grafo.html' )


@router.route('/negocio/grafo_ver_admin')
def grafo_ver_admin():
    negocio = NegocioDaoControl()
    #negociograph = NegocioGrafo()   
    list = negocio._lista
    #negociograph = negociograph.get_graph
    #print(negociograph)
    
    if not list.isEmpty:
        list.sort_models('_nombre',2)    
    return render_template('liquido/grafo.html', lista=negocio.to_dict_lista())
    #return jsonify(negocio.to_dict_lista())

@router.route('/negocio/grafo_negocio/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    print(data)
    ng = NegocioGrafo()
    ng.get_graph.insert_edges(int(data['origen'])-1, int(data['destino'])-1)
    ng.save_graph
    return redirect('/negocio/grafo_ver_admin', code=302)

@router.route('/negocio/guardar', methods=['POST'])
def negocio_guardar():
    negocio = NegocioDaoControl()
    print('----------------------------------')
    data = request.form
    print(data)
    
    negocio._negocio._nombre = data['nombre']
    negocio._negocio._direccion = data['direccion']
    negocio._negocio._horario = data['horario']
    negocio._negocio._longitud = float(data['longitud'])
    negocio._negocio._latitud = float(data['latitud'])
    negocio.save
    
    
    return redirect('/negocio', code=302)




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







