"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""

def print_days():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import date, timedelta

    dt_now = date.today()
    delta1 = timedelta(days=-1)
    delta_30 = timedelta(days=30)
    dt_yesterday = dt_now - delta1
    dt_month = dt_now - delta_30
    print(f'Сегодня: {dt_now}, вчера: {dt_yesterday}, 30 дней назад: {dt_month}')


def str_2_datetime(date_string):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    from datetime import datetime

    date_dt = datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")
    return date_dt

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
