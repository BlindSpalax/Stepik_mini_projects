def is_valid_right_side(upper_limit: int) -> int:
    while upper_limit < 1:
        upper_limit = int(input('Правая граница должна быть больше 1!\n'))

    return upper_limit


def is_valid(num: str, right_side: int) -> bool:
    if not num.isdigit():
        return False

    return 1 <= int(num) <= right_side


def get_wrong_guess_message(guessed: int, secret: int) -> str:
    adv = 'меньше' if guessed < secret else 'больше'

    return f'Ваше число {adv} загаданного, попробуйте ещё разок\n'


def one_more() -> str:
    answer = ''
    while answer.lower() not in {'да', 'нет'}:
        answer = input('Хотите сыграть ещё раз? Напишите "Да" или "Нет" без кавычек. Например: Да.\n')

    return answer
