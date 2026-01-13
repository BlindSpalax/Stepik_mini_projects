import random


def chars_allowed(chars):
    digits = '0123456789'
    lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'
    uppercase_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    punctuation = '!#$%&*+-=?@^_'
    restrict = 'il1Lo0O'

    include_digits = input('Хотите ли Вы, чтобы в пароле были цифры (от 0 до 9)? Ответьте "Да" или "Нет".\n').lower()
    include_uppercase = input(
        'Хотите ли Вы, чтобы в пароле были прописные буквы (ABC...)? Ответьте "Да" или "Нет".\n').lower()
    include_lowercase = input(
        'Хотите ли Вы, чтобы в пароле были строчные буквы (abc...)? Ответьте "Да" или "Нет".\n').lower()
    include_punctuation = input(
        'Хотите ли Вы, чтобы в пароле были небуквенные символы (!#$...)?  Ответьте "Да" или "Нет".\n').lower()
    exlude_restrict = input(
        'Хотите ли Вы исключить неоднозначные символы (il1Lo0O)? Ответьте "Да" или "Нет".\n').lower()

    if include_digits == 'да':
        chars += digits
    if include_uppercase == 'да':
        chars += uppercase_letters
    if include_lowercase == 'да':
        chars += lowercase_letters
    if include_punctuation == 'да':
        chars += punctuation
    if exlude_restrict == 'да':
        for el in restrict:
            if el in chars:
                chars = chars.replace(el, '')

    return chars


def generate_password(length, chars):
    return ''.join(random.sample(chars, length))


def main():
    how_many_passwords = int(input('Сколько паролей необходимо сгенерировать? Введите целое число.\n'))
    chars = ''
    length_of_password = 1

    while len(chars) < length_of_password:
        length_of_password = int(input('Какая длина паролей требуется? (Все пароли будут одной длины).\n'))
        chars = chars_allowed(chars)
        if len(chars) < length_of_password:
            print('Приносим извинения, однако Вы выбрали слишком мало уникальных символов для такой длины пароля :(')
            print('Попробуйте выбрать больше символов или укоротить Ваш пароль.')

    for _ in range(how_many_passwords):
        print(generate_password(length_of_password, chars))


if __name__ == '__main__':
    main()
