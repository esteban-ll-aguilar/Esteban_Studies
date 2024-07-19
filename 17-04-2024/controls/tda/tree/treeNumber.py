from controls.tda.linked.linkedList import Linked_List
from controls.tda.tree.node import Node
class TreeNumber():
    def __init__(self):
        self.__root = None
        self.__height = 0
        self.__nro_nodes = 0
        self.__levels = Linked_List()
        self.__order = Linked_List()
        
    @property
    def getNroNodes(self):
        return self.__nro_nodes
    
    @property
    def getLevels(self):
        return self.__levels
    @property
    def getHeigth(self):
        return self.__height
    
    
    
    def __calcHeight(self, tree):
        if tree == None:
            return 0
        else:
            left = self.__calcHeight(tree._left)
            right = self.__calcHeight(tree._right)
            if left > right:
                left +=1
                return left
            else:
                right += 1
                return right
            
    
    
    
    def __calcLevels(self, tree, level):
        if tree != None:
            self.__levels.get(level).add(tree)
            level += 1
            self.__calcLevels(tree._left, level)
            self.__calcLevels(tree._right, level)
        else:
            self.__levels.get(level).add(None)
            level += 1
            self.__calcLevels(None, level)
            self.__calcLevels(None, level)
            
    def levels(self):
        self.__levels = Linked_List()
        #TODO calc height
        self.__height = self.__calcHeight(self.__root)
        for i in range (0, self.__height):
            self.__levels.add(Linked_List())
        
    def insert(self, data):
        if self.__root == None:
            self.__root = Node(data)
            self.__nro_nodes += 1
            self.levels()
            return True
        else:
            new = Node(data)
            recent  = self.__root
            father = None
            while(True):
                father = recent
                if data == recent._data:
                    return False
                elif data < recent._data:
                    recent = recent._left
                    if recent == None:
                        new._father = father
                        father._left = new
                        self.__nro_nodes +=1
                        self.levels()

                        return True
                else:
                    recent = recent._right
                    if recent == None:
                        new._father = father
                        father._right = new
                        self.__nro_nodes +=1
                        self.levels()
                        return True
    
    def show_tree(self):
        self.__order = Linked_List()
        self.__pre_order(self.__root)
        return self.__order

    # def show_tree(self):
    #     out = ""
    #     for i in range(0, self.__height):
    #         for j in range(0, self.__levels.get(i)._length):
    #             if self.__levels.get(i).get(j) != None:
    #                 out += str(self.__levels.get(i).get(j)._data) + " "
    #             else:
    #                 out += "None "
    #         out += "\n"
    #     return out
    
    def __pre_order(self, tree):
        if tree != None:
            self.__order.add(tree._data, self.__order._length)
            self.__pre_order(tree._left)
            self.__pre_order(tree._right)
                        
    def pre_orders(self):
        self.__order = Linked_List()
        self.__pre_order(self.__root)
        return self.__order
    

    def __pos_order(self, tree):
        if tree != None:
            self.__pos_order(tree._left)
            self.__pos_order(tree._right)
            self.__order.add(tree._data, self.__order._length)
                        
    def pos_orders(self):
        self.__order = Linked_List()
        self.__pos_order(self.__root)
        return self.__order
    
    def __in_order(self, tree):
        if tree != None:
            self.__in_order(tree._left)
            self.__order.add(tree._data, self.__order._length)
            self.__in_order(tree._right)
                        
    def in_orders(self):
        self.__order = Linked_List()
        self.__in_order(self.__root)
        return self.__order