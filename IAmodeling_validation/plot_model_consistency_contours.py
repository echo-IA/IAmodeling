import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from getdist import plots, MCSamples
from mnras import *
import emcee

plt.rcdefaults()
plt.rcParams['figure.figsize'] = (10, 10)
plt.rcParams['font.size'] = 22

def read_nautilus_samples(npz_filename):
    data = np.load(npz_filename)
    samples = data['samples']        # shape (Nsamples, Nparams)
    weights = data['weights']        # shape (Nsamples,)
    logl = data['logl']              # shape (Nsamples,)
    return samples, weights, logl

def read_chains(filename):

    sampler = emcee.backends.HDFBackend(filename)
    tau = sampler.get_autocorr_time(tol=0)
    if np.isnan(tau).any():
        print('tau is nan')
        samples = sampler.get_chain(flat=True)
    else:
        burnin = int(2 * np.max(tau))
        thin = int(0.5 * np.min(tau))
        samples = sampler.get_chain(discard=burnin, flat=True, thin=thin)
    
    return samples
ranges = {
    'b1': [1.0, 1.8],
    'b2': [-2.2, 1.2],
    'a1': [4.3, 5.4],
    'a2': [-0.2, 5.2],
    'ad': [-3.3, 0.2]  # <-- add whatever limits you want for b_TA/ad
}

# -----------------------
# Nautilus samples
# -----------------------
output_path = '/disks/shear16/herle/models/'
names = ['b1','b2', 'a1', 'a2', 'ad']
labels = ['b_1','b_2', 'A_1', 'A_2', 'A_{1\delta}']

min_rp_scale_Mpc_h, max_rp_scale_Mpc_h =  5, 100
filename = output_path + f"nautilus_results_TATT_2800_{min_rp_scale_Mpc_h}_{max_rp_scale_Mpc_h}_flamingo_ps_scipy2_pimax300.npz"
samples, weights, logl = read_nautilus_samples(filename)

samples_getdist = MCSamples(samples=samples, 
                            weights=weights,
                            names=names, 
                            labels=labels, 
                            ignore_rows=0,
                            ranges=ranges)

# Load David's chain (emcee HDF backend)
samples = read_chains('/disks/shear16/herle//code/david_wgp_L2800N5040.h5')

names = ['b1','b2','a1','a2','ad']   # ⚠️ make sure to match exactly the same as others
labels = ['b_1','b_2','A_1','A_2','A_{1\\delta}']

david_getdist = MCSamples(
    samples=samples,
    names=names,
    labels=labels,
    ignore_rows=0,
    ranges=ranges
)

# -----------------------
# Romain chains
# -----------------------
romain_chains = pd.read_csv('/disks/shear16/herle/code/chain_flamingo_romain.csv')

# Rename Romain parameters to match Nautilus naming
romain_samples_aligned = romain_chains.rename(
    columns={'A1':'a1', 'A2':'a2', 'bTA':'ad'}
)[['b1','b2','a1','a2','ad']].values

romain_getdist = MCSamples(
    samples=romain_samples_aligned,
    names=['b1','b2','a1','a2','ad'],
    labels=['b_1','b_2','A_1','A_2','A_{1\\delta}'],
    ignore_rows=0,
    ranges=ranges
)

# Load Dennis' chain and rename params
from getdist import plots, MCSamples

# Load Dennis' chain
dennis_getdist = plots.loadMCSamples(
    '/disks/shear16/herle/code/flamingo_fitting_dennis_results/flamingo_fitting_dennis_results'
)

# Extract samples and create a new MCSamples object with renamed parameters
samples_array = dennis_getdist.samples  # shape (Nsamples, Nparams)
param_names = dennis_getdist.getParamNames().list()  # original names

# Map the columns to match your internal naming
import numpy as np

# Find indices of the parameters you care about
b1_idx = param_names.index('b_1')
a1_idx = param_names.index('A_1')

# Build a new array with only the columns you want (b1 and a1)
renamed_samples = samples_array[:, [b1_idx, a1_idx]]

names = ['b1', 'a1']
labels = ['b_1', 'A_1']

dennis_getdist_renamed = MCSamples(
    samples=renamed_samples,
    names=names,
    labels=labels,
    ignore_rows=0)

# -----------------------
# Plotting
# -----------------------
g = plots.get_subplot_plotter()
g.settings.fig_width_inch = 12
g.settings.legend_fontsize = 25
g.settings.fontsize = 25
g.settings.axes_labelsize = 30
g.settings.axes_fontsize = 25



# Now plot with all 5 parameters
g.triangle_plot(
    [samples_getdist, romain_getdist, david_getdist, dennis_getdist_renamed],
    ['b1','b2','a1','a2','ad'],
    filled=[True, True],
    marker_args={'lw':1.5},
    contour_colors=['green','blue', 'cyan', 'red'],
    contour_ls=['-','--'],
    legend_labels=['Aniruddh','Romain', 'David', 'Dennis']
)

plt.savefig('/disks/shear16/herle/code/plots/consistency_contours.png')
plt.close()
# -----------------------
# Smaller triangle plot (only b1, a1) with Dennis included
# -----------------------


