from random import randint
import sys, tty, termios


def chain(iterable_one, iterable_two):
    for i in iterable_one:
        yield i

    for i in iterable_two:
        yield i


def compress(iterable, mask):
    for (a, b) in zip(iterable, mask):
        if b:
            yield a


def cycle(iterable):
    for i in iterable:
        yield i


def get_file(folder):
    import os
    for f in os.listdir(folder):
        if f.endswith(".txt"):
            yield f


def chapter_generator(folder):
    import re
    for i in get_file(folder):
        ffile = i

        with open(folder+"/"+ffile, 'r') as f:
            read_data = f.read()
            chaprers = re.split('#', read_data)
            for ch in chaprers:
                yield ch


def word_generator(chapter_lenght):
    words = ' '
    for i in range(chapter_lenght):
        word = ''
        for a in range(randint(1, 30)):
            char = chr(randint(33, 126))
            word += char
        words += ' {}'.format(word)
    yield words


def chapter_writer(chapter_lenght):
    chapter = []
    words = word_generator(chapter_lenght)
    for word in words:
        chapter.append(word)
    yield chapter


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


def book_generator(chapter_count=4, chapter_lenght=1500):
    book_text = ""
    for a in range(1, chapter_count+1):
        book_text += "\n\nCapter {}\n".format(a)
        chapters = chapter_writer(chapter_lenght)
        for chapter in chapters:
            book_text += "  {}".format(chapter)

    yield book_text


def main():
    print(list(chain(range(0, 4), range(4, 8))))
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))

    endless = cycle(range(0, 10))
    for item in endless:
        print(item)

    book_reader()

    book = book_generator(10, 20)
    for i in book:
        print(i)






if __name__ == '__main__':
    main()
