#DAO
'''
Patron de diseno DAO PIS

Dao adapter
* create
* list
* update (change, stafe)
* search

'''

import sys
from time import time
sys.path.append('../')
import os
import psutil
from random import randint

from controls.tda.linked.linkedList import Linked_List
from controls.tda.linked.ordenation_methods.quickSort import QuickSort
from controls.tda.linked.ordenation_methods.shell import ShellSort
from controls.tda.linked.ordenation_methods.mergeSort import MergeSort
from controls.tda.linked.search_methods.binary_search import BinarySearch
from controls.tda.linked.search_methods.sequiential_binary_search import SequentialBinarySearch

from time import time
Linked = Linked_List()
quick = QuickSort()
shell = ShellSort()
merge = MergeSort()
bs = BinarySearch()
sbs = SequentialBinarySearch()
try:
    """ list10000numbres = []
    for i in range(0,10000):
        list10000numbres.append(randint(0,10000))
    
    inicio = time()
    listquick = quick.sort_acendent(list10000numbres)
    print("---------------------------------------------")
    print("QuickSort with 10000 numbers: ", time()-inicio)
    inicio = time()
    listshell = shell.sort_descendent(list10000numbres)
    print("ShellSort with 10000 numbers: ", time()-inicio)
    inicio = time() 
    listamerge = merge.sort_descendent(list10000numbres)
    print("MergeSort with 10000 numbers: ", time()-inicio)
    
    list20000numbres = []
    for i in range(0,20000):
        list20000numbres.append(randint(0,20000))

    inicio = time()
    listquick = quick.sort_acendent(list20000numbres)
    print("---------------------------------------------")
    print("QuickSort with 20000 numbers: ", time()-inicio)
    inicio = time()
    listshell = shell.sort_descendent(list20000numbres)
    print("ShellSort with 20000 numbers: ", time()-inicio)
    inicio = time() 
    listamerge = merge.sort_descendent(list20000numbres)
    print("MergeSort with 20000 numbers: ", time()-inicio)
    
    
    list25000numbres = []
    for i in range(0,25000):
        list25000numbres.append(randint(0,25000))

    inicio = time()
    listquick = quick.sort_acendent(list25000numbres)
    print("---------------------------------------------")
    print("QuickSort with 25000 numbers: ", time()-inicio)
    inicio = time()
    listshell = shell.sort_descendent(list25000numbres)
    print("ShellSort with 25000 numbers: ", time()-inicio)
    inicio = time() 
    listamerge = merge.sort_descendent(list25000numbres)
    print("MergeSort with 25000 numbers: ", time()-inicio) """
    
    
    list10000numbres = []
    for i in range(0,10000):
        list10000numbres.append(randint(0,10000))
    
    list20000numbres = []
    for i in range(0,20000):
        list20000numbres.append(randint(0,20000))
        
    list25000numbres = []
    for i in range(0,25000):
        list25000numbres.append(randint(0,25000))
        
    list10000numbres = quick.sort_descendent(list10000numbres)
    list20000numbres = quick.sort_descendent(list20000numbres)
    list25000numbres = quick.sort_descendent(list25000numbres)
    data = 5265
    
    inicio = time()
    b = bs.search(list10000numbres, data)
    print("---------------------------------------------")
    print("BinarySearch with 10000 numbers: ", time()-inicio, " ", b)
    inicio = time()
    b = sbs.search(list10000numbres, data)
    fin = time()
    print("SequentialBinarySearch with 10000 numbers: ",fin-inicio, " ", b)
    
    inicio = time()
    b = bs.search(list20000numbres, data)
    print("---------------------------------------------")
    print("BinarySearch with 20000 numbers: ", time()-inicio, " ", b)
    inicio = time()
    b = sbs.search(list20000numbres, data)
    print("SequentialBinarySearch with 20000 numbers: ", time()-inicio, " ", b)
    
    inicio = time()
    b = bs.search(list25000numbres, data)
    print("---------------------------------------------")
    print("BinarySearch with 25000 numbers: ", time()-inicio, " ", b)
    inicio = time()
    b = sbs.search(list25000numbres, data)
    print("SequentialBinarySearch with 25000 numbers: ", time()-inicio, " ", b)
    
    
    
    
        
    
    
    
except Exception as e:
    print(e)