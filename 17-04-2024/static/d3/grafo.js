var nodes = new vis.DataSet([
{id:0, label: "1 El Dragon"},
{id:1, label: "2 hola"},
{id:2, label: "3 El Esteban"},
{id:3, label: "4 El solito"},
{id:4, label: "5 LOLITA"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "204.02"},{
from: 0, to: 2, label: "160.23"},{
from: 1, to: 2, label: "46.49"},{
from: 1, to: 0, label: "204.02"},{
from: 1, to: 4, label: "13.43"},{
from: 2, to: 3, label: "46.13"},{
from: 3, to: 4, label: "13.33"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);