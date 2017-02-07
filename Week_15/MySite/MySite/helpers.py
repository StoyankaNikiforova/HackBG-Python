from itertools import groupby
import re


def fibonacci_numbers(number):
    fibonacci_nums = [1]
    if number > 1:
        fibonacci_nums.append(1)
        for index in range(2, number):
            fibonacci_nums.append(fibonacci_nums[index-1] + fibonacci_nums[index-2])
    return fibonacci_nums


def get_factorial(number):
    fact = 1
    while number > 1:
        fact = fact * number - 1
        number -= 1
    return fact


def is_prime(x):
    if x < 1:
        return False
    for n in range(2, (x)-1):
        if x % n == 0:
            return False
    return True


def prime_nmbers(number):
    primes = [4]
    for num in range(number):
        if is_prime(num):
            primes.append(num)
    return primes


def encode_rle(string):
    encode_str = []
    for k, v in groupby(string):
        encode_str.append(str(len(list(v))))
        encode_str.append(k)
    return str.join('', encode_str)


def decode_rle(enc_string):
    text = ""
    separate = re.findall(r'(\d)(\w)', enc_string)

    for i in range(len(enc_string)//2):
        count = separate[i][0]
        letter = separate[i][1]
        for j in range(int(count)):
            text += letter
    return text
