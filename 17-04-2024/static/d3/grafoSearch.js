var nodes = new vis.DataSet([
{id:0, label: "14 Platica"},
{id:1, label: "6 Artisanal Creations"},
{id:2, label: "8 Mumuso"},
{id:3, label: "11 Exaple Cutye"},
{id:4, label: "13 Otra Rolita"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "63.38"},{
from: 1, to: 0, label: "63.38"},{
from: 1, to: 2, label: "62.57"},{
from: 2, to: 1, label: "62.57"},{
from: 2, to: 3, label: "91.53"},{
from: 3, to: 2, label: "91.53"},{
from: 3, to: 4, label: "76.24"},{
from: 4, to: 3, label: "76.24"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);var camino = document.getElementById("camino");
 camino.innerHTML = " 14 Platica =>  6 Artisanal Creations =>  8 Mumuso =>  11 Exaple Cutye =>  13 Otra Rolita ";var weigths = document.getElementById("weigths");
 weigths.innerHTML = "293.72";