def one_more() -> str:
    answer = ''
    while answer.lower() not in {'да', 'нет'}:
        answer = input('Хотите сыграть ещё раз? Напишите "Да" или "Нет" без кавычек. Например: Да.\n')

    return answer
