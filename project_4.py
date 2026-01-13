def is_valid_direction() -> str:
    direction = input('Вы хотите провести шифровку или дешифровку текста? Напишите "Шифр" или "Дешифр".\n').lower()
    while not direction in {'шифр', 'дешифр'}:
        direction = input('Проверьте написания слов "Шифр"/"Дешифр".\n').lower()

    return direction


def is_valid_step() -> int:
    step = input('Какой шаг в шифре Цезаря Вы хотите реализовать? Напишите любое целое положительное число.\n'
                 '(Нецелое будет округлено в сторону нуля)\n')
    while (not step.isdigit()) or int(step) < 0:
        step = input('Шаг должен быть любым целым неотрицательным числом! Например, "0", "1", "2",...\n'
                     '(Нецелое будет округлено в сторону нуля: 2.999 => 2, -0.999 => 0.)\n')

    return int(step)


def create_alphabet() -> str or list:
    lang = input('На каком языке будет Ваш текст? Напишите "Русский" или "Английский".\n').lower()
    while not lang in {'русский', 'английский'}:
        lang = input('Проверьте написание слов "Русский"/"Английский"\n').lower()

    low_alphabet = ''
    high_alphabet = ''

    if lang == 'русский':
        for i in range(ord('а'), ord('я') + 1):
            low_alphabet += chr(i)
        for i in range(ord('А'), ord('Я') + 1):
            high_alphabet += chr(i)
    else:
        for i in range(ord('a'), ord('z') + 1):
            low_alphabet += chr(i)
        for i in range(ord('A'), ord('Z') + 1):
            high_alphabet += chr(i)

    return [high_alphabet, low_alphabet]


def ceasar_cipher(text: str, direction: str, alphabet: list, step: int) -> str:
    lenght = len(alphabet[0])
    cipher = ''

    if direction == 'шифр':
        for el in text:
            if el in alphabet[0]:
                i = alphabet[0].index(el)
                cipher += alphabet[0][(i + step) % lenght]
            elif el in alphabet[1]:
                i = alphabet[1].index(el)
                cipher += alphabet[1][(i + step) % lenght]
            else:
                cipher += el

    elif direction == 'дешифр':
        for el in text:
            if el in alphabet[0]:
                i = alphabet[0].index(el)
                cipher += alphabet[0][(i - step) % lenght]
            elif el in alphabet[1]:
                i = alphabet[1].index(el)
                cipher += alphabet[1][(i - step) % lenght]
            else:
                cipher += el

    return cipher


def main():
    text = input('Какой текст Вы хотите преобразовать?\n')
    direction = is_valid_direction()
    alphabet = create_alphabet()
    step = is_valid_step()

    print(ceasar_cipher(text, direction, alphabet, step))


if __name__ == '__main__':
    main()
