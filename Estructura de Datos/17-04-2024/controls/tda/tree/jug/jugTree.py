from controls.tda.tree.jug.node import Node
from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.jug.rules import Rules
class JugTree:
    def __init__(self, first, last):
        self.__state_first = first
        self.__state_last = last
        self.__nodes = Linked_List()
        self.__list_nodes = Linked_List()
        
    def isNodeSearch(self,na,ns):
        return (na._jb._current_capacity == ns._jb._current_capacity and na._jl._current_capacity == ns._jl._current_capacity)
        
    def search(self):
        try:
            if self.isNodeSearch(self.__state_first, self.__state_last):
                self.__nodes.add(self.__state_last, self.__nodes._length)
            else:
                self.__nodes = Linked_List()
                self.__list_nodes = Linked_List()
                self.__list_nodes.add(self.__state_first, self.__nodes._length)
                while self.__list_nodes._length>0:
                    current = self.__list_nodes.detele()
                    if self.isNodeSearch(current, self.__state_last):
                        return current
                    else:
                        ar = Rules()
                        rules = ar.rules(current._jb, current._jl)
                        rules = self.deleteRules(rules)
                        current.addSuccessor(rules)
                        for i in range(0, rules._length):
                            auxR = rules.get(i)
                            self.__list_nodes.add(auxR, self.__list_nodes._length)
                            self.__nodes.add(auxR, self.__nodes._length)
                            if self.isNodeSearch(auxR, self.__state_last):
                                print("Encontrado")
                                return auxR
        except Exception as e:
            print("Error: ", e)

        return None
    
    def deleteRules(self, rules):
        lista = Linked_List()
        if not (rules.isEmpty and  self.__list_nodes.isEmpty):
            rulesA = rules.toArray
            nodesA = self.__nodes.toArray
            for i in range(0, len(rulesA)):
                nad = True
                for j in range(0, len(nodesA)):
                    if self.isNodeSearch(rulesA[i], nodesA[j]):
                        nad = False
                        break
                if nad:
                    lista.add(rulesA[i])
        return lista
                
            
    
    
    def route(self, node):
        routes = Linked_List()
        while node is not None:
            routes.add(node)
            node = node._father
        return routes