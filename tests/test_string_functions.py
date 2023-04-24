from functions.string_functions import reverse_string, capitalize_string

def test_reverse_string():
    assert reverse_string('hello') == 'olleh'
    assert reverse_string('12345') == '54321'
    assert reverse_string('') == ''

def test_capitalize_string():
    assert capitalize_string('hello') == 'Hello'
    assert capitalize_string('12345') == '12345'
    assert capitalize_string('') == ''