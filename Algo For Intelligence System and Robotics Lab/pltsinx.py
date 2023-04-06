import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 20, 201)
y = np.sin(x)
plt.figure(figsize=(8,8))
plt.xlabel('Location(x)')
plt.ylabel('Amplitude')
plt.plot(x, y, 'b')
plt.show()




