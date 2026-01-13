import random

from common import one_more


def get_wrong_guess_message(guessed: int, secret: int) -> str:
    adv = 'меньше' if guessed < secret else 'больше'

    return f'Ваше число {adv} загаданного, попробуйте ещё разок\n'


def is_valid_guess(num: str, right_side: int) -> bool:
    if not num.isdigit():
        return False

    return 1 <= int(num) <= right_side


def is_valid_upper_limit(upper_limit: str) -> int:
    try:
        if (upper_limit := int(upper_limit)) > 1:
            return upper_limit
    except ValueError:
        while (not upper_limit.isdigit()) or int(upper_limit) <= 1:
            upper_limit = input('Правая граница должна быть числом больше 1!\n')
        upper_limit = int(upper_limit)

    return upper_limit


def game() -> None:
    upper_limit = input('От 1 до какого числа ты хочешь сыграть в числовую угадайку?\n')
    upper_limit = is_valid_upper_limit(upper_limit)

    secret = random.randint(1, upper_limit)
    guess = input(f'Попробуй угадать загаданное целое число от 1 до {upper_limit}!\n')
    guess_cnt = 1
    while True:
        if not is_valid_guess(guess, upper_limit):
            guess = input(f'Может всё-таки введём целое число от 1 до {upper_limit}? :D\n')
            guess_cnt += 1
            continue

        if (guess := int(guess)) != secret:
            guess = input(get_wrong_guess_message(guess, secret))
        else:
            print(f'Вы угадали, поздравляем! Количество попыток: {guess_cnt}.')
            print('Спасибо, что играли в числовую угадайку! Ещё увидимся ;)')
            break
        guess_cnt += 1


def main():
    print('Добро пожаловать в числовую угадайку!')

    one_more_game = 'да'
    while one_more_game.lower() == 'да':
        game()
        one_more_game = one_more()

    print('Приятно было с тобой поиграть! Заходи ещё, когда захочешь поиграть! :D')


if __name__ == '__main__':
    main()
