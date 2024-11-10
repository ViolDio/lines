#1
my_dict = {'Artem': 1984,'Katya': 1995, 'Danya': 2005}
print(my_dict)
print(my_dict.get('Artem'))
print(my_dict.get('Egor', 'без ошибки'))
my_dict.update({'Slava': 2000,
                'Alex': 2002})
print(my_dict)
a = my_dict.pop('Katya')
print(a)
print(my_dict)

#2
my_set = {1,2,3,4,1,2, True, 'good'}
print(my_set)
print(my_set.add(5))
print(my_set.add(6))
print(my_set)
print(my_set.discard(2))
print(my_set)


