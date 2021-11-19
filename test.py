import numpy as np
import matplotlib.pyplot as plt

# x = A*sin(2+pi*f*n/fs)
f = 4 # la frecuencia que se va a leer
fs = 25
nTs = np.arange(0, 1 , 1/fs)
#print(nTs)
x = np.sin(2*np.pi * f * nTs) # se supone que estos valores son las lecturas del sensor
w = np.hamming(len(x))
xw = x*w
#print(len(x))

# A partir de este punto estamos en el dominio de la frecuencia
N = 256
X = np.fft.fft(xw, N)
print(X)
Xaux = []
for i in range (len(X)):
    X[i] = ((X[i].real)**2 + (X[i].imag)**2)**(1/2)
print(X)
XdB = 10 * np.log(X) # convertir a dB
# f = m*fs/N
valMax = max(X)
m = 0
for i in range(int((len(X)+1) / 2)):
    if valMax == X[i]:
        m = i
print("La frecuencia es: ", m*fs/N)


plt.plot(XdB)
plt.show()



