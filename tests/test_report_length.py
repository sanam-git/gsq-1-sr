from lib.report_length import *

def test_five_char_string():
    #test if the string 'apple' is evaluated as 5 characters long
    result = report_length('apple')
    assert result == 'This string was 5 characters long.'

def test_nine_char_string():
    #test if the string 'apple pie' is evaluated as 9 characters long
    result = report_length('apple pie')
    assert result == 'This string was 9 characters long.'

def test_really_long_string():
    #test if the string 'supercalifragilisticexpialidocious!' is evaluated as 35 characters long
    result = report_length('supercalifragilisticexpialidocious!')
    assert result == 'This string was 35 characters long.'

def test_integer_as_string():
    #test if '42435672' is evaluated as 8 characters long
    result = report_length('42435672')
    assert result == 'This string was 8 characters long.' 