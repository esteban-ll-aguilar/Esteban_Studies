var nodes = new vis.DataSet([
{id:0, label: "El Dragon"},
{id:1, label: "Cafe Aroma"},
{id:2, label: "Instantes Creativos"},
{id:3, label: "Bistro Eclat"},
{id:4, label: "Sabor y Aroma"},
{id:5, label: "El Rincon Gastronomico"},
{id:6, label: "Pizzeria Italiana"},
{id:7, label: "Hamburgueseria del Centro"},
{id:8, label: "Restaurante El Sabor"},
{id:9, label: "La Parrilla Grill"},
{id:10, label: "Buffet Buen Sabor"},
{id:11, label: "Rosa Chocolate"}]);

 var edges = new vis.DataSet([{
from: 0, to: 1, label: "26.8"},{
from: 0, to: 2, label: "50.55"},{
from: 0, to: 3, label: "254.49"},{
from: 0, to: 4, label: "3.77"},{
from: 0, to: 7, label: "24.21"},{
from: 0, to: 5, label: "10.97"},{
from: 1, to: 0, label: "26.8"},{
from: 1, to: 10, label: "33.48"},{
from: 2, to: 0, label: "50.55"},{
from: 2, to: 5, label: "51.41"},{
from: 2, to: 3, label: "214.9"},{
from: 2, to: 7, label: "64.23"},{
from: 2, to: 9, label: "56.85"},{
from: 3, to: 0, label: "254.49"},{
from: 3, to: 2, label: "214.9"},{
from: 3, to: 9, label: "259.18"},{
from: 3, to: 6, label: "248.27"},{
from: 3, to: 8, label: "245.53"},{
from: 4, to: 0, label: "3.77"},{
from: 4, to: 5, label: "14.32"},{
from: 4, to: 11, label: "44.57"},{
from: 5, to: 0, label: "10.97"},{
from: 5, to: 2, label: "51.41"},{
from: 5, to: 4, label: "14.32"},{
from: 5, to: 6, label: "8.54"},{
from: 6, to: 3, label: "248.27"},{
from: 6, to: 5, label: "8.54"},{
from: 6, to: 9, label: "11.6"},{
from: 7, to: 0, label: "24.21"},{
from: 7, to: 2, label: "64.23"},{
from: 7, to: 8, label: "19.32"},{
from: 8, to: 3, label: "245.53"},{
from: 8, to: 7, label: "19.32"},{
from: 8, to: 9, label: "13.67"},{
from: 9, to: 2, label: "56.85"},{
from: 9, to: 3, label: "259.18"},{
from: 9, to: 6, label: "11.6"},{
from: 9, to: 8, label: "13.67"},{
from: 9, to: 10, label: "7.14"},{
from: 10, to: 1, label: "33.48"},{
from: 10, to: 9, label: "7.14"},{
from: 11, to: 4, label: "44.57"},]);
var container = document.getElementById("mynetwork"); 
 var data = { nodes: nodes, edges: edges, }; 
 var options = {}; 
var network = new vis.Network(container, data, options);