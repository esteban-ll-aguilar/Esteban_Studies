var nodes = new vis.DataSet([{id:1, label: "Perez Juan"},{id:2, label: "Cruz Esteban"},{id:3, label: "Perez Pedro"}]);

 var edges = new vis.DataSet([
{from: 1, to: 2, label: "10"},{from: 2, to: 1, label: "20"},{from: 2, to: 3, label: "30"},{from: 3, to: 2, label: "40"}]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);