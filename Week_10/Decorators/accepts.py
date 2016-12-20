def accepts(*types):
    def check_func(func):
        def cheker(*args):
            for(a, t) in zip(args, types):
                assert isinstance(a, t), "TypeError: Argument {} of {} is not {}!".format(a, func.__name__,t)
            return func(*args)
        return cheker
    return check_func


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))
    return True


def main():
    print(say_hello(4))
    print(say_hello("Hacker"))
    deposit("RadoRado", 10)


if __name__ == '__main__':
    main()
