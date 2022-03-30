# -*- coding: utf-8 -*-
"""
Created on Wed Apr  8 16:10:06 2020

@author: Sanosh
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#importing CSV data file

#no of rows to skip at top
n= 0

#replace path of data file 
t=pd.read_csv('C:\\Users\\HP\\Desktop\\Gorkha.csv',skiprows=n,usecols=[0])
acc=pd.read_csv('C:\\Users\\HP\\Desktop\\Gorkha.csv',skiprows=n,usecols=[1])

#dt is time increment in every data
#dt=0.01 means it takes 100 data in a second
dt=0.01

#calculating length of data
n = len(acc)

#computing frequency using scipy fftpack
freq = np.fft.fftfreq(n, d=dt)


# Fast Fourier Transform of Acceleration
accfft = np.array(np.fft.fft(acc, axis=0))

#computing absolute value of fft
Accfft=np.abs(accfft)*dt

#plotting the spectral
plt.loglog(freq,Accfft,lw=0.4, color='k')
plt.xlabel('frequency, Hz')
plt.ylabel(' Amplitude cm/s^2')
plt.grid()
