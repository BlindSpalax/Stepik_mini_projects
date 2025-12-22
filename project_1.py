import random


def is_valid_right_side(right_side):
    while True:
        if right_side < 1:
            right_side = int(input('Правая граница должна быть больше 1!\n'))
            continue
        break
    return right_side


def is_valid(num, right_side):
    if not num.isdigit():
        return False
    num = int(num)
    return 1 <= num <= right_side


def one_more(answer):
    while not (answer == 'да' or answer == 'нет'):
        answer = input('Хотите сыграть ещё раз? Напишите "Да" или "Нет" без кавычек. Например: Да.\n').lower()
    return answer


def game():
    print('Добро пожаловать в числовую угадайку!')
    right_side = int(input('От 1 до какого числа ты хочешь сыграть в числовую угадайку?\n'))
    right_side = is_valid_right_side(right_side)
    guess_me = random.randint(1, right_side)
    guess = input(f'Попробуй угадать загаданное целое число от 1 до {right_side}!\n')
    count_guesses = 1

    while True:
        if not is_valid(guess, right_side):
            guess = input(f'Может всё-таки введём целое число от 1 до {right_side}? :D\n')
            count_guesses += 1
            continue
        guess = int(guess)
        if guess > guess_me:
            guess = input('Ваше число больше загаданного, попробуйте ещё разок\n')
            count_guesses += 1
        elif guess < guess_me:
            guess = input('Ваше число меньше загаданного, попробуйте ещё разок\n')
            count_guesses += 1
        else:
            print(f'Вы угадали, поздравляем! Количество попыток: {count_guesses}.')
            print('Спасибо, что играли в числовую угадайку! Ещё увидимся ;)')
            break


game()
one_more_game = one_more(input('Хотите сыграть ещё раз? Если да, то напишите "Да". Если нет, то "Нет".\n').lower())

while one_more_game == 'да':
    game()
    one_more_game = one_more(input('Хотите сыграть ещё раз? Если да, то напишите "Да". Если нет, то "Нет".\n').lower())

print('Приятно было с тобой поиграть! Заходи ещё, когда захочешь поиграть! :D')
