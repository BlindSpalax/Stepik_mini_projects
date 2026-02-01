import random

DIGITS = set('0123456789')
LOWERCASE_LETTERS = set('abcdefghijklmnopqrstuvwxyz')
UPPERCASE_LETTERS = set('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
PUNCTUATION = set('!#$%&*+-=?@^_')
RESTRICT = set('il1Lo0O')
WANT = 'Хотите ли Вы, чтобы в пароле были'
YES_NO = 'Ответьте, пожалуйста, "Да" или "Нет".'


def is_number() -> int:
    num = input('Какая длина паролей требуется? (Все пароли будут одной длины).\n')
    while not num.isdigit() or int(num) < 1:
        num = input('Длина пароля должна быть числом и не может быть меньше 1!\n')

    return int(num)


def correct_input() -> tuple:
    include_digits = input(f'{WANT} цифры (от 0 до 9)?\n{YES_NO}\n').lower()
    while include_digits not in {'да', 'нет'}:
        include_digits = input(f'{YES_NO}\n').lower()

    include_uppercase = input(f'{WANT} прописные буквы (ABC...XYZ)?\n{YES_NO}\n').lower()
    while include_uppercase not in {'да', 'нет'}:
        include_uppercase = input(f'{YES_NO}\n').lower()

    include_lowercase = input(f'{WANT} строчные буквы (abc...xyz)?\n{YES_NO}\n').lower()
    while include_lowercase not in {'да', 'нет'}:
        include_lowercase = input(f'{YES_NO}\n').lower()

    include_punctuation = input(f'{WANT} небуквенные символы (!#$%&*+-=?@^_)?\n{YES_NO}\n').lower()
    while include_punctuation not in {'да', 'нет'}:
        include_punctuation = input(f'{YES_NO}\n').lower()

    exclude_restrict = input(f'Хотите ли Вы исключить неоднозначные символы (il1Lo0O)?\n{YES_NO}\n').lower()
    while exclude_restrict not in {'да', 'нет'}:
        exclude_restrict = input(f'{YES_NO}\n').lower()

    return include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_restrict


def chars_allowed(chars: set) -> str:
    include_digits, include_uppercase, include_lowercase, include_punctuation, exclude_restrict = correct_input()

    if include_digits == 'да':
        chars.update(DIGITS)
    if include_uppercase == 'да':
        chars.update(UPPERCASE_LETTERS)
    if include_lowercase == 'да':
        chars.update(LOWERCASE_LETTERS)
    if include_punctuation == 'да':
        chars.update(PUNCTUATION)
    if exclude_restrict == 'да':
        chars.difference_update(RESTRICT)

    return ''.join(chars)


def generate_password(length: int, chars: str) -> str:
    return ''.join(random.sample(chars, length))


def main():
    how_many_passwords = int(input('Сколько паролей необходимо сгенерировать? Введите целое число.\n'))
    allowed_chars = set()
    length_of_password = is_number()

    while len(allowed_chars) < length_of_password:
        allowed_chars = chars_allowed(allowed_chars)

        while len(allowed_chars) < length_of_password:
            print('Приносим извинения, однако Вы выбрали слишком мало уникальных символов для такой длины пароля :(')
            print(f'Попробуйте укоротить Ваш пароль. Например, введите число равное или меньше {len(allowed_chars)}.')
            length_of_password = is_number()

    for _ in range(how_many_passwords):
        print(generate_password(length_of_password, allowed_chars))


if __name__ == '__main__':
    main()
