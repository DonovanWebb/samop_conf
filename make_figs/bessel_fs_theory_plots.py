from scipy.special import jv 
import matplotlib.pyplot as plt
import numpy as np

eta = 0.05
omega = np.linspace(0, 4,5000) #MHz
delta = 1.1 # MHz

tex_fonts = {
    # Use LaTeX to write all text
    #"text.usetex": True,
    "font.family": "serif",
    # Use 10pt font in plots, to match 10pt font in document
    "axes.labelsize": 14,
    "font.size": 14,
    # Make the legend/label fonts a little smaller
    "legend.fontsize": 14,
    "xtick.labelsize": 14,
    "ytick.labelsize": 14
}


plt.rcParams.update(tex_fonts)


plt.figure()
plt.plot(2*omega/delta, 1e3*eta*omega*(np.abs(jv(0, 2*omega/delta) + jv(2, 2*omega/delta))), label="standard MS")
plt.plot(2*omega/delta, 1e3*eta*omega, label="cnulled MS")
plt.xlabel(r"$2\Omega/\delta$")
plt.ylabel(r"$\Omega_{eff}$ (kHz)")
plt.legend()


omega = np.linspace(0, 4,5000)
delta = 1.1/2 # MHz
plt.figure()
plt.plot(2*omega/delta, 1e3*eta*omega*(np.abs(jv(1, 2*omega/delta) + jv(3, 2*omega/delta))), label="CANZZ")
plt.xlabel(r"$2\Omega/\delta$")
plt.ylabel(r"$\Omega_{eff}$ (kHz)")
plt.legend()
plt.show()
