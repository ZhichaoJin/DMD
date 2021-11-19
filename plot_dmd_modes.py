# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 12:07:38 2020

@author: lerch
"""
import pandas as pd
import plot_snapshots
import numpy as np



#运行前需改动 plot_snapshots中文件名字以及文件标题
Phi_abs = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_mean_phi_abs.csv", delimiter = " ", header = None).values
freqs = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDfreqs_mean_imaginary.csv", delimiter = " ", header = None).values

# Phi_abs = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_phi_abs.csv", delimiter = " ", header = None).values
# freqs = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\optDMDfreqs_imaginary.csv", delimiter = " ", header = None).values

G = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\geometry.csv", skiprows = 0, delimiter = " ",names=["X","Y","Z"])
X = G["X"].values
Y = G["Y"].values
Z = G["Z"].values

## optDMD Mode Phase
A = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\snapshotbase_Shroud.csv", delimiter = " ", header = None).values

Phi_re = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_phi_real.csv", delimiter = " ", header = None).values
Phi_im = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_phi_imaginary.csv", delimiter = " ", header = None).values

# Phi_re = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_mean_phi_real.csv", delimiter = " ", header = None).values
# Phi_im = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\zj19\Desktop\optdmd\opt_mean_phi_imaginary.csv", delimiter = " ", header = None).values

def scalePhi(Phi,A):
    x1 = A[:,0]
    b = np.linalg.lstsq(Phi,x1)[0]
    m = np.size(Phi, 1) #columns of A
    n = np.size(Phi, 0) #rows of A
    Phi_scaled = np.zeros((n,m))
    for i in range (m):
        Phi_scaled[:,i] = Phi[:,i]*b[i]*2
    return Phi_scaled

Phi_phase = np.arctan(np.divide(Phi_im,Phi_re))

Phi_im = scalePhi(Phi_im,A)
Phi_re = scalePhi(Phi_re,A)

#plot_snapshots.plotPhase(X,Y,Z,Phi_phase,freqs)
#plot_snapshots.plotIm(X,Y,Z,Phi_im,freqs)
#plot_snapshots.plotRe(X,Y,Z,Phi_re,freqs)
plot_snapshots.plotAmplitude_alex(X,Y,Z,Phi_abs,freqs)
