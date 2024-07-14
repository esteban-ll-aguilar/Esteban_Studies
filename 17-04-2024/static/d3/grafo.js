var nodes = new vis.DataSet([
{id:0, label: "1 El Dragon"},
{id:1, label: "2 hola"},
{id:2, label: "3 El Esteban"},
{id:3, label: "4 El solito"},
{id:4, label: "5 LOLITA"},
{id:5, label: "6 Mishel"},
{id:6, label: "7 Solene"},
{id:7, label: "8 Mumuso"},
{id:8, label: "9 Joaquin"}]);

 var edges = new vis.DataSet([{
from: 0, to: 3, label: "200.72"},{
from: 0, to: 2, label: "160.23"},{
from: 1, to: 5, label: "63.38"},{
from: 1, to: 3, label: "8.19"},{
from: 2, to: 0, label: "160.23"},{
from: 2, to: 4, label: "33.4"},{
from: 2, to: 5, label: "70.09"},{
from: 3, to: 0, label: "200.72"},{
from: 3, to: 1, label: "8.19"},{
from: 3, to: 6, label: "53.04"},{
from: 3, to: 8, label: "8.06"},{
from: 4, to: 2, label: "33.4"},{
from: 4, to: 6, label: "53.72"},{
from: 5, to: 1, label: "63.38"},{
from: 5, to: 2, label: "70.09"},{
from: 5, to: 7, label: "62.57"},{
from: 6, to: 3, label: "53.04"},{
from: 6, to: 4, label: "53.72"},{
from: 7, to: 5, label: "62.57"},{
from: 8, to: 3, label: "8.06"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);