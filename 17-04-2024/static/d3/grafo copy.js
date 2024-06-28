var nodes = new vis.DataSet([{id:1,label: "T"},
{id:2,label: "X"},
{id:3,label: "Y"},
{id:4,label: "Z"},
{id:5,label: "W"},
]);
var edges = new vis.DataSet([
{from:1,to: 3, label:"0.63"},
{from:1,to: 2, label:"0.82"},
{from:2,to: 4, label:"1.24"},
{from:2,to: 1, label:"0.82"},
{from:2,to: 3, label:"1.42"},
{from:3,to: 1, label:"0.63"},
{from:3,to: 5, label:"2.71"},
{from:3,to: 2, label:"1.42"},
{from:4,to: 2, label:"1.24"},
{from:5,to: 3, label:"2.71"},
]);var container = document.getElementById("mynetwork");
      var data = {
        nodes: nodes,
        edges: edges,
      };
      var options = {};
      var network = new vis.Network(container, data, options);
