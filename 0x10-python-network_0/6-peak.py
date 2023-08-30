#!/usr/bin/python3
"""that finds a peak in a list of unsorted integers"""


def find_peak(nums):
    if not nums:
        return None
    start = 0
    end = len(nums) - 1

    while start < end:
        mid = (start + end) // 2

        if nums[mid] > nums[mid + 1] and nums[mid] > nums[mid - 1]:
            return nums[mid]
        if nums[mid] < nums[mid + 1]:
            start = mid + 1
        else:
            end = mid - 1

    if start == end:
        return nums[end]

    return 0
