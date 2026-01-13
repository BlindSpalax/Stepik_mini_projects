import random

from common import get_wrong_guess_message, is_valid, is_valid_upper_limit, one_more


def game() -> None:
    upper_limit = input('От 1 до какого числа ты хочешь сыграть в числовую угадайку?\n')
    upper_limit = is_valid_upper_limit(upper_limit)

    secret = random.randint(1, upper_limit)
    guess = input(f'Попробуй угадать загаданное целое число от 1 до {upper_limit}!\n')
    guess_cnt = 1
    while True:
        if not is_valid(guess, upper_limit):
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
