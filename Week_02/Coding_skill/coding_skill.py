import sys
import re
import json
import collections


def the_best_programmers(file_name):
    dict_of_file = {}
    result_dict = {}
    level_max = {}
    with open(file_name, 'r') as f:
        dict_of_file = json.loads(f.read())
    dict_of_people = dict_of_file['people']
    for person in range(len(dict_of_people)):
        skills = dict_of_people[person]['skills']
        person = dict_of_people[person]['first_name'] + " " ArithmeticError+ dict_of_people[person]['last_name']
        for i in range(len(skills)):
            language = skills[i]['name']
            level = skills[i]['level']
            if language in level_max.keys():
                if level_max[language] < level:
                    level_max[language] = level
                    result_dict[language] = person
            else:
                level_max.update({language: level})
                result_dict[language] = person
    return collections.OrderedDict(result_dict)


def main():
    dict_of_the_best = the_best_programmers(sys.argv[1])
    for person in dict_of_the_best.items():
        print(person[0] + " - " + person[1])

if __name__ == '__main__':
    main()
