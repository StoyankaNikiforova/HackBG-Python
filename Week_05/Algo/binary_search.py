def binary_search(array, start, end, element):
    mid = (start + end) // 2
    if array[mid] == element:
        return mid
    if array[mid] > element:
        return binary_search(array, start, mid-1, element)
    else:
        return binary_search(array, mid+1, end, element)


def find_turning_point(array, start, end):
    mid = (start + end) // 2
    if array[start] > array[start + 1]:
        return "Turning point is {} on index {}.".format(array[start + 1], start + 1)
    if mid + 1 >= len(array):
        return end
    if array[mid] > array[mid - 1] and array[mid] > array[mid + 1]:
        return mid
    if array[mid] < array[mid - 1] and array[mid] > array[mid + 1]:
        return find_turning_point(array, start, mid - 1)
    else:
        return find_turning_point(array, mid + 1, end)
