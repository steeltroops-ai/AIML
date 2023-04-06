#y=a sin(wt + 0)    #here 0 = phi
#y(t)=a sin (2*pi*f*t + 0)

import numpy as np
import matplotlib.pyplot as plt

a = 1 # amplitude of the sinusoidal function
f = 5.0 # frequency of the sinusoidal function in Hertz
phi = 0 # phase shift of the sinusoidal function

def y(t):
    return a * np.sin(2*np.pi*f*t + phi)

s = 100 # number of samples
ts = 100/100 # sample interval
t = np.linspace(0, s*ts, s) # create an array of time values

# calculate the y values
y_values = y(t)

# plot the y values
plt.plot(t, y_values)

# show the plot
plt.show()
