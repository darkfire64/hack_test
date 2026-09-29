"""
input: n = 5
output => [5, 4, 3, 2, 1, 0]
"""


def fn_hack_8():
    n = 5
    result = []
    for i in range(5, -1, -1):
        result.append(i)
    return result
