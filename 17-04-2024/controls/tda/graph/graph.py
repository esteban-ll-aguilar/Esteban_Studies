import sys
import os , json
from math import nan
class Graph:
    def __init__(self):
        self.__URL = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(os.path.abspath(__file__))))))
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
    
    def getVertex(self, label):
        raise NotImplementedError("Please implement this method")
    
    def fileExists(self, file):
        url = self.__URL +'/data/'+file
        return os.path.exists(url)
    
    
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
        url = self.__URL +'/static/'+ file
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
        url = self.__URL +'/static/'+ file
        js = 'var nodes = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            js+= '\n{id:'+str(i)+', label: "'+str(self.getLabel(i))+'"},'
        js = js[:-1]
        js += ']);\n'
        
        js+= '\n var edges = new vis.DataSet(['
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            if not adjs.isEmpty:
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    js += '{\nfrom: '+str(i)+', to: '+str(adj._destination)+', label: "'+str(adj._weigth)+'"},'
        js += ']);\n'
        js += 'var container = document.getElementById("mynetwork"); \n var data = { nodes: nodes, edges: edges, }; \n var options = {}; \nvar network = new vis.Network(container, data, options);'
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


    

    def __transform__(self):
        json = "["
        for i in range(0, self.num_vertex):
            adjs = self.adjacent(i)
            json += '\n\t{\n\t\t"labelId":' + f"{str(self.getVertex(self.getLabel(i)))},"
            json += '\n\t\t"label": "' + str(self.getLabel(i)) + '",'
            if not adjs.isEmpty:
                json += '\n\t\t"destinations": ['
                for j in range(0, adjs._length):
                    adj = adjs.get(j)
                    json += '\n\t\t\t{\n\t\t\t\t"from":'+f"{str(self.getVertex(self.getLabel(i)))}"+', \n\t\t\t\t"to":'+str(adj._destination)+'\n\t\t\t},'
                json = json[:-1]
                json += '\n\t\t]'
                json += '\n\t},'
            else:
                json += '\n\t\t"destinations": []\n'
                json = json[:-1]
                json +='\n\t},'
            adjs = self.adjacent(i)
        json = json[:-1]
        json += "\n]"
        
        return json
    
    def save_graph_labeled(self, file='grafo.json'):
        url = self.__URL +'/data/'+file
        a = open(url , 'w')
        a.write(self.__transform__())
        a.close()
        
    def recontruct_graph(self, file='grafo.json', atype: object = None):
        url = self.__URL +'/data/'+file
        a = open(url , 'r')
        data = json.load(a)
        a.close()
        newGraph = atype(len(data))
        for item in data:
            print(item)
            newGraph.labelVertex(item['labelId'], item['label'])
        
        for item in data:
            destination = item['destinations']
            print(destination)
            if destination != []:
                for dest in item['destinations']:
                    newGraph.insert_edges(dest['from'], dest['to'])
        return newGraph
        
        
    
        
        
        