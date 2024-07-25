"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""

def fn_hack_3(s):
    result = s
    dictorio = {
        "a" : "@",
        "e" : "3",
        "i" : "¡",
        "o" : "0",
        "u" : "v",
        "f" : "F",
        "n" : "N",
        "q" : "Q",
        "x" : "X",
        "b" : "B",
        "z" : "z",
        "m" : "m",
        "r" : "r",
        "3" : "3"
}
    change = []
    for txt in result:
        change.append(dictorio.get(txt))

        result = "".join(change)
    return result
