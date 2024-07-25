var nodes = new vis.DataSet([
{id:0, label: "Cafe Aroma"},
{id:1, label: "El Dragon"},
{id:2, label: "El Rincon Gastronomico"},
{id:3, label: "Pizzeria Italiana"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "26.8"},{
from: 1, to: 0, label: "26.8"},{
from: 1, to: 2, label: "10.97"},{
from: 2, to: 1, label: "10.97"},{
from: 2, to: 3, label: "8.54"},{
from: 3, to: 2, label: "8.54"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);
var advertencia = document.getElementById("advertencia");
advertencia.innerHTML = ""
var camino = document.getElementById("camino");
 camino.innerHTML = "Desde: 'Cafe Aroma' hacia 'El Dragon' con una distancia de 26.8 km -><br>Desde: 'El Dragon' hacia 'El Rincon Gastronomico' con una distancia de 10.97 km -><br>Desde: 'El Rincon Gastronomico' hacia 'Pizzeria Italiana' con una distancia de 8.54 km";
var weigths = document.getElementById("weigths");
 weigths.innerHTML = "Distancia Total de recorrido: 46.31 km";