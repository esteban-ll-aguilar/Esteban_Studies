var nodes = new vis.DataSet([
{id:0, label: "Central Park"},
{id:1, label: "Parque Pedrito"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "4862.58"},{
from: 1, to: 0, label: "4862.58"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);
var advertencia = document.getElementById("advertencia");
advertencia.innerHTML = ""
var camino = document.getElementById("camino");
 camino.innerHTML = "Desde: 'Central Park' hacia 'Parque Pedrito' con una distancia de 4862.58 km";
var weigths = document.getElementById("weigths");
 weigths.innerHTML = "Distancia Total de recorrido: 4862.58 km";