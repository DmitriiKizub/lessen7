import json


# Объект -> сохраняем в строку
# Строка -> объект


# xml
# json
# yaml

person = {
    'name': 'Max',
    'age': 10,
    'phones':['8911', '73833'],
    '1':'test'
}
print('Начальный объект')
print(person)
print(type(person))
result = json.dumps(person)

print('В формате json')
print(result)
print(type(result))

print('Восстановленный объект')
person_recovery = json.loads(result)
print(person_recovery)
print(type(result))


# Записи в файл json
with open('person.json', 'w') as f:
    json.dump(person,f)

with open('person.json', 'r') as f:
    result = json.load(f)
    print(result)

