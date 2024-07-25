"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""


def fn_hack_7(s):
    result = s
    lista = []

    for items in result:
        if items == "a":
            lista.append("1")
        elif items == "b":
            lista.append(2)
        elif items == "c":
            lista.append("3")
        elif items == "d":
            lista.append(4)
        elif items == "e":
            lista.append("5")

    if not lista:
        return [0]

    result = lista

    return result
