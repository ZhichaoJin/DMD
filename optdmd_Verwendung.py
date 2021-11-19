from os import error
import numpy as np
import pandas as pd
import scipy
import scipy.integrate

from matplotlib import animation
from IPython.display import HTML
from matplotlib import pyplot as plt
from dmd import DMD
import functions_dmd as dfc
from optdmd import DMDOptOperator,OptDMD

import dmd, optdmd




dt = 60/(4000*256) # time step of signal, 4000 rev/min with 256 steps

snapshots = pd.read_csv(r"\\nas.tu-clausthal.de\win-home$\\zj19\Desktop\\MA\\snapshotbase_shroud.csv", delimiter = " ", header = None).values
X, Y = dfc.timeShift(snapshots) # create X(k+1) = Atilde * X(k), where X(k+1) is X2 and X(k) is X
#s = np.size(snapshots, 0) #number of rows in the snapshotbase
s = np.shape(snapshots)[0]
x1 = snapshots[:,1]
np.savetxt("x_1.csv", x1)

opt = DMDOptOperator(svd_rank=0, factorization="svd")
Uz,Sz,Vz, Q ,Atilde = opt.compute_operator(X,Y)
Sz_diag = np.diag(Sz)#S is a 1d array. for further calculations we need a 2d array with S on the main diagonal
#print(Sz.shape,Vz.shape)


np.savetxt("atilde.csv", Atilde)

#eigenvalues and eigenvectors of Atilde
lamb, W = dfc.eigenDecomposition(Atilde)

# opt DMD modes
Phi = dfc.dmdModes(Vz,Sz_diag,W,Y)

# Cut negative half plane of DMD spectrum and modes
Phi, lamb = dfc.cutModes(Phi, lamb)

np.savetxt("opt_mean_eigenvalues_real.csv", np.real(lamb))
np.savetxt("opt_mean_eigenvalues_imaginary.csv", np.imag(lamb))

np.savetxt("opt_mean_phi_real.csv", np.real(Phi))
np.savetxt("opt_mean_phi_imaginary.csv", np.imag(Phi))

# np.savetxt("opt_eigenvalues_real.csv", np.real(lamb))
# np.savetxt("opt_eigenvalues_imaginary.csv", np.imag(lamb))

# np.savetxt("opt_phi_real.csv", np.real(Phi))
# np.savetxt("opt_phi_imaginary.csv", np.imag(Phi))
Phi_abs = dfc.scaleModes(Phi,snapshots)
np.savetxt("opt_mean_phi_abs.csv", np.real(Phi_abs))
#np.savetxt("opt_phi_abs.csv", np.real(Phi_abs))

#DMD Spectra
DMDfreqs, DMDpower = dfc.dmdSpectrum(lamb, dt, Phi, snapshots, s)

rowsPhi_abs = len(Phi_abs)
colsPhi_abs = len(Phi_abs[0])
Phi_mean = np.zeros(colsPhi_abs)

for i in range (colsPhi_abs):
    Phi_mean[i] = sum(Phi_abs[:,i])/rowsPhi_abs
#snapshots的平均值运行一下保存    
np.savetxt("optDMDfreqs_mean_real.csv", np.real(DMDfreqs))
np.savetxt("optDMDfreqs_mean_imaginary.csv", np.imag(DMDfreqs))
np.savetxt("optDMDpower_mean.csv", DMDpower)
np.savetxt("optDMDpower_mean_Phi.csv", Phi_mean)
#只是opt运行一下保存
# np.savetxt("optDMDfreqs_real.csv", np.real(DMDfreqs))
# np.savetxt("optDMDfreqs_imaginary.csv", np.imag(DMDfreqs))
# np.savetxt("optDMDpower.csv", DMDpower)
# np.savetxt("optDMDpower_Phi.csv", Phi_mean)
