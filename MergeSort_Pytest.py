
from random import randint
def mergeSort(myList):
    if len(myList) > 1:
        mid = len(myList) // 2
        left = myList[:mid]
        right = myList[mid:]
        mergeSort(left)
        mergeSort(right)
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                myList[k] = left[i]
                i += 1
            else:
                myList[k] = right[j]
                j += 1

            k += 1
        while i < len(left):
            myList[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            myList[k] = right[j]
            j += 1
            k += 1


def test_Merge():
    """ Algorithm of  Merge sort  """
    size = randint(10, 10)
    A = []
    for i in range(0, size):
        A.append(randint(0, 100))
    print(A)
    d = size-1
    Merge1 = mergeSort(A)
    print(A)
    status = True
    for i in range(0,d):
        if A[i] > A[i + 1]:
            status = False
    assert status, " Your method is not working correctly  "

