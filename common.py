def is_valid_upper_limit(upper_limit: str) -> int:
    try:
        if (upper_limit := int(upper_limit)) > 1:
            return upper_limit
    except ValueError:
        while (not upper_limit.isdigit()) or int(upper_limit) <= 1:
            upper_limit = input('Правая граница должна быть числом больше 1!\n')
        upper_limit = int(upper_limit)

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
