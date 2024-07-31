immutable_var = ('Номер', 1, 4, 7)
print("Immutable tuple:", immutable_var)
# immutable_var[0] = 'Число'
# immutable_var[2] = 3
print("Immutable tuple:", immutable_var)
# Кортеж - это список элементов, которые могут представлять различные типы данных. Он представлен в круглых скобках.
# Кортеж строго упорядочен, т.е. нельзя изменить какой-либо элемент данного списка, но к нему можно добавлять внешние.
immutable_var = immutable_var + (2, True)
print("Immutable tuple:", immutable_var)

mutable_var = ['Номер', 1, 4, 7]
print("Mutable list:", mutable_var)
mutable_var [0] = 'Число'
mutable_var [2] = 3
print("Mutable list:", mutable_var)
