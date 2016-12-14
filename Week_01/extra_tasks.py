import re


def is_anagram(input1, input2):
    input = str.lower(input1) + str.lower(input2)
    char_colection = {}
    for char in input:
        if char in char_colection:
            char_colection[char] += 1
        else:
            char_colection[char] = 1
    is_anagram = True
    for char in char_colection:
        if char_colection[char] % 2:
            is_anagram = False
    return is_anagram

print(is_anagram("TOP_CODER", "COT_PRODE"))
#

def gas_stations(distance, tank_size, stations):
    res = [0]
    stations.append(distance)

    for i in range(len(stations) - 1):
        diff = stations[i+1] - stations[i]
        size = tank_size - (stations[i] - res[-1])
        if size < diff:
            res.append(stations[i])
            size = tank_size
    return res[1:]
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))


def reduce_file_path(path):
    result = path
    result = re.sub('\w+\/\.\.\/', '/', result)
    result = re.sub('\.\/', '', result)
    result = re.sub('\/{2,}', '/', result)
    result = re.sub('\.', '/', result)
    if len(result) > 1 and result[len(result)-1] == '/':
        result = result[: -1]
    return result


# goldbach(n)
def is_prime(x):
    if x < 2:
        return False
    for n in range(2, (x)-1):
        if x % n == 0:
            return False
    return True


def prime_numbers_in_range(start, end):
        primes = []
        str
        for x in range(start, end):
            if is_prime(x):
                primes.append(x)
        return primes


def goldbach(n):
    primes = prime_numbers_in_range(0, n//2+1)
    sum_tuples = []
    for prime in primes:
        diff = n-prime
        if is_prime(diff):
            current_tuple = (prime, diff)
            sum_tuples.append(current_tuple)
    return sum_tuples
print(goldbach(100))

def is_credit_card_valid(number):
    reversed_num = "".join(reversed(str(number)))
    lenght = len(reversed_num)
    summ = 0
    is_valid = False
    for i in range(0, lenght, 2):
        summ = summ + int((reversed_num)[i])
    for i in range(1, lenght, 2):
        transform_num = int(reversed_num[i]) * 2
        summ = summ + (transform_num // 10) + (transform_num % 10)
    if summ % 10 == 0 and lenght % 2 != 0:
        is_valid = True
    return is_valid

print(is_credit_card_valid(79927398713))
