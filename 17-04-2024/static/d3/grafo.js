var nodes = new vis.DataSet([
{id:1, label: "Garcia Esteban"},
{id:2, label: "Cabrera Alicia"},
{id:3, label: "Perez Juan"},
{id:4, label: "nan"},
{id:5, label: "nan"}]);

 var edges = new vis.DataSet([{
from: 1, to: 1, label: "10"},{
from: 1, to: 2, label: "20"},{
from: 2, to: 3, label: "20"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);