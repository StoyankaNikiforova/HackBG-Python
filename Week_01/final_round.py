import re


def is_number_balanced(number):
    n = str(number)
    if len(n) == 1:
        return True
    left_sum = 0
    for index in range(len(n)//2):
        left_sum += int(n[index])
    right_sum = 0
    beg = len(n)//2
    if len(n) % 2 != 0:
        beg = (len(n)//2)+1
    for index in range(beg, len(n)):
        right_sum += int(n[index])
    if right_sum == left_sum:
        return True
    else:
        return False
print(is_number_balanced(121))


def increasing_or_decreasing(seq):
    false = False
    down = False
    up = False

    for i in range(len(seq)-1):
        if seq[i] > seq[i+1]:
            down = True
        if seq[i] < seq[i+1]:
            up = True
        if seq[i] == seq[i+1]:
            return False
    if down and up:
        return false
    if down and not up:
        return "Down!"
    else:
        return "Up!"
# print(increasing_or_decreasing([9, 8, 7, 6]))

#palindromes
def is_palidrome(number):
    n = str(number)
    num_lenght = len(str(n))
    middle = num_lenght//2
    is_pal = True
    left_part = []
    right_part = []
    for i in range(middle):
        left_part.append(n[i])
    end = middle
    if num_lenght % 2 == 0:
        end = middle-1
    for j in range(num_lenght-1, end, -1):
        right_part.append(n[j])
    if left_part != right_part:
        is_pal = False
    return is_pal
# print(is_palidrome(242))


def get_largest_palindrome(n):
    all_palidromes_in_range = []
    for i in range(1, int(n)-1):
        if is_palidrome(i):
            all_palidromes_in_range.append(i)
    return all_palidromes_in_range[len(all_palidromes_in_range)-1]

# print(get_largest_palindrome(994687))


def sum_of_numbers(st):
    numbers = re.split("\D+", st)
    summ = 0
    if numbers[0] != '':
        for num in numbers:
            summ += int(num)
    return summ
# print(sum_of_numbers("abc"))


def birthday_ranges(birthdays, ranges):
    result = []
    for rangge in ranges:
        temp_count = 0
        for i in range(rangge[0], rangge[1]+1):
            if i in birthdays:
                temp_count = temp_count + birthdays.count(i)
        result.append(temp_count)
    return result
# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))


def numbers_to_message(pressed_sequence):
    pressed_sequence.append(0)
    # create dekoded dict
    decoder = {'0': " ", '1': "", '-1': ""}
    index = 97
    for i in range(2, 10):
        if i == 9 or i == 7:
            end = 5
        else:
            end = 4
        key = ""
        for x in range(1, end):
            key += str(i)
            decoder[key] = chr(index)
            index += 1
    # full key sequence
    keys_seq = []
    temp_list = []
    temp_list.append(str(pressed_sequence[0]))
    for i in range(1, len(pressed_sequence)):
        if pressed_sequence[i] != pressed_sequence[i-1] or pressed_sequence[i] == len(pressed_sequence):
            # check are we have element over
            if temp_list[0] == "7" or temp_list[0] == '9':
                koef = len(temp_list) % 4
            else:
                koef = len(temp_list) % 3
            temp_list = temp_list[-koef:]
            keys_seq.append(temp_list)
            temp_list = [str(pressed_sequence[i])]

        else:
            temp_list.append(str(pressed_sequence[i]))
    # decode sequence
    decoded_string = ''
    is_upper = False
    for x in range(len(keys_seq)):
        letter_key = ''.join(keys_seq[x])
        letter = decoder[''.join(keys_seq[x])]
        if is_upper:
            decoded_string += str.upper(letter)
            is_upper = False
        else:
            decoded_string += letter
        if letter_key == '1':
            is_upper = True
    return decoded_string
# print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
# print(numbers_to_message([2, 2, 2, 2]))
# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    message += '0'
    # create dekoded dict
    coder = {' ': 0, '0': -1}
    index = 97
    for i in range(2, 10):
        if i == 9 or i == 7:
            end = 5
        else:
            end = 4
        key = ""
        for x in range(1, end):
            key += str(i)
            coder[chr(index)] = key
            index += 1
    # full key sequence
    decode_seq = []
    for i in range(len(message)-1):
        current_code = [int(x) for x in str(coder[str.lower(message[i])])]
        if ord(message[i]) < 97 and ord(message[i]) > 65:
            decode_seq.append('1')
            decode_seq.append(current_code)
        elif abs(ord(message[i]) - ord(message[i+1])) <= 2:
            decode_seq.append(current_code)
            decode_seq.append('-1')
        else:
            decode_seq.append(current_code)
    result = [int(j) for i in decode_seq for j in i if j != '-']
    final = []
    for j in range(len(result)):
        if (result[j] == 1) and ((result[j - 1]) == (result[j + 1])):
            result[j] = -1
        final.append(result[j])
    return final

# print(message_to_numbers("abc"))
