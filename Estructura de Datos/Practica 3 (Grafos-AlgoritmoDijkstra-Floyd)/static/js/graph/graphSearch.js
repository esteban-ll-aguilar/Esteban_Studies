var nodes = new vis.DataSet([
{id:0, label: "El Dragon"},
{id:1, label: "El Rincon Gastronomico"},
{id:2, label: "Pizzeria Italiana"},
{id:3, label: "La Parrilla Grill"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "10.97"},{
from: 1, to: 0, label: "10.97"},{
from: 1, to: 2, label: "8.54"},{
from: 2, to: 1, label: "8.54"},{
from: 2, to: 3, label: "11.6"},{
from: 3, to: 2, label: "11.6"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);
var advertencia = document.getElementById("advertencia");
advertencia.innerHTML = ""
var camino = document.getElementById("camino");
 camino.innerHTML = "Desde: 'El Dragon' hacia 'El Rincon Gastronomico' con una distancia de 10.97 km -><br>Desde: 'El Rincon Gastronomico' hacia 'Pizzeria Italiana' con una distancia de 8.54 km -><br>Desde: 'Pizzeria Italiana' hacia 'La Parrilla Grill' con una distancia de 11.6 km";
var weigths = document.getElementById("weigths");
 weigths.innerHTML = "Distancia Total de recorrido: 31.11 km";