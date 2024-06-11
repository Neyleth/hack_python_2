from hack_1 import fn_hack_1
from hack_2 import fn_hack_2
from hack_3 import fn_hack_3
from hack_4 import fn_hack_4
from hack_5 import fn_hack_5
from hack_6 import fn_hack_6
from hack_7 import fn_hack_7
from hack_8 import fn_hack_8
from hack_9 import fn_hack_9
from hack_10 import fn_hack_10
#
import pytest



def test_hack_1():
    assert fn_hack_1("fooziman") == "fOozIman"
    assert fn_hack_1("qux") == "qUx"
    assert fn_hack_1("eq") == "eq"


def test_hack_2():
    assert fn_hack_2("fooziman") == "fzmn"
    assert fn_hack_2("barziman") == "brzmn"
    assert fn_hack_2("qux") == "qx"


def test_hack_3():
    assert fn_hack_3("fooziman") == "F00z¡m@N"
    assert fn_hack_3("barziman") == "B@rz¡m@N"
    assert fn_hack_3("3q") == "3Q"
    assert fn_hack_3("qu") == "Qv"
    assert fn_hack_3("qux") == "QvX"


def test_hack_4():
    assert fn_hack_4("fooziman") == "oozima"
    assert fn_hack_4("barziman") == "arzima"
    assert fn_hack_4("qux") == "qux"


def test_hack_5():
    assert fn_hack_5("fooziman") == "fo-zi-ma-"
    assert fn_hack_5("barziman") == "ba-zi-an"
    assert fn_hack_5("qu-") == "qu-"
    assert fn_hack_5("eq") == "eq"


def test_hack_6():
    assert fn_hack_6(["a","b","c","d","e"]) == ["1","-","3","-","5"]
    assert fn_hack_6([]) == ["0"]


def test_hack_7():
    assert fn_hack_7(["a","b","c","d","e"]) == ["1",2,"3",4,"5"]
    assert fn_hack_7([0]) == [0]


def test_hack_8():
    assert fn_hack_8(["a","b","c","d","e"]) == ["e-5","d-4","c-3","b-2","a-1"]
    assert fn_hack_8(["a","b","c"]) == ["c-3","b-2","a-1"]
    assert fn_hack_8(["a","b","c","d"]) == ["4","3","2","1"]
    assert fn_hack_8(["a","b"]) == ["2","1"]


def test_hack_9():
    assert fn_hack_9({"foo":"fookziman","bar":"barziman"}) == {"Foo":"Fooziman"}


def test_hack_10():
    assert fn_hack_10([{"a":"b"},{"c":"d"},{"e":"f"}]) == [{"1":"2"},{"3":"4"},{"5":"6"}]


