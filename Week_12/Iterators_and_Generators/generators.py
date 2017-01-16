from random import randint


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


def print_chapter(folder):
    import re
    for i in get_file(folder):
        ffile = i

        pattern = '\#[\w\d!;,?]*'

        with open(folder+"/"+ffile, 'r') as f:
            read_data = f.read()
            print(read_data)
            chaprers = re.split('#', read_data)
            for ch in chaprers:
                yield ch


def word_generator():
    word = ""
    for a in range(randint(5, 50)):
        char = chr(randint(32, 126))
        word += char
    yield word


def book_generator(chapter_count=4, chapter_lenght=1500):
    book_text = ""
    for a in range(chapter_count):
        book_text += "Capter {}\n".format(a)
        words = word_generator()

        for w in range(chapter_lenght):
            for word in words:
                book_text += " {}".format(word)

    return book_text


def main():
    print(list(chain(range(0, 4), range(4, 8))))
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))

    endless = cycle(range(0, 10))
    for item in endless:
        print(item)

    book = book_generator()
    for i in book:
        print(i)


    ss = print_chapter("Book")
    for i in ss:
        key = input("Press Space to get chapter...")
        if key == ' ':
            print(i)




if __name__ == '__main__':
    main()
