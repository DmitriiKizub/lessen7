'''
Кодировка и байты
'''

# Строка - ?
# Изображение - ?
# Видео - ?
# Звук - ?

print(ord('@'))
print(chr(64))

# Байты и строки
some_str = 'Hello'
print(type(some_str))
some_byte = b'Hello'
print(some_byte)
print(type(some_byte))

for char in some_byte:
    print(char)


print(ord('E'))

some_utf_8_str = 'тут русские буквы'
# Кодирование - получились байты
some_utf_8_bytes = some_utf_8_str.encode('utf-8')

print(some_utf_8_bytes)

# Декодирование из байт в строку
some_utf_8_str = some_utf_8_bytes.decode('utf-8')
print(some_utf_8_str)

# Кодируем ASCII а декодируем  UTF-8

some_utf_8_str = 'Hello word'

some_utf_8_bytes = some_utf_8_str.encode('ASCII')
print(some_utf_8_bytes)
some_utf_8_str = some_utf_8_bytes.decode('utf-8')
print(some_utf_8_str)

# Кодировка при записи в файл
with open('code.txt', 'w',encoding='utf-8') as f:
    f.write('выапавы')
