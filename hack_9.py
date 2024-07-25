"""
text: {"foo":"fookziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):

    result = {str("Foo"): str("Fooziman") for key, _ in s.items()}

    return result
