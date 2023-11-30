#!/bin/python3
# fuctuion to find peak in a unsorted list
def find_peak(list_of_integers):
    if not list_of_integers:
        return None

    length = len(list_of_integers)
    mid = int(length / 2)

    # check 3 values.
    if mid + 1 >= length and mid - 1 < 0:
        return list_of_integers[mid]
    elif mid - 1 < 0:
        if list_of_integers[mid] > list_of_integers[mid + 1]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid + 1]
    elif mid + 1 >= length:
        if list_of_integers[mid] > list_of_integers[mid - 1]:
            return list_of_integers[mid]
        else:
            return list_of_integers[mid - 1]

    if list_of_integers[mid - 1] < list_of_integers[mid] > list_of_integers[mid + 1]:
        return list_of_integers[mid]

    if list_of_integers[mid + 1] > list_of_integers[mid - 1]:
        return find_peak(list_of_integers[mid:])

    return find_peak(list_of_integers[:mid])
