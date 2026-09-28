"""
input: a = 10, b = 3
output => (13, 7, 30, 1, 3)   # suma, resta, multiplicación, módulo, división entera
"""


def fn_hack_3():
    a = 10
    b = 3
    result = (0, 0, 0, 0, 0)
    result = (a + b, a - b, a * b, b // b, a // b)
    return result
