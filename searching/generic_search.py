#!/usr/bin/env python3

## for decending sorted list of numbers.

test_cases = [
    {'input': {'nums': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 2, 'condition': 'l'}, 'output': 8},
    {'input': {'nums': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6, 'condition': 'r'},'output': 7}
]

def binary_search(lo, hi, check_condition):
    while lo <= hi:
        mid = (lo+hi)//2
        result = check_condition(mid)
        if result == 'found':
            return mid
        elif result == 'left':
            hi = mid-1
        elif result == 'right':
            lo = mid+1
    return -1

def check(nums, query, condition):

    def check_left(mid):

        if nums[mid] == query:
            if mid > 0 and nums[mid-1] == query:
                return 'left'
            else:
                return 'found'
        elif query > nums[mid]:
            return 'left'
        else:
            return 'right'

    def check_right(mid):

        if nums[mid] == query:
            if mid < len(nums)-1 and nums[mid+1] == query:
                return 'right'
            else:
                return 'found'
        elif query > nums[mid]:
            return 'left'
        else:
            return 'right'

    if condition == 'l':
        return binary_search(0, len(nums)-1, check_left)
    else:
        return binary_search(0, len(nums)-1, check_right)


for test in test_cases:
    
    result = check(**test['input'])
    if result == test['output']:
        print(True, result)
    else:
        print(False, result)
