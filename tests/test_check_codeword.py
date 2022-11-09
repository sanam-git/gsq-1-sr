from lib.check_codeword import * 

def test_correctamundo():
    #test if the correct prompt is returned when the correct codeword is used as an argument
    result = check_codeword('horse')
    assert result == 'Correct! Come in.'

def test_check_codeword_close():
    #test if the correct prompt is returned when a value which shares the same initial and final characters as the codeword is used as an argument
    result = check_codeword('hope')
    assert result=='Close, but nope.'

def test_check_codeword_wrong():
    #test if the correct prompt is returned when an incorrect codeword is used as an argument
    result = check_codeword('soap')
    assert result == 'WRONG!'

