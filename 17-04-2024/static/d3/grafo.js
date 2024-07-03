var nodes = new vis.DataSet([{id:1, label: "1"},{id:2, label: "2"},{id:3, label: "3"},{id:4, label: "4"},{id:5, label: "5"}]);

 var edges = new vis.DataSet([
{from: 1, to: 1, label: "10"},{from: 1, to: 2, label: "20"},{from: 2, to: 0, label: "10"},{from: 2, to: 3, label: "20"},{from: 3, to: 0, label: "20"},{from: 4, to: 1, label: "20"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);