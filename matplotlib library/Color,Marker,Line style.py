import matplotlib.pyplot as plt
import numpy as np

x = [1,2,3,4,5,6,7]
plt.plot(x,np.power(x,2),'k^-.',x,np.power(x,3),'c+:')
plt.xlabel('X axis')
plt.ylabel('Y axis')
plt.title('Example')
plt.show()