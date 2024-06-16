class MergeSort:
    def sort_asendent(self, array):
        if len(array) <= 1:
            return array
        else: 
            return self.merge_sort(array, True)
    
    def sort_descendent(self, array):
        if len(array) <= 1:
            return array
        else: 
            return self.merge_sort(array, False)
    
    
    def sort_models_acendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else: 
            return self.merge_sort_models(array, attribute, True)
            
    def sort_models_descendent(self, array, attribute):
        if len(array) <= 1:
            return array
        else: 
            return self.merge_sort_models(array, attribute, False)
    
    
    def merge_sort_models(self, array, attribute, isacendent=True):
        if len(array) > 1:
            mitad = len(array) // 2
            izquierda = array[:mitad]
            derecha = array[mitad:]
        
            self.merge_sort_models(izquierda, attribute, isacendent)
            self.merge_sort_models(derecha, attribute, isacendent)
            
            aux = []
            
            if isacendent:
                while len(izquierda) > 0 and len(derecha) > 0:
                    if getattr(izquierda[0], attribute) > getattr(derecha[0], attribute):
                        aux.append(izquierda.pop(0))
                    else:
                        aux.append(derecha.pop(0))
            else: 
                while len(izquierda) > 0 and len(derecha) > 0:
                    if getattr(izquierda[0], attribute) < getattr(derecha[0], attribute):
                        aux.append(izquierda.pop(0))
                    else:
                        aux.append(derecha.pop(0))
                        
            while len(izquierda) > 0:
                aux.append(izquierda.pop(0))
            while len(derecha) > 0:
                aux.append(derecha.pop(0))
                
            return aux
        
    def merge_sort(self, array, isacendent=True):  
        if len(array) > 1:
            mitad = len(array) // 2
            izquierda = array[:mitad]
            derecha = array[mitad:]
        
            self.merge_sort(izquierda, isacendent)
            self.merge_sort(derecha, isacendent)
            
            aux = []
            
            if isacendent:
                while len(izquierda) > 0 and len(derecha) > 0:
                    if izquierda[0] < derecha[0]:
                        aux.append(izquierda.pop(0))
                    else:
                        aux.append(derecha.pop(0))
            else: 
                while len(izquierda) > 0 and len(derecha) > 0:
                    if izquierda[0] > derecha[0]:
                        aux.append(izquierda.pop(0))
                    else:
                        aux.append(derecha.pop(0))
                        
            while len(izquierda) > 0:
                aux.append(izquierda.pop(0))
            while len(derecha) > 0:
                aux.append(derecha.pop(0))
                
            return aux
            
            
            