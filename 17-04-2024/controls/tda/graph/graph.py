import sys
import os 
from math import nan
class Graph:
    @property
    def num_vertex(self):
        raise NotImplementedError("Please implement this method")
    @property
    def num_edges(self):
        raise NotImplementedError("Please implement this method")
    
    def exist_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def weigth_edges(self, v1,v2):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges_weigth(self, v1, v2, weigth):
        raise NotImplementedError("Please implement this method")
    
    def insert_edges(self, v1, v2):
        raise NotImplementedError("Please implement this method")
    
    def adjacent(v1):
        raise NotImplementedError("Please implement this method")
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i+1) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
            
        return out
    
    @property
    def paint_graph(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__)))))) + '/static/d3/grafo.js'
        print(url)
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '{id:'+str(i+1)+', label: "'+str(i+1)+'"},'
        js = js[:-1]
        js += ']);\n'
    
        js+= '\n var edges = new vis.DataSet([\n'
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{from: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    @property
    def paint_graph_model(self):
        url = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__)))))) + '/static/d3/grafo.js'
        auxjs = 'var nodes = new vis.DataSet(['
        
        
        js= '\n var edges = new vis.DataSet([\n'
        labels = []
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    if not labels.__contains__(adj._label):
                        labels.append(adj._label)
                        print(adj._label)
                        auxjs+= '{id:'+str(len(labels))+', label: "'+str(adj._label)+'"},'
                    js += '{from: '+str(i+1)+', to: '+str(adj._destination+1)+', label: "'+str(adj._weigth)+'"},'
                
        
        auxjs = auxjs[:-1]
        auxjs += ']);\n'
        js = js[:-1]
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'        
        a = open(url , 'w')
        a.write(auxjs+js)
        a.close()
        
        
    
    @property
    def print(self):
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i+1) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
        print(out)
        
    @property
    def print_model(self):
        out = ""
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            out += "V" + str(i+1) + " -> "
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._label) +str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
        print(out)
