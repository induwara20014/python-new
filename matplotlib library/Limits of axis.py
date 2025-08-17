import matplotlib.pyplot as plt

#xlim()

plt.plot([1,2,3,4],[2,4,6,8])
left,right = plt.xlim(left=2,right=4)
print(left)
print(right)
plt.show()

#ylim()
plt.plot([1,2,3,4],[2,4,6,8])
bottom,top = plt.ylim(bottom=1,top=7)
print(bottom)
print(top)
plt.show()

