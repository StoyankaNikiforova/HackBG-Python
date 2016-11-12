def sum_of_digits(number):
    n = int(abs(number))
    sum = 0
    while n > 0:
        digit = n % 10
        sum = sum + digit
        n = n//10
    return sum


# Create list with the digits of a number
def to_digits(number):
    digits_colection = []
    positiveNum = int(abs(number))
    while positiveNum > 0:
        digit = positiveNum % 10
        digits_colection.insert(0, digit)
        positiveNum = positiveNum//10
    return digits_colection


# Create number from array
def to_number(digits):
    number = ""
    for digit in digits:
        number = number + str(digit)
    return int(number)


# Count the vowels in a string
def count_vowels(string):
    count_vowels = 0
    english_vowels = ['a', 'e', 'i', 'y', 'u', 'o']
    for char in string:
        if str.lower(char) in english_vowels:
            count_vowels = count_vowels + 1
    return count_vowels


# Count the consonants in a string
def count_consonants(string):
    count_consonants = 0
    english_vowels = ['a', 'e', 'i', 'y', 'u', 'o']
    for char in str.lower(string):
        number_of_char = ord(char)
        if char not in english_vowels and number_of_char > 64 and number_of_char < 91 or char  not in english_vowels and number_of_char > 96 and number_of_char < 123:
            count_consonants = count_consonants + 1
    return count_consonants


# Check if a given number is prime
def prime_number(number):
    if number < 1:
        return False
    for n in range(2, (number)-1):
        if number % n == 0:
            return False
    return True


def factorial(number):
    n = int(number)
    if n == 1:
        return 1
    else:
        return n * fact_digits(n - 1)


# Sum of the factorials of the digits in the number
def fact_digits(number):
    digits = to_digits(number)
    result = 0
    for value in digits:
        result += factorial(value)
    return result



# fibonacci sequince
def fibonacci(number):
    fibonacci_numbers = [1]
    if number > 1:
        fibonacci_numbers.append(1)
        for index in range(2, number):
            fibonacci_numbers.append(fibonacci_numbers[index-1] + fibonacci_numbers[index-2])
    return fibonacci_numbers


def fib_nimber(n):
    number = int(abs(n))
    result = [str(x) for x in fibonacci(number)]
    return ''.join(result)


# Check if a given string is palindrome
def palindrome(string):
    input_str = str(string)
    is_palidrome = False
    str_len = len(input_str)
    first_half_str = input_str[0:str_len//2]
    second_half_str_reverse = (input_str[:str_len//2:-1])
    if first_half_str == second_half_str_reverse:
        is_palidrome = True
    return is_palidrome


# Dictionary with all characters from a string
def char_histogram(string):
    dict_all_chars = {}
    for charr in string:
        if charr in dict_all_chars:
            dict_all_chars[charr] = dict_all_chars[charr] + 1
        else:
            dict_all_chars.update({charr: 1})
    return dict_all_chars


def main():
    print(sum_of_digits(123))
    print(sum_of_digits(1325132435356))
    print(sum_of_digits(6))
    print(sum_of_digits(-10))
    print(to_digits(123))
    print(to_digits(9999))
    print(to_digits(123023))
    print(to_number([1, 2, 3]))
    print(to_number([9, 9, 9, 9, 9]))
    print(to_number([1, 2, 3, 0, 2, 3]))
    print(to_number([21, 2, 33]))
    print(count_vowels("Python"))
    print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_vowels("Theistareykjarbunga"))
    print(count_vowels("grrrrgh!"))
    print(count_vowels("A nice day to code!"))
    print(count_consonants("Python"))
    print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
    print(count_consonants("Theistareykjarbunga"))
    print(count_consonants("grrrrgh!"))
    print(count_consonants("A nice day to code!"))
    print(prime_number(6))
    print(prime_number(7))
    print(prime_number(8))
    print(fact_digits(111))
    print(fact_digits(145))
    print(fact_digits(999))
    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(3))
    print(fibonacci(10))
    print(fib_nimber(3))
    print(fib_nimber(10))
    print(palindrome(121))
    print(palindrome("kapak"))
    print(palindrome("baba"))
    print(char_histogram("Python!"))
    print(char_histogram("AAAAaaa!!!"))


if __name__ == '__main__':
    main()
