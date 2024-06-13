class ShellSort:
    
    def sort_acendent(self, array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                t = array[i]
                j = i
                while j >= gap and array[j-gap] > t:
                    array[j] = array[j-gap]
                    j -= gap
                array[j] = t
            gap //= 2
        return array
    
    
    def sort_desendent(self, array):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                t = array[i]
                j = i
                while j >= gap and array[j-gap] < t:
                    array[j] = array[j-gap]
                    j -= gap
                array[j] = t
            gap //= 2
        return array
    
    
    def sort_models_acendent(self, array, attribute):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                t = array[i]
                j = i
                while j >= gap and getattr(array[j-gap], attribute) > getattr(t, attribute):
                    array[j] = array[j-gap]
                    j -= gap
                array[j] = t
            gap //= 2
        return array
    
    
    def sort_models_desendent(self, array, attribute):
        gap = len(array) // 2
        while gap > 0:
            for i in range(gap, len(array)):
                t = array[i]
                j = i
                while j >= gap and getattr(array[j-gap], attribute) < getattr(t, attribute):
                    array[j] = array[j-gap]
                    j -= gap
                array[j] = t
            gap //= 2
        return array