
# startswith(), endswith()
name = "codepro lk"

print(name.startswith("c"))
print(name.startswith("pro",4))
print(name.endswith("c"))

print("-------------------------------------------")

#replace()

x = "kamal,22,colombo"

print(x)
print(x.replace(",","-"))
print(x.replace("l","z"))

print("---------------------------------------------")

#join()

x = 'abc'
y = 'xyz'

print("-".join(y))
print(x.join(y))

name = ["kamal","saman","nimal"]
print(" ".join(name))

#split()

name = "anil amala sunil nade \n 45 65 90"
print(name.split( ))
print(name.split("a"))

print(name.split("\n"))
print(name.splitlines())

