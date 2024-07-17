var nodes = new vis.DataSet([
{id:0, label: "Creative Minds Studio"},
{id:1, label: "Artisanal Creations"},
{id:2, label: "GreenLeaf Organics"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "63.38"},{
from: 1, to: 0, label: "63.38"},{
from: 1, to: 2, label: "63.25"},{
from: 2, to: 1, label: "63.25"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);var camino = document.getElementById("camino");
 camino.innerHTML = " Creative Minds Studio =>  Artisanal Creations =>  GreenLeaf Organics ";var weigths = document.getElementById("weigths");
 weigths.innerHTML = "126.63";