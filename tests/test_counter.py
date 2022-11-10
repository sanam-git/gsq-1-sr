from lib.counter import Counter

def test_count_to_seven():
    i=Counter()
    i.add(7)
    assert i.report() == 'Counted to 7 so far.'

def test_add_thrice():
    j=Counter()
    j.add(3)
    j.add(5)
    j.add(2)
    assert j.report() == 'Counted to 10 so far.' 

def test_add_negative_number():
    n=Counter()
    n.add(-5)
    assert n.report() == 'Counted to -5 so far.' 