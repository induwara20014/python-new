lst1 = [20,30,10,60]
lst2 = list((12,43,67,89))

print(lst1)
print(lst2)
print(type(lst1))
print(type(lst2))

my_list = ['kamal',20,'kandy',False,20]
print(my_list[-5])
print(my_list[2:4])
print(my_list[0:3])
print(my_list[0:3:2])
print(my_list[::2])

my_list = ['kamal',20,'kandy',False,20,[4,5,6]]
print(my_list[-1])
print(my_list[5][0])

print(my_list)
my_list[2] = 'colombo'
print(my_list)

#list add to data(append(),extend(),insert())
my_list1 = ['kamal', 20 , 'kandy', False , 20]

my_list1.append("saman")
print(my_list1)
my_list1.extend(['Amal' , 'sunil' , 56.343])
print(my_list1.index)
my_list1.insert(2,'hello')
print(my_list1)

#list remove the data(pop(),remove())

my_list1.pop(0)
print(my_list1)
my_list1.remove('saman')
print(my_list1)


print(len(my_list1))
print(my_list1.index('Amal'))
print(my_list1.count(20))

#my_list1[:] = [] or my_list1.clear()
my_list1.clear()
print(my_list1)





