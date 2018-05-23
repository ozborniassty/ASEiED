import numpy as np
import time



def bubble_sort(elements):
    continueSorting = True
    start = time.time()

    while(continueSorting):

        changedSth = False
        for indx, x in enumerate(elements):
            try:
                if elements[indx] > elements[indx + 1]:
                    elements[indx], elements[indx + 1] = elements[indx + 1], elements[indx]
                    changedSth = True
            except:
                pass
        if changedSth == False:
            continueSorting = False

    end = time.time()
    print("bubble sort time: ",end - start)

    return elements


def selectionSort(elements):
    start = time.time()

    for x in range(len(elements)):
        smallestIndx = x
        smallestElem = elements[x]

        indx = 0

        for y in range(indx + x, len(elements)):
            if elements[y] < smallestElem:
                smallestIndx = y
                smallestElem = elements[y]

        elements[x], elements[smallestIndx] = elements[smallestIndx], elements[x]

    end = time.time()
    print("selectionSortTime: ", end - start)
    return elements


def quicksort(elements):

    if len(elements) <=1:
        return elements
    else:
        smaller_part, equal, larger_part = [], [], []
        pivot = elements[int(len(elements) / 2)]

        for element in elements:
            if element < pivot:
                smaller_part.append(element)
            elif element == pivot:
                equal.append(element)
            elif element > pivot:
                larger_part.append(element)


        try:
            return quicksort(smaller_part) + equal + quicksort(larger_part)
        except:
            pass



elements = np.random.permutation(np.arange(5000))
elem2 = np.copy(elements)
elem3 = np.copy(elements)

start = time.time()
quicksort(elements)
end = time.time()
print("quick sort time: ", end - start)

selectionSort(elem3)
bubble_sort(elem2)

pass