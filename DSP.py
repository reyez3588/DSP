
import numpy as np
import matplotlib.pyplot as plt

# x = A*sin(2*pi*f*(n/fs))

f = 5
fs = 15.
nT = np.arange(0, 1, 1/fs )
print(nT)

x = np.sin(2 * np.pi * f * nT)
print(x)
#plt.plot(nT, x)
#plt.show()

w = np.hamming(len(x))
xw = x*w

FFTpuntos = 128
X = np.fft.fft(xw, FFTpuntos)
XdB = 20 * np.log(abs(X[0:int(len(X)/2)]))
#XdB = XdB / sum(XdB)
plt.plot(range(int(FFTpuntos/2)), XdB)
plt.show()

m = 0
maxVal = max(XdB)
for index in range(len(XdB)):
    if XdB[index] == maxVal:
        m=index

print("El valor de la frecuencia es: ", m*fs/FFTpuntos)