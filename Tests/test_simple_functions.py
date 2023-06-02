import pytest
from App import simple_functions
from App.simple_functions import NotStringException


@pytest.mark.parametrize('text, expected', [
    ('abc', 'cba'),
    ('kiwi', 'iwik'),
    ('apple', 'elppa'),
    ('', '')
])
def test_reverse_string_valid_input(text, expected):
    assert simple_functions.reverse_string(text) == expected, "Reverse string is not working!"


@pytest.mark.parametrize('text, ', [
    123,
    0.1,
    True
])
def test_reverse_string_invalid_input(text):
    with pytest.raises(TypeError):
        simple_functions.reverse_string(text)


@pytest.mark.parametrize('text, expected', [
    ('level', True),
    (2002, True),
    (1.1, True),
    (1.0, False),
    ('banana', False),
    ('', True),
    ('a', True),
    ('zz', True),
    ('Madam', True),
    ('Taco cat', True),
    ('!', True),
    ('Top spot', True)
])
def test_is_palindrome(text, expected):
    assert simple_functions.is_palindrome(text) == expected, "Palindrome is not working!"


@pytest.mark.parametrize('num, expected', [
    (3, 'Fizz'),
    (5, 'Buzz'),
    (15, 'FizzBuzz'),
    (2, 2),
    (0, 'FizzBuzz'),
    (-1, -1),
    (100, 'Buzz')
])
def test_fizz_buzz(num, expected):
    assert simple_functions.fizz_buzz(num) == expected, "Fizz Buzz is not working!"


@pytest.mark.parametrize('num, expected', [
    (2, True),
    (3, True),
    (11, True),
    (100, False),
    (-1, False),
    (-50, False),
    (0, False),
    (1, False)
])
def test_is_prime(num, expected):
    assert simple_functions.is_prime(num) == expected, "Is not working!"


@pytest.mark.parametrize('numbers, num, expected', [
    ([1, 5, 3], 3, [3, 15, 9]),
    ([2, 10, 50], 1, [2, 10, 50]),
    ([-8, 5, 32], 5, [-40, 25, 160]),
    ([-8, 5, 32], 0, [0, 0, 0]),
    ([0, 0, 0], 20, [0, 0, 0]),
    ([], 2, []),
    ([-1, 2, -3], -2, [2, -4, 6])
])
def test_multiply_list_elements(numbers, num, expected):
    assert simple_functions.multiply_list_elements(numbers, num) == expected, "Multiply list is not working!"


@pytest.mark.parametrize('a, b, expected', [
    (1, 5, 5),
    (-8, -10, -8),
    (5, 0, 5),
    (0, -4, 0),
    (1, 1, 1),
    (1, 0.99, 1),
    (2.99, 5.99, 5.99),
])
def test_get_max_between_numbers(a, b, expected):
    assert simple_functions.get_max_between_numbers(a,
                                                    b) == expected, "Get max number between 2 numbers is not working!"


@pytest.mark.parametrize('text, expected', [
    ('aab', 'b'),
    ('acb', 'acb'),
    ('accbcaba', ''),
    ('', ''),
    ('    ', ''),
    ('a', 'a'),
    ('a sdsa ', 'd'),
    ('Aa', 'Aa'),
    (' Hello there!', 'Hothr!'),
])
def test_get_unique_characters_valid(text, expected):
    assert simple_functions.get_unique_characters(text) == expected, "Get unique characters is not working!"


@pytest.mark.parametrize('text', [
    1,
    -6,
    0,
    108.8998,
    True,
    False
])
def test_get_unique_characters_invalid(text):
    with pytest.raises(NotStringException):
        simple_functions.get_unique_characters(text)
