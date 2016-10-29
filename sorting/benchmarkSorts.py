# Made by Micha de Groot
# used to compare several sorting algorithms

from quickSort import *
from radixSort import *
from mergeSort import *
import sys
import time
import random



# unsorted is a list of variables.
# listType is a string, describing the unsortedList.
# algorihms is a list of strings, each string is a function name
# of a soring function, taking a list as input

def sortList(unsorted, listType, algorithms):
    print('Type of list is: ', listType)
    print('Number of sorted elements is: ', len(unsorted))
    for i in range(len(algorithms)):
        begin = time.time()
        try:
            newSorted = eval(algorithms[i]+'(unsorted)')
            end = time.time()
            print("The", algorithms[i], "function took ", end-begin, " seconds.")
        except Exception:
            print("The", algorithms[i], "function could not sort this type of list.")
    print('\n')
            
def main():
    algorithms = [
    'mergeSort',
    'quickSort',
    'radixSort',
    ]

    listType = 'Positive integers, random'
    unsorted = []
    for i in range(50000):
        unsorted.append(random.randrange(0,100000))
    sortList(unsorted, listType, algorithms)

    listType = 'Positive integers, half sort, half random'
    unsorted = []
    randNum = random.randrange(0,100000)
    for i in range(20000):
        unsorted.append(randNum)
    for i in range(20000):
        unsorted.append(random.randrange(0,100000))
    sortList(unsorted, listType, algorithms)


    listType = 'Positive and negative integers, random'
    unsorted = []
    for i in range(50000):
        unsorted.append(random.randrange(-100000,100000))
    sortList(unsorted, listType, algorithms)

    listType = 'Positive floating points, random'
    unsorted = []
    for i in range(10000):
        unsorted.append(random.random())
    sortList(unsorted, listType, algorithms)
    

main()

