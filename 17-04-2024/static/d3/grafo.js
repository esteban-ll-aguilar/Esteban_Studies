var nodes = new vis.DataSet([
{id:0, label: "1 El Dragon"},
{id:1, label: "2 hola"},
{id:2, label: "3 El Esteban"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "nan"},{
from: 0, to: 2, label: "nan"},{
from: 1, to: 2, label: "nan"},{
from: 1, to: 0, label: "nan"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);