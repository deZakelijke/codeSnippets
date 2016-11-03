# Made by micha de Groot
# LSD Radix sort
# Python cannot do negative integer radixsort. 
# Integers do not have a fixed size, making it impssible (very hard)
# to place negtive numbers of various sizes in the right bin.
# Strings can be tried, however Unicode allows more than a million
# different characters. This could require a million bins.
# Only ASCII can be done easily

import math

# Should be called with (List,1, base)
# base should be the size of the alphabet
def radixSortF(unsortedList, digitIndex, base):
    if unsortedList == []:
        return []
    buckets = [] 
    for i in range(base):
        buckets.append([])
    modNumber = 10 ** digitIndex
    digits = 0
    for i in range(len(unsortedList)):
        index = (unsortedList[i]%modNumber)//(modNumber//10)
        buckets[index].append(unsortedList[i])
        if unsortedList[i] > 0:
            tempDigits = int(math.log10(unsortedList[i]))+1
        elif unsortedList[i] == 0:
            tempDigits  = 0
        else: 
            tempDigits = int(math.log10(-unsortedList[i]))+2
        if tempDigits > digits:
            digits = tempDigits
    buckets = [item for sublist in buckets for item in sublist]
    if(digitIndex <= digits):
        buckets = radixSortF(buckets,digitIndex+1, base) 
    return buckets

def radixSort(unsorted):
    if isinstance(unsorted[0], int) or isinstance(unsorted[0], long):
        for i in range(len(unsorted)):
            if unsorted[i] <0:
                raise Exception('radix sord cannot handle negative numbers yet!')
        return radixSortF(unsorted,1,10)
    elif isinstance(unsorted[0], str):
        #return radixSortF(unsorted,1,'unicode max, I guess')
        raise Exception('radixSort cannot handle strings yet!')
    elif isinstance(unsorted[0], float):
        raise Exception('radixSort cannot sort floats.')
    else:
        raise Exception('Cannot sort this.')




