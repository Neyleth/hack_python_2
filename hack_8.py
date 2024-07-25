"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""


def fn_hack_8(s):
    list_salida = []

    for element, index in enumerate(s, 1):
        if len(s) % 2 !=  1:
            list_salida.append(str(element))
        else:
            list_salida.append(str(f"{index}-{element}"))

    return list_salida[::-1]