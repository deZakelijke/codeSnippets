# Made by Micha de Groot

def mergeSort(listA):
    if len(listA) == 1:
        return listA
    left = []
    right = []
    halfPoint = len(listA) // 2
    for i in range(len(listA)):
        if i < halfPoint:
            left.append(listA[i])
        else:
            right.append(listA[i])

    leftS = mergeSort(left)
    rightS = mergeSort(right)
    return merge(leftS, rightS)

def merge(left, right):
    result = []

    while left != [] and right != []:
        if(left[0] <= right[0]):
            result.append(left[0])
            left = left[1:]
        else:
            result.append(right[0])
            right = right[1:]

    while left != []:
        result.append(left[0])
        left = left[1:]
    while right != []:  
        result.append(right[0])
        right = right[1:]

    return result
