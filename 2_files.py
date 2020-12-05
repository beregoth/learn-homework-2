"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    ith open('referat.txt', 'r', encoding='utf-8') as f:
        text = f.read()
        len_text = len(text)
        print(f'Длина текста: {len_text} символов')
        count_word = len(set(text.replace(';', '').replace('.', '').replace(',', '').lower().split()))
        print(f'Количество слов в тексте: {count_word} слов')
        text = text.replace('.','!')
    with open('referat2.txt', 'w', encoding='utf-8') as ff:
        ff.write(text)

if __name__ == "__main__":
    main()
