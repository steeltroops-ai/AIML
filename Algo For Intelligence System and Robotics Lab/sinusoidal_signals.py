import matplotlib.pyplot as plt
import numpy as np

# create the time and frequency values
s = 100 
tr = 1.0/100 
t = np.arange(0, s*tr, tr)
n = len(t)
freq = n/tr

# create the three sinusoidal signals
f1 = 1 
y1 = 3*np.sin(2*np.pi*f1*t) 

f2 = 3 
y2 = np.sin(2*np.pi*f2*t) 

f3 = 7
y3 = np.sin(2*np.pi*f3*t) 

# sum the three sinusoidal signals
y = y1 + y2 + y3

# plot the sum of the sinusoidal signals
plt.plot(t, y, 'ro')
plt.show()

# compute the discrete Fourier transform of the sum of the sinusoidal signals
x = np.fft.fft(y)

# plot the magnitude of the discrete Fourier transform
plt.stem(np.abs(x), markerfmt=' ', basefmt='-b')
plt.show()
