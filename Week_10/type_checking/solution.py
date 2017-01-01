import sys
import re

# def parser(inpt):


def is_valid_composition(inpt):
    functions = {}
    count_lines = len(inpt)-2
    for i in range(count_lines):
        line = str.replace('\n', '', inpt[i])
        func_props = re.findall('\w+', line)
        functions[func_props[0]] = [func_props[1], func_props[2]]

    composition = re.findall('\w+', inpt[count_lines+1])

    is_valid = 'True'

    inerr_f = composition.pop()
    while composition:
        outrer_f = composition.pop()
        out_inner = functions[inerr_f][1]
        in_outer = functions[outrer_f][0]
        if out_inner != in_outer:
            is_valid = 'False'

        inerr_f = outrer_f

    print(is_valid)


def main():
    inpt = list(sys.stdin)
    is_valid_composition(inpt)


if __name__ == '__main__':
    main()
