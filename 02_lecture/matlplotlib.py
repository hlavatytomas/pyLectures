import numpy as np

import matplotlib.pyplot as plt 

x = np.linspace(0,4,20)
y = np.sin(x)
y2 = np.sin(x) + 1

# print(x)
# print(y)
plt.plot(x,y2,'b')
plt.plot(x,y,'r')


plt.title("sehfa")
plt.legend(['prvni graf', 'druhy graf'])

# plt.show()
plt.savefig('graf1.png')
plt.close()

x = np.linspace(0,4,20)
y = np.tan(x)

plt.plot(x,y)

# plt.show()
plt.savefig('graf2.png')


# plt.savefig('graf.png')



