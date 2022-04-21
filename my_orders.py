'''
Программа для сохранения покупок
'''
import os
FILENAME = 'orders.txt'
orders = []
if os.path.exists(FILENAME):
    with open(FILENAME,'r') as f:
        for order in f:
            orders.append(order.replace('\n',''))


while True:
    print('1.Добавить покупку')
    print("2.История покупок")
    print('3.Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input("Введите название:")
        orders.append(name)
    elif    choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILENAME,'a') as f:
            for order in orders:

                f.write(f'{order}\n')
        break
    else:
        print('Не правильно введены данные')