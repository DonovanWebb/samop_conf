import matplotlib.pyplot as plt
import numpy as np

x = np.array([0,
     0,
     1,
     1,
     2,
     2,
     3,
     3,
     4,
     4,
    ])

plt.plot(1+x[0:-1],x[1:], color='b',linewidth=5)
plt.plot(9-x[0:-1],x[1:], color='b',linewidth=5)
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.xticks([])
plt.yticks([])
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.show()
