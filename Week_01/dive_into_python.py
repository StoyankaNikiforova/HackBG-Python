import re
import collections
import sys


def count_substrings(haystack, needle):
    patt = re.compile(needle)
    result = patt.findall(haystack)
    return len(result)


def sum_matrix(m):
    result_sum = sum([sum(row)for row in m])
    return result_sum


def nan_expand(times):
    final_string = ""
    if times > 0:
        if times > 0:
            final_string = final_string + 'Not '
            for index in range(times -1):
                final_string = final_string + 'a Not '
        final_string += 'a NaN'
    return final_string


def prime_factorization(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    prime_fact = collections.Counter(factors)
    result = []
    for value in sorted(dict(prime_fact).keys()):
        tup = (value, dict(prime_fact)[value])
        result.append(tup)
    return result


def group(number_collection):
    list_elements = []
    temp_list = []
    temp_list.append(number_collection[0])
    index_begin = 1
    for index in range(index_begin, len(number_collection)):
        curent_number = number_collection[index]
        prev_number = number_collection[index-1]
        if curent_number == prev_number:
            temp_list.append(curent_number)
        else:
            index_begin = index+1
            list_elements.append(temp_list)
            temp_list = [curent_number]
    list_elements.append(temp_list)
    return list_elements


def max_consecutive(items):
    count_max = 1
    current_count = 1      #-sys.maxint
    for x in range(1, len(items)):
        if items[x] == items[x-1]:
            current_count = current_count + 1
        else:
            if current_count > count_max:
                count_max = current_count
                current_count = 0
    return count_max


# word counter
def find_all_occur_in_horizontal_lines(pattern, matrix, rows, colls):
    count = 0
    for i in range(rows):
        matcher = re.findall(pattern, "".join(matrix[i]))
        count += len(matcher)
    for i in range(rows):
        matcher = re.findall(pattern, ("".join(reversed(matrix[i]))))
        count += len(matcher)
    return count

def find_all_occur_in_vertical_lines(pattern, matrix, rows, colls):
    # generate line
    coll_lines = []
    for i in range(colls):
        temp_line = ""
        for j in range(rows):
            temp_line += matrix[j][i]
        coll_lines.append(temp_line)
    count = 0
    for i in range(colls):
        matcher = re.findall(pattern, coll_lines[i])
        count += len(matcher)
    for i in range(colls):
        matcher = re.findall(pattern, "".join(reversed(coll_lines[i])))
        count += len(matcher)
    return count

def find_all_occur_in_cross_lines(pattern, matrix, rows, colls):
    cross_lines = []
    c = 0
    for i in range(colls):
        temp_line = ""
        r = 0
        c = i
        for j in range(i, colls):
            temp_line += matrix[r][c]
            r += 1
            c += 1
        cross_lines.append(temp_line)
    c = 0
    for i in range(rows-1):
        temp_line = ""
        r = i+1
        c = 0
        for j in range(colls-i):
            temp_line += matrix[r][c]
            r += 1
            c += 1
        cross_lines.append(temp_line)
    count = 0
    for i in range(len(cross_lines)):
        matcher = re.findall(pattern, cross_lines[i])
        count += len(matcher)
    for i in range(len(cross_lines)):
        matcher = re.findall(pattern, "".join(reversed(cross_lines[i])))
        count += len(matcher)
    return count


def word_counter():
    word = input()
    matrix_dem = input().split()
    m_witdh = int(matrix_dem[1])
    m_hight = int(matrix_dem[0])
    # fill matrix
    matrix = [[0 for i in range(m_witdh)] for j in range(m_hight)]
    for i in range(m_hight):
        matrix[i] = list(input().split(' '))
    # find count of occurences
    count = 0
    pattern = word
    count += find_all_occur_in_horizontal_lines(pattern, matrix, m_hight, m_witdh)
    count += find_all_occur_in_vertical_lines(pattern, matrix, m_hight, m_witdh)
    count += find_all_occur_in_cross_lines(pattern, matrix, m_hight, m_witdh)
    return(count)
