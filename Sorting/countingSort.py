"""
############################
# Abir Hasan Mubin         #
# abirhasanmubin@gmail.com #
############################
"""


def countingSort(arr):
    ma = 0
    for i in arr:
        ma = max(ma, i)
    count = [0 for i in range(ma + 1)]
    for i in arr:
        count[i] += 1
    for i in range(len(count)):
        if count[i] > 0:
            print(i, count[i])


# Driver Program
list1 = [1, 10, 9, 8, 2, 6, 3, 4, 5, 7]
countingSort(list1)
