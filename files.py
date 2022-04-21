'''
Примеры работы с текстовым файлом
'''

# open, close не оптимальный способ
f = open('moduls.txt','w')

f.write('hello\n')
f.write('hello\n')

f.writelines(['1\n','2\n','3\n','end'])

data = ['1;','2;','3;']
f.writelines(data)
f.close()

# Менеджер контекста
with open('moduls.txt','w') as f:
    f.write('hello\n')
    f.write('hello\n')

    f.writelines(['1\n', '2\n', '3\n', 'end'])

    data = ['1;', '2;', '3;']
    f.writelines(data)

print('end')

# Чтение файла
with open('moduls.txt','r') as f:
    # 1. Прочитать сразу все данные
    result = f.read()
    print(result)

print('*'*100)
with open('moduls.txt','r') as f:
    # 2. Прочитать построчно
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)
    result = f.readline()
    print(result)
print('*'*100)
with open('moduls.txt','r') as f:
    # 3. Читаем все строки в цикле
    for line in f:
        # line это каждая строка
        print(line.replace('\n',''))

print('*' * 100)
with open('moduls.txt','r') as f:
    # 3. Прочитать сразу все
    lines = f.readline()
    print(lines)