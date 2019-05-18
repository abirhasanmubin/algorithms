"""
############################
# Abir Hasan Mubin         #
# abirhasanmubin@gmail.com #
############################
"""


def bubbleSort(arr):
    """
    * * bubbleSort [
        * Takes an list of elements and sorts its elements in ascending order.
        * Time Complexity : O(n^2)
        * ]

    * Arguments:
        @param arr {[list]} -- [List of numbers]
    """
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            # Checking the two elments for sorting
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]


# Test algorithm

list1 = [1, 10, 9, 8, 2, 6, 3, 4, 5, 7]
bubbleSort(list1)
print(list1)
