"""
generic script

text: "fooziman" output => "fOozIman" 
text: "qux" output => "qUx" 
text: "eq" output => "eq" 
"""


def fn_hack_1(s):
    result = s
    _ls = []

    txt_ls = [result[i:i+3] for i in range(0, len(result), 3)]

    for txt in txt_ls:
        if len(txt) % 2 != 0:
            content = f"{txt[0]}{txt[1].upper()}{txt[2]}"
            _ls.append(content)
        else:
            _ls.append(txt)
    result = "".join(_ls)
    return result
