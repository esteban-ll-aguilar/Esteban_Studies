var nodes = new vis.DataSet([
{id:0, label: "Sabor y Aroma"},
{id:1, label: "El Dragon"},
{id:2, label: "Bistro Eclat"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "3.77"},{
from: 1, to: 0, label: "3.77"},{
from: 1, to: 2, label: "254.49"},{
from: 2, to: 1, label: "254.49"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);
var advertencia = document.getElementById("advertencia");
advertencia.innerHTML = ""
var camino = document.getElementById("camino");
 camino.innerHTML = "Desde: 'Sabor y Aroma' hacia 'El Dragon' con una distancia de 3.77 km -><br>Desde: 'El Dragon' hacia 'Bistro Eclat' con una distancia de 254.49 km";
var weigths = document.getElementById("weigths");
 weigths.innerHTML = "Distancia Total de recorrido: 258.26 km";