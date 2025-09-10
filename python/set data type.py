my_list = ['kamal', 20 , 'jaffna', False, 20]
my_tuple = ('kamal', 20, 'jaffna', False, 20)

my_set = {'kamal', 20, 'jaffna', False, 20}
my_set2 = set(my_list)

print(my_set2)
print(my_set)

my_set.remove('kamal')
print(my_set)

print(type(my_set))

A = {1,2,3,5,7}
B = {5,7,9,10,11}

print(A.union(B))
print(A.intersection(B))
print(B.difference(A))

my_set.add('saman')
print(my_set)
my_set.add(('Akila','Gihan'))
print(my_set)
my_set.update(['Yohan','Rohan'])
print(my_set)
my_set.remove(False)
print(my_set)
my_set.discard(10)
print(my_set)
my_set.pop()
print(my_set)
my_set.clear()
print(my_set)

