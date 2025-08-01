"""
Given a string, we need to reverse it using recursion
For example, input = "Zero To Mastery", output = "yretsaM oT oreZ"
"""

def iterativeReversed(string):
    alterString = ''
    # Este for es como contar desde el final
    for i in range(len(string)):
        alterString = alterString + string[len(string) - i - 1]
    return alterString
print(iterativeReversed("Zero To Mastery"))


def reversed(string):
    print(string)
    # caso base: cuando la cadena esta vacia, deja de llamar recursivamente
    if len(string) == 0:
        return string
    else:
        # toma la cadena  sin la priera letra (string[1:]) y la revierte, luego añade la priera letra al final
        return reversed(string[1:]) + string[0]

print(reversed("Zero To Mastery"))