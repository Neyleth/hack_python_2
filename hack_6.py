"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""


def fn_hack_6(input_list):
    list_salida = []
    for item, _ in enumerate(input_list, 1):
        if item % 2 == 1:
            list_salida.append(str(item))
        else:
            list_salida.append("-")
    if not input_list:
        list_salida.append("0")
    return list_salida
