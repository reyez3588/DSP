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
fig,ax = plt.subplots(1, 2, sharex=True, sharey=True)
N = 256
freqs = np.arange(0, N/2)*fs/N

X = np.fft.fft(x, N)
print(X)
for i in range (len(X)):
    X[i] = ((X[i].real)**2 + (X[i].imag)**2)**(1/2)
print(X)
X[X<np.finfo(float).eps] = np.finfo(float).eps
XdB = 20 * np.log(X) # convertir a dB
ax[0].plot(freqs,XdB[0:128])

XW = np.fft.fft(xw, N)
#print(X)
for i in range (len(X)):
    XW[i] = ((XW[i].real)**2 + (XW[i].imag)**2)**(1/2)
#print(X)
XWdB = 20 * np.log(XW) # convertir a dB
ax[1].plot(freqs,XWdB[0:128])

plt.show()

'''
Para obtener el valor de la frecuencia 
'''
# f = m*fs/N
valMax = max(XWdB)
m = 0
for i in range(int((len(X)+1) / 2)):
    if valMax == XWdB[i]:
        m = i
print("La frecuencia es: ", m*fs/N)


