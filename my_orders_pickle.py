'''
Программа для сохранения покупок
Название + цена
'''
import os
import pickle
FILENAME = 'orders_pickpe.data'
orders = []
if os.path.exists(FILENAME):
    with open(FILENAME, 'rb') as f:
        orders = pickle.load(f)

while True:
    print('1.Добавить покупку')
    print("2.История покупок")
    print('3.Выход')
    choise = input('Введите номер: ')
    if choise == '1':
        name = input("Введите название:")
        cost = int(input("Введите цену: "))
        order = (name, cost)
        orders.append(order)
    elif choise == '2':
        for order in orders:
            print(order)
    elif choise == '3':
        with open(FILENAME,'wb') as f:
            pickle.dump(orders,f)
        break
    else:
        print('Не правильно введены данные')