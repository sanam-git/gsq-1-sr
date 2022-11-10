from lib.gratitudes import *

def test_initial_state():
    g=Gratitudes()
    assert g.gratitudes == []
    assert g.format() == 'Be grateful for: '

def test_add_two_elements():
    g=Gratitudes()
    g.add('blue skies')
    g.add('good friends')
    assert g.format() == 'Be grateful for: blue skies, good friends'