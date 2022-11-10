from lib.string_builder import *

def test_addition_of_choco_and_late():
    strng=StringBuilder()
    strng.add('choco')
    strng.add('late')
    assert strng.output() == 'chocolate'
    assert strng.size() == 9