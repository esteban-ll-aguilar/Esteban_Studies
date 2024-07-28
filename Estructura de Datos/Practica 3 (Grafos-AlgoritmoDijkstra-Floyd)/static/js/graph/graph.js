var nodes = new vis.DataSet([
{id:0, label: "Parque Cruzpamba"},
{id:1, label: "Parque Pedrito"},
{id:2, label: "Central Park"},
{id:3, label: "Hyde Park"},
{id:4, label: "Golden Gate Park"}]);

 var edges = new vis.DataSet([{
from: 0, to: 2, label: "5013.98"},{
from: 0, to: 4, label: "6384.88"},{
from: 0, to: 3, label: "9667.33"},{
from: 0, to: 1, label: "181.92"},{
from: 1, to: 0, label: "181.92"},{
from: 1, to: 2, label: "4862.58"},{
from: 1, to: 4, label: "6352.11"},{
from: 1, to: 3, label: "9485.49"},{
from: 2, to: 0, label: "5013.98"},{
from: 2, to: 1, label: "4862.58"},{
from: 2, to: 4, label: "4146.34"},{
from: 2, to: 3, label: "5575.42"},{
from: 3, to: 0, label: "9667.33"},{
from: 3, to: 1, label: "9485.49"},{
from: 3, to: 2, label: "5575.42"},{
from: 3, to: 4, label: "8640.59"},{
from: 4, to: 0, label: "6384.88"},{
from: 4, to: 1, label: "6352.11"},{
from: 4, to: 2, label: "4146.34"},{
from: 4, to: 3, label: "8640.59"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);