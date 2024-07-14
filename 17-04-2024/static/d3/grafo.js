var nodes = new vis.DataSet([
{id:0, label: "1 El Dragon"},
{id:1, label: "2 hola"},
{id:2, label: "3 El Esteban"},
{id:3, label: "4 El solito"},
{id:4, label: "5 LOLITA"},
{id:5, label: "6 Mishel"}]);

 var edges = new vis.DataSet([{
from: 2, to: 5, label: "70.09"},{
from: 2, to: 0, label: "160.23"},{
from: 3, to: 5, label: "55.22"},{
from: 5, to: 2, label: "70.09"},{
from: 5, to: 3, label: "55.22"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);