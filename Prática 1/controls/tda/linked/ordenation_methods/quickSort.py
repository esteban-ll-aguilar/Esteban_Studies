class QuickSort:
    
    def sort_asendent(self, array):
        if len(array)<=1:
            return array
        else:
            pivote = array[0]
            lower = []
            equal = []
            bigger = []
            
            for i in range(0, len(array)):
                if array[i] < pivote:
                    lower.append(array[i])
                elif array[i] == pivote:
                    equal.append(array[i])
                else:
                    bigger.append(array[i])
                    
            lower = self.sort_asendent(lower)
            bigger = self.sort_asendent(bigger)
            array = lower + equal + bigger
            return array
        
    def sort_descendent(self, array):
        if len(array)<=1:
            return array
        else:
            pivote = array[0]
            lower = []
            equal = []
            bigger = []
            
            for i in range(0, len(array)):
                if array[i] < pivote:
                    lower.append(array[i])
                elif array[i] == pivote:
                    equal.append(array[i])
                else:
                    bigger.append(array[i])
                    
            lower = self.sort_descendent(lower)
            bigger = self.sort_descendent(bigger)
            array = bigger + equal + lower
            return array
        
        
    def sort_models_acendent(self, array, attribute):
        if len(array)<=1:
            return array
        else:
            pivote = getattr(array[0], attribute)
            lower = []
            equal = []
            bigger = []
            for i in range(0, len(array)):
                print(getattr(array[i], attribute))
                att = getattr(array[i], attribute)
                if att < pivote:
                    lower.append(array[i])
                elif att == pivote:
                    equal.append(array[i])
                else:
                    bigger.append(array[i])
                    
            lower = self.sort_models_acendent(lower, attribute)
            bigger = self.sort_models_acendent(bigger, attribute)
            
            array = lower + equal + bigger
            return array
            
            
            
            
    def sort_models_descendent(self, array, attribute):
        if len(array)<=1:
            return array
        else:
            pivote = getattr(array[0], attribute)
            lower = []
            equal = []
            bigger = []
            for i in range(0, len(array)):
                att = getattr(array[i], attribute)
                if att < pivote:
                    lower.append(array[i])
                elif att == pivote:
                    equal.append(array[i])
                else:
                    bigger.append(array[i])
                    
            lower = self.sort_models_descendent(lower, attribute)
            bigger = self.sort_models_descendent(bigger, attribute)
            
            array = bigger + equal + lower
            return array
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    