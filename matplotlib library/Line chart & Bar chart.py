import matplotlib.pyplot as plt
age = [10,20,30,40,50,60,70]
weight = [35,55,60,70,74,72,75]
plt.plot(age,weight)
plt.show()

subjects  = ['maths','physics','chemistry']
marks = [78,80,60]
plt.bar(subjects,marks)
plt.show()

#plt.barh(subjects,marks)
#plt.bar(subjects,marks,weight=0.5)