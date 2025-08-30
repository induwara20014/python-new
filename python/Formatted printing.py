name, age, score = "kamal", 22, 43.567

#He is kamal. He is 22 years old, and his score is 43..567.

print("He is "+ name + "He is "+ str(age) + " Years old, his score is " + str(score))
print("-------------------------------------------------------------------------------")

print("He is %s. He is %d years old, and his score is %.2f" %(name, age, score))
print("-------------------------------------------------------------------------")

print("He is {}.He is {} years old,and his score is {}".format(name,age,score))
print("He is {0}.He is {2} years old,and his score is {1}".format(name,age,score))
print("---------------------------------------------------------------------------------")

print(f"He is {name}. He is {age} years old, and his score is {score}")




