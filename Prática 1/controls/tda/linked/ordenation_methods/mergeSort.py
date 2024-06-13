class MergeSort:
    def sort_acendent(self, array):
        n = len(array)
        mitad = n // 2
        derecha = [] 
        izquierda = []
        if n <= 1:
            return array
        else:
            for i in range(0,n):
                if i > mitad:
                    izquierda.append(array[i])
                else:
                    derecha.append(array[i])
            izquierda = self.sort_acendent(izquierda)
            derecha = self.sort_acendent(derecha)
            array = izquierda + derecha
            return array
        
    def sort_descendent(self, array):
        n = len(array)
        mitad = n // 2
        derecha = [] 
        izquierda = []
        if n <= 1:
            return array
        else:
            for i in range(0,n):
                if i < mitad:
                    izquierda.append(array[i])
                else:
                    derecha.append(array[i])
            izquierda = self.sort_acendent(izquierda)
            derecha = self.sort_acendent(derecha)
            array = derecha + izquierda
            return array
        
    def sort_models_acendent(self, array, attribute):
        n = len(array)
        mitad = n // 2
        derecha = [] 
        izquierda = []
        if n <= 1:
            return array
        else:
            for i in range(0,n):
                if  getattr(array[i], attribute) > getattr(array[mitad], attribute):
                    izquierda.append(array[i])
                else:
                    derecha.append(array[i])
            izquierda = self.sort_acendent(izquierda, attribute)
            derecha = self.sort_acendent(derecha, attribute)
            array = izquierda + derecha
            return array
        
    def sort_models_descendent(self, array, attribute):
        n = len(array)
        mitad = n // 2
        derecha = [] 
        izquierda = []
        if n <= 1:
            return array
        else:
            for i in range(0,n):
                if  getattr(array[i], attribute) < getattr(array[mitad], attribute):
                    izquierda.append(array[i])
                else:
                    derecha.append(array[i])
            izquierda = self.sort_acendent(izquierda, attribute)
            derecha = self.sort_acendent(derecha, attribute)
            array = derecha + izquierda
            return array
        