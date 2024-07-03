var nodes = new vis.DataSet([{id:1, label: "1"}]);

 var edges = new vis.DataSet([
]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);