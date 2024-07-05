import sys
import os 
from math import nan
class Graph:
    def __init__(self):
        self.__URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__)))))) + '/static/'
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
    """ def setLabel(self, vertex, label):
        raise NotImplementedError("Please implement this method")"""
    def getLabel(self, vertex):
        raise NotImplementedError("Please implement this method")
    
    def __str__(self) -> str:
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
            
        return out
    
    @property
    def paint_graph(self, file='d3/grafo.js'):
        url = self.__URL + file
        print(url)
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i+1)+', label: "'+str(i+1)+'"},'
        js = js[:-1]
        js += ']);\n'
    
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    @property
    def paint_graph_labeled(self, file='d3/grafo.js'):
        url = self.__URL + file
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i+1)+', label: "'+str(self.getLabel(i))+'"},'
        js = js[:-1]
        js += ']);\n'
        
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i+1)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    def paint_map_labeled(self, file='d3/mapa.js'):
        url = self.__URL + file
        """ var marker = L.marker([45565, -0.09]).addTo(map);
        marker.bindPopup("<b>Hello world!</b><br>I am a popup.").openPopup(); """
        js = ''
        for i in range(0, self.num_vertex):
            obj = self.getLabel(i)
            print(obj)
            if obj is nan:
                js+= f'var {obj} = L.marker([0,0]).addTo(map);\n'
            else:
                js+= f'var {(obj._nombre).replace(" ","")} = L.marker(['+str(obj._latitud)+','+str(obj._longitud )+']).addTo(map);\n'
                js+= f'{(obj._nombre).replace(" ","")}.bindPopup("<b>{obj._nombre}</b><br>{obj._direccion}").openPopup();\n'
            
        a = open(url , 'w')
        a.write(js)
        a.close()
        
    @property
    def print_graph(self):
        print(self.__str__())
        
    @property
    def print_graph_labeled(self):
        out = ""
        for i in range(0, self.num_vertex):
            out += "V" + str(i) + " -> " + str(self.getLabel(i)) + " -> "
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    out += "ady V" + str(adj._destination+1) + " weigth " + str(adj._weigth) + " -> \n"
            
        print(out)
