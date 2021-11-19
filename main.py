import numpy as np
import matplotlib.pyplot as plt

"""
# x(t) = sin(2*pi*f0*n*1/fs)

#SEÑAL ORIGINAL
f0 = 7000             #es la frecuencia que se esta muestreando, en Hz
fs = 7000*100          #tiempo de muestreo 1/fs
n = np.arange(0, 0.01, 1/fs)   #índice de la secuencia
t = n*1/fs
y = np.sin(2 * np.pi * f0 * n )
#plt.plot(n[0:700],y[0:700])
plt.plot(n,y)
#plt.show()


#SEÑAL ORIGINAL CON FRECUENCIA DE MUESTREO MENOR
f0 = 7000             #es la frecuencia que se esta muestreando, en Hz
fs = 14000          #tiempo de muestreo 1/fs
n = np.arange(0, 0.01, 1/fs)   #índice de la secuencia
y = np.sin(2 * np.pi * f0 * n )
print(y)
#plt.plot(n,y, c = [1,0,0])
plt.scatter(n, y, c=[0,0,0],)
plt.show()



#ALIAS DE LA SEÑAL CON k=-1
f0 = 8000             #es la frecuencia que se esta muestreando, en Hz
fs = f0 * 100         #tiempo de muestreo 1/fs
n = np.arange(0, 0.01, 1/fs)   #índice de la secuencia
y = np.sin(2 * np.pi * f0 * n ) *-1
plt.plot(n,y, c = [1,0,0])
plt.show()
"""

from numpy import fft
Nf = 64
fs = 64
f = 10
t = np.arange(0,1,1/fs)
deltaf = 1/2.

# keep x and y-axes on same respective scale
fig,ax = plt.subplots(2, 2, sharex=True, sharey=True)
#fig.set_size_inches((8,3))
x=np.cos(2*np.pi*f*t) + np.cos(2*np.pi*(f+2)*t) # 2 Hz frequency difference
ax[0][0].plot(t,x)
X = fft.fft(x,Nf)/np.sqrt(Nf)
ax[1][0].plot(np.linspace(0,fs,Nf),abs(X),'-o')
ax[1][0].set_title(r'$\delta f = 2$ Hz, $T=1$ s',fontsize=18)
ax[1][0].set_ylabel(r'$|X(f)|$',fontsize=18)
ax[1][0].grid()
x=np.cos(2*np.pi*f*t) + np.cos(2*np.pi*(f+deltaf)*t) # delta_f frequency difference
X = fft.fft(x,Nf)/np.sqrt(Nf)
ax[1][1].plot(np.linspace(0,fs,Nf),abs(X),'-o')
ax[1][1].set_title(r'$\delta f = 1/2$ Hz, $T=1$ s')

plt.show()