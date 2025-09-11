my_dict = {'name':'kamal','age':20, 'city': 'kandy'}
students = {80:'kamal',81:'saman',82:'sunil'}

print(my_dict)
print(my_dict['age'])
print(type(my_dict))

print(my_dict)
my_dict['name'] = 'yomal'
print(my_dict)

my_dict['is_married'] = False
print(my_dict)

my_dict.update({'is_married':False, 'gender':'male'})
print(my_dict)

print(my_dict.get('name'))


del my_dict['age']

print(my_dict.pop('name'))
print(my_dict.pop('xyz',"Not Found"))

my_dict.clear()
print(my_dict)