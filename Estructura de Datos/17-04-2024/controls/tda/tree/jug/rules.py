from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.jug.node import Node
class Rules():
    def rules(self, jb, jl):
        x = jb._current_capacity
        y = jl._current_capacity
        rules = Linked_List()
        
        #regla 1 : Llenar jarra grande de 4 litros no esta completamente llena
        if x < jb._capacity:
            node = Node()
            node.set_current_capacity(jb._capacity, y)
            rules.add(node, rules._length)
        
        #regla 1 : Llenar jarra pequena de 3 litros no esta completamente llena
        if y < jb._capacity:
            node = Node()
            node.set_current_capacity(x, jl._capacity)
            rules.add(node, rules._length)
        #regla 3 : Vaciar jarra grande de 4 litros no esta completamente vacia
        if x > 0:
            node = Node()
            node.set_current_capacity(0, y)
            rules.add(node, rules._length)
        
        #regla 4 : Vaciar jarra pequena de 3 litros no esta completamente vacia
        if y > 0:
            node = Node()
            node.set_current_capacity(x, 0)
            rules.add(node, rules._length)
        
        #regla 5 : Llenar jarra grande de 4 litros con jarra pequena de 3 litros
        if x+y >= jb._capacity and (x < jb._capacity and y > 0):
            node = Node()
            node.set_current_capacity(jb._capacity, y-(jb._capacity-x))
            rules.add(node, rules._length)
            
        #regla 6 : Llenar jarra pequena de 3 litros con jarra grande de 4 litros
        if x+y >= jl._capacity and (y < jl._capacity and x > 0):
            node = Node()
            node.set_current_capacity(x-(jl._capacity-y), jl._capacity)
            rules.add(node, rules._length)
            
            
        #regla 7 : Vaciar jarra grande de 4 litros en jarra pequena de 3 litros
        if x+y <= jl._capacity and x>0:
            node = Node()
            node.set_current_capacity(0, x+y)
            rules.add(node, rules._length)
            
        #regla 8 : Vaciar jarra pequena de 3 litros en jarra grande de 4 litros
        if x+y <= jb._capacity and y>0:
            node = Node()
            node.set_current_capacity(x+y, 0)
            rules.add(node, rules._length)
            
        return rules