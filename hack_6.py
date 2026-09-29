"""
input: a = 3, b = 3, c = 4
- "invalido"   si no puede existir
- "equilatero" si los tres lados son iguales
- "isosceles"  si exactamente dos lados son iguales
- "escaleno"   si los tres lados son diferentes
output => "isosceles"
"""


def fn_hack_6():
    a = 3
    b = 3
    c = 4
    result = ""
    if a == b and a == c:
        result = "equilatero"
    elif a == b or a == c or b == c:
        result = "isosceles"
    elif a != b and a != c and b!= c:
        result = "escaleno"
    else:
        result = "invalido"
    return result
