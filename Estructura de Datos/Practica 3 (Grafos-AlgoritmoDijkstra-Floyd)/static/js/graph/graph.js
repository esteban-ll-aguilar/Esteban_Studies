var nodes = new vis.DataSet([
{id:0, label: "Parque Jipiro"},
{id:1, label: "Parque Central (Parque Bolivar)"},
{id:2, label: "Parque Lineal La Tebaida"},
{id:3, label: "Parque Pucara"},
{id:4, label: "Parque Universitario La Argelia"},
{id:5, label: "Parque Infantil Daniel Alvarez Burneo"},
{id:6, label: "Parque San Sebastian"},
{id:7, label: "Parque Simon Bolivar"},
{id:8, label: "Parque Lineal Zamora Huayco"},
{id:9, label: "Parque de la Madre"},
{id:10, label: "Parque San Jose"},
{id:11, label: "Parque Colinas Lojanas"},
{id:12, label: "Parque La Alborada"},
{id:13, label: "Parque Las Palmas"},
{id:14, label: "Parque Ciudadela Zamora"},
{id:15, label: "Parque La Sede"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "2.58"},{
from: 0, to: 5, label: "3.72"},{
from: 0, to: 13, label: "16.47"},{
from: 1, to: 0, label: "2.58"},{
from: 1, to: 14, label: "0.78"},{
from: 1, to: 11, label: "3.5"},{
from: 1, to: 5, label: "1.22"},{
from: 1, to: 12, label: "93.36"},{
from: 1, to: 15, label: "1.72"},{
from: 1, to: 13, label: "16.09"},{
from: 1, to: 10, label: "3.95"},{
from: 1, to: 2, label: "2.58"},{
from: 1, to: 8, label: "2.36"},{
from: 1, to: 3, label: "1.61"},{
from: 1, to: 6, label: "0.83"},{
from: 1, to: 7, label: "1.03"},{
from: 1, to: 4, label: "5.02"},{
from: 1, to: 9, label: "1.43"},{
from: 2, to: 1, label: "2.58"},{
from: 2, to: 15, label: "1.05"},{
from: 2, to: 13, label: "16.4"},{
from: 2, to: 7, label: "1.62"},{
from: 2, to: 8, label: "2.2"},{
from: 2, to: 3, label: "1.44"},{
from: 2, to: 6, label: "1.86"},{
from: 2, to: 10, label: "3.94"},{
from: 3, to: 1, label: "1.61"},{
from: 3, to: 2, label: "1.44"},{
from: 3, to: 4, label: "3.74"},{
from: 3, to: 6, label: "0.79"},{
from: 3, to: 12, label: "93.56"},{
from: 4, to: 1, label: "5.02"},{
from: 4, to: 3, label: "3.74"},{
from: 4, to: 7, label: "4.04"},{
from: 4, to: 6, label: "4.28"},{
from: 5, to: 0, label: "3.72"},{
from: 5, to: 1, label: "1.22"},{
from: 5, to: 8, label: "1.49"},{
from: 5, to: 10, label: "4.15"},{
from: 5, to: 14, label: "1.22"},{
from: 6, to: 1, label: "0.83"},{
from: 6, to: 2, label: "1.86"},{
from: 6, to: 3, label: "0.79"},{
from: 6, to: 4, label: "4.28"},{
from: 6, to: 7, label: "0.24"},{
from: 7, to: 1, label: "1.03"},{
from: 7, to: 2, label: "1.62"},{
from: 7, to: 4, label: "4.04"},{
from: 7, to: 6, label: "0.24"},{
from: 7, to: 9, label: "2.42"},{
from: 7, to: 14, label: "1.12"},{
from: 8, to: 1, label: "2.36"},{
from: 8, to: 2, label: "2.2"},{
from: 8, to: 5, label: "1.49"},{
from: 8, to: 15, label: "1.4"},{
from: 8, to: 13, label: "18.07"},{
from: 8, to: 10, label: "5.6"},{
from: 9, to: 1, label: "1.43"},{
from: 9, to: 7, label: "2.42"},{
from: 9, to: 11, label: "4.75"},{
from: 9, to: 13, label: "16.21"},{
from: 10, to: 1, label: "3.95"},{
from: 10, to: 2, label: "3.94"},{
from: 10, to: 5, label: "4.15"},{
from: 10, to: 8, label: "5.6"},{
from: 11, to: 1, label: "3.5"},{
from: 11, to: 9, label: "4.75"},{
from: 12, to: 1, label: "93.36"},{
from: 12, to: 3, label: "93.56"},{
from: 12, to: 14, label: "94.08"},{
from: 13, to: 0, label: "16.47"},{
from: 13, to: 1, label: "16.09"},{
from: 13, to: 2, label: "16.4"},{
from: 13, to: 8, label: "18.07"},{
from: 13, to: 9, label: "16.21"},{
from: 13, to: 15, label: "16.72"},{
from: 14, to: 1, label: "0.78"},{
from: 14, to: 5, label: "1.22"},{
from: 14, to: 7, label: "1.12"},{
from: 14, to: 12, label: "94.08"},{
from: 15, to: 1, label: "1.72"},{
from: 15, to: 2, label: "1.05"},{
from: 15, to: 8, label: "1.4"},{
from: 15, to: 13, label: "16.72"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {nodes: { shape: "dot", size: 20, color: { border: "#2b2b2b", background: "#4a90e2", highlight: { border: "#1c1c1c", background: "#1f77d0" }, hover: { border: "#000000", background: "#c0c0c0" } }, font: { color: "#7928ab", size: 16, face: "verdana", background: "#c0c0c0" ,}, borderWidth: 2 },  edges: { width: 0.5, color: { color: "#7f8c8d", highlight: "#e74c3c", hover: "#95a5a6", opacity: 0.6 }, smooth: { type: "continuous", forceDirection: "none", roundness: 0.2 } }, layout: { improvedLayout: true, hierarchical: false }, physics: { enabled: true, barnesHut: { gravitationalConstant: -2000, centralGravity: 0.4, springLength: 290, springConstant: 0.04, damping: 0.09, avoidOverlap: 0.5 }, stabilization: { iterations: 300, updateInterval: 25 } } };
var network = new vis.Network(container, data, options);