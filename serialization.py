'''
Сериализация - Сохранение объекта в виде байт
Десереализация - восстановление объекта
'''
import pickle


big_objict = {
    'items': ['1', (2, 3), ['some', 'else'], {'op', 'ap'}]
}
# Сереализация
result = pickle.dumps(big_objict)
print(result)

# Десериализация
big_objict_recovery = pickle.loads(result)
print(big_objict_recovery)

print(big_objict == big_objict_recovery)

# dump
with open('big_obj_data', 'wb') as f:
    pickle.dump(big_objict, f)

with open('big_obj_data', 'rb') as f:
    big_objict_recovery = pickle.load(f)
print(big_objict_recovery)