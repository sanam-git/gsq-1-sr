import pytest
from lib.password_checker import *

def test_initial_state():
    pwd=PasswordChecker()
    assert pwd.check('asdfghjk') == True

def test_for_short_password():
    pwd=PasswordChecker()
    with pytest.raises(Exception) as err:
        pwd.check('asdf')
    error_message = str(err.value)
    assert error_message == 'Invalid password, must be 8+ characters.'
