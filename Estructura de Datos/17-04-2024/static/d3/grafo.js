var nodes = new vis.DataSet([
{id:0, label: "EcoVerde"},
{id:1, label: "TechNexus"},
{id:2, label: "Gourmet Delights"},
{id:3, label: "Casa Bella"},
{id:4, label: "BlueWave Solutions"},
{id:5, label: "Artisanal Creations"},
{id:6, label: "Urban Oasis"},
{id:7, label: "TechSolutions"},
{id:8, label: "GreenLeaf Organics"},
{id:9, label: "Gourmet Night"},
{id:10, label: "Urban Style Boutique"},
{id:11, label: "Fitness Haven"},
{id:12, label: "Green Thumb Garden Center"},
{id:13, label: "Creative Minds Studio"},
{id:14, label: "Global Travel Agency"},
{id:15, label: "Sparkle & Shine Cleaning"},
{id:16, label: "SmartHome Innovations"},
{id:17, label: "EcoLiving Supplies"}]);

 var edges = new vis.DataSet([{
from: 0, to: 3, label: "200.72"},{
from: 0, to: 2, label: "160.23"},{
from: 0, to: 7, label: "202.99"},{
from: 0, to: 5, label: "181.21"},{
from: 0, to: 10, label: "132.72"},{
from: 0, to: 16, label: "203.46"},{
from: 1, to: 5, label: "63.38"},{
from: 1, to: 3, label: "8.19"},{
from: 1, to: 2, label: "46.49"},{
from: 1, to: 9, label: "4.08"},{
from: 2, to: 0, label: "160.23"},{
from: 2, to: 1, label: "46.49"},{
from: 2, to: 4, label: "33.4"},{
from: 2, to: 5, label: "70.09"},{
from: 3, to: 0, label: "200.72"},{
from: 3, to: 1, label: "8.19"},{
from: 3, to: 6, label: "53.04"},{
from: 3, to: 8, label: "8.06"},{
from: 3, to: 4, label: "13.33"},{
from: 4, to: 2, label: "33.4"},{
from: 4, to: 3, label: "13.33"},{
from: 4, to: 6, label: "53.72"},{
from: 4, to: 8, label: "13.42"},{
from: 4, to: 9, label: "10.05"},{
from: 4, to: 5, label: "59.36"},{
from: 5, to: 0, label: "181.21"},{
from: 5, to: 1, label: "63.38"},{
from: 5, to: 2, label: "70.09"},{
from: 5, to: 4, label: "59.36"},{
from: 5, to: 7, label: "62.57"},{
from: 5, to: 8, label: "63.25"},{
from: 5, to: 13, label: "63.38"},{
from: 6, to: 3, label: "53.04"},{
from: 6, to: 4, label: "53.72"},{
from: 6, to: 7, label: "59.78"},{
from: 7, to: 0, label: "202.99"},{
from: 7, to: 5, label: "62.57"},{
from: 7, to: 6, label: "59.78"},{
from: 7, to: 8, label: "1.02"},{
from: 7, to: 9, label: "3.0"},{
from: 7, to: 10, label: "91.53"},{
from: 8, to: 3, label: "8.06"},{
from: 8, to: 4, label: "13.42"},{
from: 8, to: 5, label: "63.25"},{
from: 8, to: 7, label: "1.02"},{
from: 8, to: 9, label: "4.01"},{
from: 8, to: 11, label: "7.42"},{
from: 9, to: 1, label: "4.08"},{
from: 9, to: 4, label: "10.05"},{
from: 9, to: 7, label: "3.0"},{
from: 9, to: 8, label: "4.01"},{
from: 9, to: 10, label: "88.55"},{
from: 10, to: 0, label: "132.72"},{
from: 10, to: 7, label: "91.53"},{
from: 10, to: 9, label: "88.55"},{
from: 10, to: 12, label: "76.24"},{
from: 11, to: 8, label: "7.42"},{
from: 12, to: 10, label: "76.24"},{
from: 13, to: 5, label: "63.38"},{
from: 13, to: 14, label: "34.07"},{
from: 14, to: 13, label: "34.07"},{
from: 14, to: 15, label: "6.47"},{
from: 15, to: 14, label: "6.47"},{
from: 15, to: 17, label: "35.34"},{
from: 16, to: 0, label: "203.46"},{
from: 17, to: 15, label: "35.34"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);