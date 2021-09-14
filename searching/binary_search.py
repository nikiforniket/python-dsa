#!/usr/bin/env python3

# for decending sorted list.

test_cases = [
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 7}, 'output': 3},
    {'input': {'cards': [13, 11, 10, 7, 4, 3, 1, 0], 'query': 1}, 'output': 6},
    {'input': {'cards': [4, 2, 1, -1], 'query': 4}, 'output': 0},
    {'input': {'cards': [3, -1, -9, -127], 'query': -127}, 'output': 3},
    {'input': {'cards': [6], 'query': 6}, 'output': 0},
    {'input': {'cards': [9, 7, 5, 2, -9], 'query': 4}, 'output': -1},
    {'input': {'cards': [], 'query': 7}, 'output': -1},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0], 'query': 3}, 'output': 7},
    {'input': {'cards': [8, 8, 6, 6, 6, 6, 6, 6, 3, 2, 2, 2, 0, 0, 0],'query': 6},'output': 2}
]

def check_function(cards, check, query):
    if cards[check] == query:
        if check-1 >=0  and cards[check -1] == query:
            return 'left'
        else:
            return 'found'
    elif cards[check] < query:
        return 'left'
    else:
        return 'right'
        
def binary_search(cards, query):
    lo, hi = 0, len(cards) - 1
    check = None
    while lo <= hi:
        check = (lo+hi)//2
        check_value = check_function(cards, check, query) 
        if check_value == 'found':
            return check
        elif check_value == 'left':
            hi = check - 1
        elif check_value == 'right':
            lo = check + 1
    return -1


for test_case in test_cases:
    result = binary_search(**test_case['input'])
    if result == test_case['output']:
        print(True, result)
    else:
        print(False, result)
