import random


def quicksort(array_to_sort, start, end):
    right = end
    left = start + 1
    continue_move = True

    while continue_move:

        while left <= len(array_to_sort) - 1 and array_to_sort[left] < array_to_sort[start] and left <= right:
            left += 1

        while right >= 0 and array_to_sort[right] > array_to_sort[start] and right >= left:
            right -= 1

        if left > right:
            continue_move = False
        else:
            temp = array_to_sort[left]
            array_to_sort[left] = array_to_sort[right]
            array_to_sort[right] = temp

    temp = array_to_sort[start]
    array_to_sort[start] = array_to_sort[right]
    array_to_sort[right] = temp

    if start < right - 1:
        quicksort(array_to_sort, start, right - 1)
    if end > right + 1:
        quicksort(array_to_sort, right + 1, end)


def check(array_to_check):
    for index in range(len(array_to_check)):
        if index != 0 and array_to_check[index] < array_to_check[index - 1]:
            return False
    return True


randomValuesArray = random.sample(range(1, 100), 20)
print randomValuesArray
quicksort(randomValuesArray, 0, len(randomValuesArray) - 1)
print randomValuesArray
print check(randomValuesArray)
