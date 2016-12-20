from functools import wraps


def encrypt(num):
    def encrypt_func(func):
        @wraps(func)
        def crypter():
            cipher_text = ""
            for ch in func():
                if ch.isalpha():
                    new_letter_ascii_code = ord(ch) + num
                    if new_letter_ascii_code > ord('z'):
                        new_letter_ascii_code -= 26
                    final_letter = chr(new_letter_ascii_code)
                    cipher_text += final_letter
                if ch == ' ':
                    cipher_text += " "
            return cipher_text
        return crypter
    return encrypt_func


@encrypt(2)
def get_low():
    return "Get get get low"


def main():
    print(get_low())

if __name__ == '__main__':
    main()
