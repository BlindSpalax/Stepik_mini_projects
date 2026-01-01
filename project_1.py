import random


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


def game() -> None:
    print('Добро пожаловать в числовую угадайку!')

    upper_limit = int(input('От 1 до какого числа ты хочешь сыграть в числовую угадайку?\n'))
    upper_limit = is_valid_right_side(upper_limit)

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
    one_more_game = 'да'
    while one_more_game.lower() == 'да':
        game()
        one_more_game = one_more()

    print('Приятно было с тобой поиграть! Заходи ещё, когда захочешь поиграть! :D')


if __name__ == '__main__':
    main()
