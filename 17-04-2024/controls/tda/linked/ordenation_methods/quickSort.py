class QuickSort:
    
    def quick_sort(self, array, isacendent = True):
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
                    
            lower = self.quick_sort(lower, isacendent)
            bigger = self.quick_sort(bigger, isacendent)
            
            if isacendent:
                array = lower + equal + bigger
            else:
                array = bigger + equal + lower
            return array
        
        
    def quick_sort_models(self, array, attribute, isacendent = True):
        if len(array)<=1:
            return array
        else:
            pivote = getattr(array[0], attribute)[0].lower()
            lower = []
            equal = []
            bigger = []
            for i in range(0, len(array)):
                att = getattr(array[i], attribute)[0].lower()
                if att < pivote:
                    lower.append(array[i])
                elif att == pivote:
                    equal.append(array[i])
                else:
                    bigger.append(array[i])
                    
            lower = self.quick_sort_models(lower, attribute, isacendent)
            bigger = self.quick_sort_models(bigger, attribute, isacendent)
            
            if isacendent:
                array = lower + equal + bigger
            else:
                array = bigger + equal + lower
            return array
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
            
    
    