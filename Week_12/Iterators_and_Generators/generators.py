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



def chapter_writer(chapter_lenght):
    chapter = []
    words = word_generator(chapter_lenght)
    for word in words:
        chapter.append(word)
    yield chapter




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
