from lib.greet import *

def test_greet_returns_hello_sanam():
    result = greet('sanam')
    assert result=='Hello, sanam!'

    