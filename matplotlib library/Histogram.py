import matplotlib.pyplot as plt
marks = [12,33,67,97,45,3,43,90,65,43,32,65,87,54,23]
plt.hist(marks,bins=[0,50,75,100],rwidth=0.95,color='g')
plt.show()