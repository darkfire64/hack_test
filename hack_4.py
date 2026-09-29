"""
input: numero = 8
output => True   # True si el número es par y está entre 1 y 10
"""


def fn_hack_4():
    numero = 8
    result = False
    if numero % 2 == 0 and numero >= 1 and numero <= 10:
        result = True
    return result
