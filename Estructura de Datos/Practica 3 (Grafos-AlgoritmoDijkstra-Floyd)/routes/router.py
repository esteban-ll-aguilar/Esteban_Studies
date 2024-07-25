from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.modelDaoControls.negocioDaoControl import NegocioDaoControl
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.modelGraphsControl.negocioGrafo import NegocioGrafo
from controls.tda.graph.searchMethod.dijkstraAlgorithm import DijkstraAlgorithm
from controls.tda.graph.searchMethod.floydWarshallAlgorithm import FloydWarshallAlgorithm
from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito

@router.route('/')
def lista_negocios():
    pd = NegocioDaoControl()
    list = pd._lista
    if not list.isEmpty:
        list.sort_models('_nombre')
        return render_template('negocio/lista.html', lista=pd.to_dict_lista())
    return render_template('negocio/lista.html', lista=[])



#NEGOCIO

@router.route('/negocio/editar/<pos>')
def ver_negocio_editar(pos):
    pd = NegocioDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('negocio/editar.html', data=nene)

@router.route('/negocio/formulario')
def ver_negocio_guardar():
    return render_template('negocio/guardar.html')


@router.route('/grafo')
def mapa():
    return render_template('grafo/grafo.html')

@router.route('/negocio/grafo_negocio')
def grafo_negocio():
    negocio = NegocioDaoControl()
    list = negocio._lista
    if not list.isEmpty:
        list.sort_models('_nombre') 
        
    ng = NegocioGrafo()
    ng.get_graph
    if list.isEmpty:
        return render_template('negocio/grafo.html', negocios=[], grafonegocio=[])
    return render_template('negocio/grafo.html' , negocios=negocio.to_dict_lista())

#BUSCAR CAMINO
@router.route('/negocio/buscar-camino-corto', methods=['POST'])
def buscar_camino_corto():
    negociograph = NegocioGrafo()
    data = request.form
    if not data:
        return redirect('/negocio/grafo_negocio', code=404)
    if data['algoritmo'] == '0':
        search = DijkstraAlgorithm(negociograph.get_graph, int(data['origen']), int(data['destino']))
        search.dijkstra
    else:
        search = FloydWarshallAlgorithm(negociograph.get_graph, int(data['destino']), int(data['origen']))
        search.floydWarshall
    return redirect('/negocio/grafo_negocio', code=302)


@router.route('/negocio/grafo_ver_admin')
def grafo_ver_admin():
    negocio = NegocioDaoControl()
    negociograph = NegocioGrafo()  
    negociograph.get_graph
    list = negocio._lista
    if not list.isEmpty:
        list.sort_models('_nombre')    
        return render_template('negocio/adyacencias.html', lista=negocio.to_dict_lista(), grafolista=negociograph.obtainWeigths)
    return render_template('negocio/adyacencias.html')

@router.route('/negocio/grafo_negocio/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    print(data)
    ng = NegocioGrafo()
    if not data or ng.get_graph == []:
        return redirect('/negocio/grafo_ver_admin', code=404)
    
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
    
    return redirect('/', code=302)







