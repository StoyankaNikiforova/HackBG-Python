from fraction_class import Fraction


def main():
    print(Fraction(2, 4))
    a = Fraction(1, 2)
    b = Fraction(2, 4)

    # print(a == b) # True

    print(a + b)# 1
    print(a - b)# 0
    # print(a * b) # 1 / 4


if __name__ == '__main__':
    main()
