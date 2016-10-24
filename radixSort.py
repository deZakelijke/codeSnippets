# Made by micha de Groot
# LSD Radix sort

import math

# Should be called with (List,1, base)
# base should be the size of the alphabet
def radixSort(unsortedList, digitIndex, base):
    if unsortedList == []:
        return []
    buckets = [] 
    for i in range(base):
        buckets.append([])
    modNumber = 10 ** digitIndex
    digits = 0
    for i in range(len(unsortedList)):
        index = 9 -(unsortedList[i]%modNumber)//(modNumber//10)
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
        buckets = radixSort(buckets,digitIndex+1, base) 
    return buckets

sortedList = radixSort([23,54,12,71, 73, 44, 99],1,10)
print(sortedList)
