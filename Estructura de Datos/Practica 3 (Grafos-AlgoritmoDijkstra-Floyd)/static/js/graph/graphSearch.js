var nodes = new vis.DataSet([
{id:0, label: "Parque Jipiro"},
{id:1, label: "Parque Ciudadela Zamora"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "2.61"},{
from: 1, to: 0, label: "2.61"},]);
var container = document.getElementById("mynetworkSearch"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {nodes: { shape: "dot", size: 20, color: { border: "#2b2b2b", background: "#4a90e2", highlight: { border: "#1c1c1c", background: "#1f77d0" }, hover: { border: "#000000", background: "#c0c0c0" } }, font: { color: "#7928ab", size: 16, face: "verdana", background: "#c0c0c0" ,}, borderWidth: 2 },  edges: { width: 0.5, color: { color: "#7f8c8d", highlight: "#e74c3c", hover: "#95a5a6", opacity: 0.6 }, smooth: { type: "continuous", forceDirection: "none", roundness: 0.2 } }, layout: { improvedLayout: true, hierarchical: false }, physics: { enabled: true, barnesHut: { gravitationalConstant: -2000, centralGravity: 0.4, springLength: 290, springConstant: 0.04, damping: 0.09, avoidOverlap: 0.5 }, stabilization: { iterations: 300, updateInterval: 25 } } };
var network = new vis.Network(container, data, options);
var advertencia = document.getElementById("advertencia");
advertencia.innerHTML = ""
var camino = document.getElementById("camino");
 camino.innerHTML = "Desde: 'Parque Jipiro' hacia 'Parque Ciudadela Zamora' con una distancia de 2.61 km";
var weigths = document.getElementById("weigths");
 weigths.innerHTML = "Distancia Total de recorrido: 2.61 km";