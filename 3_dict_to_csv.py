"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    import csv

    employees = [
        {'name': 'Alex', 'age': '29', 'job': 'engineer', 'offer': '2300 USD'},
        {'name': 'Bill', 'age': '32', 'job': 'devops','offer': '3200 USD'},
        {'name': 'Jonh', 'age': '24', 'job': 'junior_dev','offer': '1900 USD'},
        {'name': 'Kate', 'age': '28', 'job': 'middle_dev','offer': '2700 USD'},
        {'name': 'Andy', 'age': '36', 'job': 'senior_dev','offer': '4000 USD'}
        ]

    with open('export.csv', 'w', encoding='utf-8', newline='') as f:
        fields = ['name', 'age', 'job', 'offer']
        writer = csv.DictWriter(f, fields, delimiter=';')
        writer.writeheader()        
        for employee in employees:
            writer.writerow(employee)

if __name__ == "__main__":
    main()
