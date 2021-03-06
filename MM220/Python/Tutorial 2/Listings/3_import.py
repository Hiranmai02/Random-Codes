import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,4*np.pi,0.1) # start,stop,step
y = np.sin(x)
y = np.sin(x)
z = np.cos(x)

plt.plot(x,y,x,z)
plt.xlabel('x values from 0 to 4pi')
plt.ylabel('sin(x) and cos(x)')
plt.title('Plot of sin and cos from 0 to 4pi')
plt.legend(['sin(x)', 'cos(x)'])
plt.savefig('sincos.png')
plt.show()
