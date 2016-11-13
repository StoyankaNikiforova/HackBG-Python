from collections import OrderedDict


def is_prime(x):
    if x < 1:
        return False
    for n in range(2, (x)-1):
        if x % n == 0:
            return False
    return True


def simplify_fraction(fraction):
    nominator = fraction[0]
    denominator = fraction[1]
    if nominator == denominator:
        return (1)
    if nominator != denominator and (is_prime(nominator) and is_prime(denominator)):
        return fraction
    bigger_devisor = 2
    for i in range(2, denominator+1):
        if nominator % i == 0 and denominator % i == 0:
            if i > bigger_devisor:
                bigger_devisor = i
    return(nominator//bigger_devisor, denominator//bigger_devisor)


def sort_fractions(fractions):
    len_list = len(fractions)
    for value in fractions:
        for i in range(1, len_list):
            current = fractions[i][0]/fractions[i][1]
            prev = fractions[i - 1][0]/fractions[i - 1][1]
            if prev > current:
                buffer_fr = fractions[i]
                fractions[i] = fractions[i - 1]
                fractions[i - 1] = buffer_fr
    return fractions
