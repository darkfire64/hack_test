"""
input: nota = 85
- 90 a 100: "Excelente"
- 80 a 89:  "Notable"
- 60 a 79:  "Aprobado"
- 0 a 59:   "Reprobado"
output => "Notable"
"""


def fn_hack_5():
    nota = 85
    result = ""
    if nota >= 90 and nota <= 100:
        result = "Excelente"
        print (result)
    elif nota >= 80 and nota <= 89:
        result = "Notable"
        print (result)
    elif nota >= 60 and nota <= 79:
        result = "Aprobado"
        print (result)
    elif nota >= 0 and nota <= 59:
        result = "Reprobado"
        print (result)
    else:
        result = "Nota inválida"
        print (result)
    return result
