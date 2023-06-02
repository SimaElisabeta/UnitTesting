def reverse_string(text):
    return text[::-1]


def is_palindrome(text):
    # convert given parameter to string, then convert to lower and finally remove all space characters inside the text
    text = str(text).lower().replace(' ', '')
    return text == text[::-1]


def fizz_buzz(num):
    if (num % 5 == 0) and (num % 3 == 0):
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num


def is_prime(num):
    if num <= 1:
        return False

    for i in range(2, int(num / 2)):
        if num % i == 0:
            return False
    else:
        return True


def multiply_list_elements(numbers, number):
    return [number * n for n in numbers]


def get_max_between_numbers(a, b):
    return max(a, b)


class NotStringException(Exception):
    pass


def get_unique_characters(text):
    if not isinstance(text, str):
        raise NotStringException(f'{text} must be a string')

    # remove any space character
    text = text.replace(' ', '')

    result_text = ''
    for char in text:
        if text.count(char) == 1:
            result_text += char
    return result_text


if __name__ == '__main__':
    test = ' Hello there!'
    print(get_unique_characters(test))
