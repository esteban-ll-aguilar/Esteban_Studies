var nodes = new vis.DataSet([
{id:1, label: "0 El Dragon"},
{id:2, label: "nan"},
{id:3, label: "nan"},
{id:4, label: "nan"},
{id:5, label: "nan"}]);

 var edges = new vis.DataSet([]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);