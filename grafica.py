import matplotlib.pyplot as plt
import numpy as np

datos = np.loadtxt("album.txt")

y1 = datos[:,0]
y2 = datos[:,1]

x = np.arange(160)

plt.plot(x,y1)
plt.plot(x,y2)
plt.savefig("grafica.pdf")
