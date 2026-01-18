import random

from common import one_more


def get_wrong_guess_message(guessed: int, secret: int) -> str:
    adv = 'меньше' if guessed < secret else 'больше'

    return f'Ваше число {adv} загаданного, попробуйте ещё разок ^_^\n'


def is_valid_num(num: str, upper_limit=float('inf')) -> int:
    while not num.isdigit() or 1 > int(num) or int(num) > upper_limit:
        num = input(f'Введите число от 1 до {upper_limit}!\n')

    return int(num)


def game() -> None:
    upper_limit = is_valid_num(input('От 1 до какого числа ты хочешь сыграть в числовую угадайку?\n'))
    secret = random.randint(1, upper_limit)
    guess = input(f'Попробуй угадать загаданное целое число от 1 до {upper_limit}!\n')
    guess_cnt = 1

    while (guess := is_valid_num(guess, upper_limit)) and guess != secret:
        guess = input(get_wrong_guess_message(guess, secret))
        guess_cnt += 1

    print(f'Вы угадали, поздравляем! Количество попыток: {guess_cnt}.')
    print('Спасибо, что играли в числовую угадайку! Ещё увидимся ;)')


def main():
    print('Добро пожаловать в числовую угадайку!')

    one_more_game = 'да'
    while one_more_game.lower() == 'да':
        game()
        one_more_game = one_more()

    print('Приятно было с тобой поиграть! Заходи ещё, когда захочешь поиграть! :D')


if __name__ == '__main__':
    main()
