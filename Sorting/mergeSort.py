"""
############################
# Abir Hasan Mubin         #
# abirhasanmubin@gmail.com #
############################
"""


def mergeSort(arr):
    """
    * * mergeSort [
        * Takes an list of elements and sorts its elements in ascending order.
        * Uses divide and conquer approach.
        * Time Average Complexity : O(nlogn).
        * ]

    * Arguments:
        @param arr {[list]} -- [List of numbers]

    """

    if len(arr) > 1:
        midIndex = len(arr)//2
        # Slicing list in two temporary list
        sl1 = arr[:midIndex]
        sl2 = arr[midIndex:]
        # Sorting the temporary lists
        mergeSort(sl1)
        mergeSort(sl2)
        # Merging the list
        i = j = k = 0
        while (i < len(sl1) and j < len(sl2)):
            if sl1[i] < sl2[j]:
                arr[k] = sl1[i]
                i += 1
            else:
                arr[k] = sl2[j]
                j += 1
            k += 1
        while (i < len(sl1)):
            arr[k] = sl1[i]
            i += 1
            k += 1
        while (j < len(sl2)):
            arr[k] = sl2[j]
            j += 1
            k += 1


# Running function

list1 = [1, 10, 9, 8, 2, 6, 3, 4, 5, 7]
mergeSort(list1)
print(list1)
