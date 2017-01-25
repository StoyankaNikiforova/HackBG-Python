import sys, tty, termios


def get_file(folder):
    import os
    for f in os.listdir(folder):
        if f.endswith(".txt"):
            yield f


def word_generator(chapter_lenght):
    words = ' '
    for i in range(chapter_lenght):
        word = ''
        for a in range(randint(1, 30)):
            char = chr(randint(33, 126))
            word += char
        words += ' {}'.format(word)
    yield words


def chapter_generator(folder):
    import re
    for i in get_file(folder):
        ffile = i

        with open(folder+"/"+ffile, 'r') as f:
            read_data = f.read()
            chaprers = re.split('#', read_data)
            for ch in chaprers:
                yield ch


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def book_reader():
    ss = chapter_generator("Book")
    for i in ss:
        print("Press Space to get chapter...")
        key = getch()
        print(key)
        if key == ' ':
            print(i)


def main():

    book_reader()





if __name__ == '__main__':
    main()
