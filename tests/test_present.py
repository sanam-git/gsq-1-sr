import pytest
from lib.present import *

def test_initial_state_returns_none():
    p=Present()
    assert p.contents == None


def test_wraps_and_unwraps_contents():
    p=Present()
    p.wrap('lawnmower')
    assert p.unwrap() == 'lawnmower'

def test_wrap_on_already_wrapped():
    p=Present()
    p.wrap('lawnmower')
    with pytest.raises(Exception) as err:
        p.wrap('spade') 
    error_message = str(err.value)
    assert error_message == "A contents has already been wrapped."


def test_cannot_unwrap():
    p=Present()
    with pytest.raises(Exception) as err:
        p.unwrap()
    error_message = str(err.value)
    assert error_message == 'No contents have been wrapped.'