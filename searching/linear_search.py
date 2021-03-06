#!/usr/bin/env python3

# for decending sorted list of numbers.

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

heavy_test = {'input': {'cards': range(100000, 0, -1), 'query': 2}, 'output': 99998}

def locate_cards(cards, query):
    position = 0
    print(len(cards))
    while position < len(cards):
        if cards[position] == query:
            return position
        position += 1
    return -1

for test_case in test_cases:
    result = locate_cards(**test_case['input'])
    if result == test_case['output']:
        print(True, result)
