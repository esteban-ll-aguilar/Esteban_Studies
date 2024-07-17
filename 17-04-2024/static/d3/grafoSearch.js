var nodes = new vis.DataSet([
{id:0, label: "holita"},
{id:1, label: "EstebanQuito"},
{id:2, label: "Platica"},
{id:3, label: "Artisanal Creations"},
{id:4, label: "GreenLeaf Organics"},
{id:5, label: "Otra Rondita"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "6.47"},{
from: 1, to: 0, label: "6.47"},{
from: 1, to: 2, label: "34.07"},{
from: 2, to: 1, label: "34.07"},{
from: 2, to: 3, label: "63.38"},{
from: 3, to: 2, label: "63.38"},{
from: 3, to: 4, label: "63.25"},{
from: 4, to: 3, label: "63.25"},{
from: 4, to: 5, label: "7.42"},{
from: 5, to: 4, label: "7.42"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);var camino = document.getElementById("camino");
 camino.innerHTML = " holita =>  EstebanQuito =>  Platica =>  Artisanal Creations =>  GreenLeaf Organics =>  Otra Rondita ";var weigths = document.getElementById("weigths");
 weigths.innerHTML = "174.59";