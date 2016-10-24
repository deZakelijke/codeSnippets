def quickSort(array):
    less = []
    equal = []
    greater = []
    if len(array) > 1:
        pivot = array[0]
        for x in array:
            if x[2] < pivot[2]:
                less.append(x)
            if x[2] == pivot[2]:
                equal.append(x)
            if x[2] > pivot[2]:
                greater.append(x)
        return sort(less)+equal+sort(greater)  
    else:  
        return array

