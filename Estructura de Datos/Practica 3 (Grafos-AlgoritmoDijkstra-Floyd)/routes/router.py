from flask import Blueprint, jsonify, make_response, request, render_template, redirect, abort
from controls.modelDaoControls.parqueDaoControl import ParqueDaoControl
from controls.tda.graph.graphLabeledNoManaged import GraphLabeledNoManaged
from controls.modelGraphsControl.parqueGrafo import ParqueGrafo
from controls.tda.graph.searchMethod.dijkstraAlgorithm import DijkstraAlgorithm
from controls.tda.graph.searchMethod.floydWarshallAlgorithm import FloydWarshallAlgorithm
from flask_cors import CORS
router = Blueprint('router', __name__)
#get para presentar los datos
#post para enviar los datos, modificar y iniciar sesion
# monolito

@router.route('/')
def lista_parques():
    pd = ParqueDaoControl()
    list = pd._lista
    if not list.isEmpty:
        list.sort_models('_nombre')
        return render_template('parque/lista.html', lista=pd.to_dict_lista())
    return render_template('parque/lista.html', lista=[])



#parque

@router.route('/parque/editar/<pos>')
def ver_parque_editar(pos):
    pd = ParqueDaoControl()
    nene = pd._list().get(int(pos)-1)
    print(nene)
    return render_template('parque/editar.html', data=nene)

@router.route('/parque/formulario')
def ver_parque_guardar():
    return render_template('parque/guardar.html')


@router.route('/grafo')
def mapa():
    return render_template('grafo/grafo.html')

@router.route('/parque/grafo_parque')
def grafo_parque():
    parque = ParqueDaoControl()
    list = parque._lista
    if not list.isEmpty:
        list.sort_models('_nombre') 
        
    ng = ParqueGrafo()
    ng.get_graph
    if list.isEmpty:
        return render_template('parque/grafo.html', parques=[], grafoparque=[])
    
    if ng.get_graph.allVertexConnected != True:
        return render_template('graph/graph.html')
    
    return render_template('parque/grafo.html' , parques=parque.to_dict_lista())

#BUSCAR CAMINO
@router.route('/parque/buscar-camino-corto', methods=['POST'])
def buscar_camino_corto():
    parquegraph = ParqueGrafo()
    data = request.form
    if not data:
        return redirect('/parque/grafo_parque', code=404)
    if data['algoritmo'] == '0':
        search = DijkstraAlgorithm(parquegraph.get_graph, int(data['origen']), int(data['destino']))
        search.dijkstra
    else:
        search = FloydWarshallAlgorithm(parquegraph.get_graph, int(data['origen']), int(data['destino']))
        search.floydWarshall
    return redirect('/parque/grafo_parque', code=302)


@router.route('/parque/grafo_ver_admin')
def grafo_ver_admin():
    parque = ParqueDaoControl()
    parquegraph = ParqueGrafo()  
    parquegraph.get_graph
    list = parque._lista
    if not list.isEmpty:
        list.sort_models('_nombre')    
        return render_template('parque/adyacencias.html', lista=parque.to_dict_lista(), grafolista=parquegraph.obtainWeigths)
    return render_template('parque/adyacencias.html')



@router.route('/parque/grafo_parque/agregar_adyacencia', methods=['POST'])
def agregar_adyacencia():
    data = request.form
    print(data)
    ng = ParqueGrafo()
    if not data or ng.get_graph == []:
        return redirect('/parque/grafo_ver_admin', code=404)
    
    ng.get_graph.insert_edges(int(data['origen'])-1, int(data['destino'])-1)
    ng.save_graph
    return redirect('/parque/grafo_ver_admin', code=302)

@router.route('/parque/guardar', methods=['POST'])
def parque_guardar():
    parque = ParqueDaoControl()
    print('----------------------------------')
    data = request.form
    print(data)
    
    parque._parque._nombre = data['nombre']
    parque._parque._direccion = data['direccion']
    parque._parque._horario = data['horario']
    parque._parque._longitud = float(data['longitud'])
    parque._parque._latitud = float(data['latitud'])
    parque.save
    
    return redirect('/', code=302)



@router.route('/parque/modificar/<int:id>', methods=['POST'])
def parque_modificar(id):
    parque = ParqueDaoControl()
    data = request.form
    print(data)
    parque._parque._id = id
    parque._parque._nombre = data['nombre']
    parque._parque._direccion = data['direccion']
    parque._parque._horario = data['horario']
    parque._parque._longitud = float(data['longitud'])
    parque._parque._latitud = float(data['latitud'])
    parque.merge(id)
    return redirect('/', code=302)





