var nodes = new vis.DataSet([
{id:1, label: "3 El Esteban"},
{id:2, label: "nan"},
{id:3, label: "nan"}]);

 var edges = new vis.DataSet([]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);