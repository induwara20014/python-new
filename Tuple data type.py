tpl1 = (23,54,65,76)
tpl2 = tuple((45,65,76,87))

print(type(tpl1))
print(type(tpl2))
print(tpl1)
print(tpl2)

print(tpl1[0])
print(tpl2[-2])
print(tpl1[1:3])

print(tpl1.count(23))
print(tpl1.index(65))

lst = [34,54,65,76]
print(type(lst))

tpl = tuple(lst)
print(tpl)
print(type(tpl))