# -*- coding: utf-8 -*-
"""
Created on Wed May 27 13:52:52 2020

@author: lerch
"""

# Std Library imports
import numpy as np
from numpy.core.fromnumeric import shape
import pandas as pd
import matplotlib
matplotlib.rcParams['text.usetex'] = True #use latex in text
import matplotlib.pyplot as plt
plt.rc('font', **{'family': 'serif', 'serif': ['Computer Modern']})  #use latex also in labels
from matplotlib.ticker import MultipleLocator # to add minor ticks

# Local imports
import functions_dmd as dfc
import functions_fft as ffc

def readFile(fname, delim):
    A = pd.read_csv(fname , delimiter = delim, header = None).values # read the snapshotbase
    # insert check for correct snapshotbase structure
    return A

plt.rcParams.update({'font.size':24})

fname = r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\snapshotbase_Shroud.csv"
delim = " "
dt = 60/(4000*256) # time step of signal, 4000 rev/min with 256 steps
L = 0.015 # seconds covered by data, 4000 U/min, and 1 rev taken
s = 256 # stack length for DMD 1D
r = 163 # truncation threshold for DMD 1D
fmax =9000 # max freq on x axis
ymax = 350 # max pressure or velocity on y axis
label_y = r'$\displaystyle u$ [Pa]'

t = np.arange(0,L,dt)
N = np.size(t) # number of samples
n = int(N/2)

A = readFile(fname, delim)

A_point = A[1,:] # for creating a point data. 139123 is the node number of monitor point 2

#FFT

freqs, xpower = ffc.fourier_abs(A_point,dt,t)

np.savetxt("xpower.csv", xpower)
np.savetxt("freqs.csv", freqs)

# print(freqs.shape)
# print(xpower.shape)
opt_freqs =pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDfreqs_imaginary.csv", delimiter = " ", header = None).values
opt_xpower=pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDpower.csv", delimiter = " ", header = None).values
opt_freqs =np.asanyarray(opt_freqs).squeeze()#去除列属性
opt_xpower=np.asanyarray(opt_xpower).squeeze()
# print(opt_freqs.shape)
# print(opt_xpower.shape)
dmd_freqs =pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\MA\DMDfreqs_imaginary.csv", delimiter = " ", header = None).values
dmd_xpower=pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\MA\DMDpower.csv", delimiter = " ", header = None).values
dmd_freqs =np.asanyarray(dmd_freqs).squeeze()#去除列属性
dmd_xpower=np.asanyarray(dmd_xpower).squeeze()
# print(dmd_freqs.shape)
# print(dmd_xpower.shape)
opt_mean_freqs =pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDfreqs_mean_imaginary.csv", delimiter = " ", header = None).values
opt_mean_xpower=pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDpower_mean.csv", delimiter = " ", header = None).values
opt_mean_freqs =np.asanyarray(opt_mean_freqs).squeeze()#去除列属性
opt_mean_xpower=np.asanyarray(opt_mean_xpower).squeeze()





# plt.subplot(2, 2, 1)
# plt.xlabel(r'$\displaystyle f$ [Hz]')
# plt.ylabel(label_y)
# plt.bar(freqs,xpower, label= 'FFT 1D', color = "black", width = 50)
# plt.legend()
# plt.subplot(2, 2, 2)
# plt.xlabel(r'$\displaystyle f$ [Hz]')
# plt.ylabel(label_y)
# plt.bar(opt_freqs,opt_xpower, label= 'optDMD 1D', color = "orange", width = 20)
# plt.legend()
# plt.subplot(2, 2, 3)
# plt.xlabel(r'$\displaystyle f$ [Hz]')
# plt.ylabel(label_y)
# plt.bar(dmd_freqs,dmd_xpower, label= 'DMD 1D', color = "red", width = 20)
# plt.legend()
# plt.subplot(2, 2, 4)
# plt.xlabel(r'$\displaystyle f$ [Hz]')
# plt.ylabel(label_y)
# plt.bar(opt_mean_freqs,opt_mean_xpower, label= 'optmean', color = "green", width = 20)
# plt.legend()
# plt.suptitle("Comparison between FFT, DMD and optDMD on pressure")
# plt.axis([0,fmax,0,ymax])
# #plt.plot([1.699999],[30.641500], marker = "o", markersize = 6, color = "red")
# #plt.annotate("x = 1.699999, y = 30.641500",xy = (1.699999,30.641500), xytext = (1.699999+0.05,30.641500-1))
# plt.savefig('spectrum_rotor.png')
# plt.show()
#Mean FFT

# X_power_whole = readFile(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDpower.csv", delim)

# rowsX_power = len(X_power_whole)
# colsX_power = len(X_power_whole[0])
# X_power_mean = np.zeros(colsX_power)

# for i in range (colsX_power):
#     X_power_mean[i] = sum(X_power_whole[:,i])/rowsX_power
# np.savetxt("xpower_mean.csv", X_power_mean)  
# plt.xlabel(r'$\displaystyle f$ [Hz]')
# plt.ylabel(label_y)
# plt.bar(freqs,X_power_mean, label= 'FFT 2D', color = "blue", width = 5)
# #plt.plot([1.699999],[30.641500], marker = "o", markersize = 6, color = "red")
# #plt.annotate("x = 1.699999, y = 30.641500",xy = (1.699999,30.641500), xytext = (1.699999+0.05,30.641500-0.5))
# plt.savefig('spectrum_rotor_meanFFT.png')
# plt.show()
#DMD

# A_DMD = np.squeeze(np.transpose(A_point))
# A_DMD = np.concatenate((A_DMD,A_DMD))
# X0 = np.zeros((s,np.size(A_DMD)-s))
# for k in range (s):
#     X0[k,:] = A_DMD[k:np.size(A_DMD)-s+k]
    
# X, X2 = dfc.timeShift(X0)
# U,S,V = dfc.SVD(X)
# S = np.diag(S)
# S_med = np.median(S)
# r_opt = S_med*2.8582

#funktion für DMD plot
# def plotDMDpoint(s,r,A):
#     X0 = np.zeros((s,np.size(A)-s))
#     for k in range (s):
#         X0[k,:] = A[k:np.size(A)-s+k]
    
#     X, X2 = dfc.timeShift(X0)
#     U,S,V = dfc.SVD(X,r)
#     Atilde = dfc.calcAtilde(U,S,V,X2)
#     Lambda, W = dfc.eigenDecomposition(Atilde)
#     Phi = dfc.dmdModes(V,S,W,X2)
#     Phi, Lambda = dfc.cutModes(Phi, Lambda)
#     DMDfreqs, DMDpower = dfc.dmdSpectrum(Lambda, dt, Phi, X0, s)
#     DMDfreqs = DMDfreqs.imag
#     print(DMDpower)
#     plt.scatter(DMDfreqs, DMDpower, label = 'optDMD 1D', color = "orange", linewidths = 10)
#     for i,j in zip(DMDfreqs,DMDpower):
#         plt.annotate("x = %f, y = %f" %(i,j),xy =(i,j),xytext=(i+0.05,j))
#     plt.legend()

# plotDMDpoint(s,r,A_DMD)
# plt.savefig('spectrum_rotor_optDMD.png')
# plt.show()


#comparison with whole rotor pressure

# f_im = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDfreqs_imaginary.csv", header = None).values
# p = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDpower_mean.csv", header = None).values
# print(f_im.shape)
# print(p.shape)

# plt.scatter(freqs, xpower, label = 'FFT 2D', color = "green", linewidths = 10)
# plt.scatter(dmd_freqs, dmd_xpower, label = 'DMD 2D', color = "yellow", linewidths = 10)
plt.scatter(opt_freqs, opt_xpower, label = 'optDMD 2D', color = "blue", linewidths = 10)
plt.scatter(opt_mean_freqs, opt_mean_xpower, label = 'DMD 2D', color = "red", linewidths = 10)
# for i,j in zip(opt_freqs,opt_xpower):
#    plt.annotate("x = %f, y = %f" %(i,j),xy =(i,j),xytext=(i+0.05,j))
plt.legend()
plt.xlabel(r'$\displaystyle f$ [Hz]')
plt.ylabel(label_y)
# ml = MultipleLocator(50)
# plt.axes().xaxis.set_minor_locator(ml)
plt.grid(True, which = 'both')
plt.savefig('spectrum_rotor123.png')
plt.show()