"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""


def fn_hack_10(s):
    result = s
    lista = []
    contador = 1

    for _ in result:
        new_dict = {}
        new_dict[str(contador)] = str(contador + 1)
        contador += 2

        lista.append(new_dict)

    return lista
