import numpy as np
import pandas as pd
from astropy.io import fits
import matplotlib.pyplot as plt
from mnras import correct_tick_marks

run = 'L2800N5040'
min_rp_scale_Mpc_h = 5.0
max_rp_scale_Mpc_h = 100.0
h = 0.681
xlim = (1, 300)
# ---- Data ----
wgg_measured = pd.read_hdf(
    f'/disks/shear16/herle/correlations1/correlations_galaxy_{run}_HYDRO_FIDUCIAL_0.0.h5'
)[['wgg_rp', 'wgg_xip']]
cov_wgg = np.load(f'/disks/shear16/herle/correlations1/wgg_cov_jk_galaxy_{run}_HYDRO_FIDUCIAL_0.0.npy')

wgp_measured = pd.read_hdf(
    f'/disks/shear16/herle/correlations1/correlations_galaxy_{run}_HYDRO_FIDUCIAL_0.0.h5'
)[['wgp_rp', 'wgp_xip']]
cov_wgp = np.load(f'/disks/shear16/herle/correlations1/wgp_cov_jk_galaxy_{run}_HYDRO_FIDUCIAL_0.0.npy')

wgg_rp = wgg_measured["wgg_rp"].values / h
wgg_measured["wgg_xip"] /= h
cov_wgg /= h**2

wgp_rp = wgp_measured["wgp_rp"].values / h
wgp_measured["wgp_xip"] /= h
cov_wgp /= h**2

# ---- Models ----
wgg_aniruddh = np.load('/disks/shear16/herle/code/wgg_model_scipy_ccl.npy')
wgp_aniruddh = np.load('/disks/shear16/herle/code/wgp_model_scipy_ccl.npy')

#romain
hdul = fits.open("flamingo_fit_TATT_rp.fits")
bestfit = hdul['BESTFIT'].data
rp_romain = bestfit['rp'] /h
wgg_romain = bestfit['wgg'] /h
wgp_romain = bestfit['wgp'] /h

#dennis
dennis_wgg = np.loadtxt('/disks/shear16/herle/code/flamingo_L2800N5040_dennis_gg.txt')
dennis_wgg_rp = dennis_wgg[:,0] 
dennis_wgg_xip = dennis_wgg[:,1]
dennis_wgp = np.loadtxt('/disks/shear16/herle/code/flamingo_L2800N5040_dennis_gp.txt')
dennis_wgp_rp = dennis_wgp[:,0] 
dennis_wgp_xip = dennis_wgp[:,1]

#david
david_wgg = np.loadtxt('/disks/shear16/herle/code/david_wgg_model.txt')
david_wgp = np.loadtxt('/disks/shear16/herle/code/david_wgp_model.txt')
david_rp = np.loadtxt('/disks/shear16/herle/code/david_rp_model.txt')


# ---- Plotting ----
fig, axes = plt.subplots(
    2, 2,
    figsize=(15, 12),
    sharex='col',
    gridspec_kw={'height_ratios': [3, 1]}  # Top row taller
)
ax1, ax2 = axes[0, 0], axes[0, 1]
ax1_resid, ax2_resid = axes[1, 0], axes[1, 1]

# --- wgg main plot ---
ax1.errorbar(wgg_rp, wgg_measured["wgg_xip"].values, 
             yerr=np.sqrt(np.diag(cov_wgg)), fmt='o', color='black', label='Data')

ax1.plot(rp_romain, wgg_romain, color='blue', linestyle='--', label='Romain')
ax1.plot(wgg_rp, wgg_aniruddh, color='green', linestyle='--', label='Aniruddh')
ax1.plot(rp_romain, wgg_romain, color='blue', linestyle='--', label='Romain')
ax1.plot(dennis_wgg_rp, dennis_wgg_xip, color='red', linestyle='--', label='Dennis')
ax1.plot(david_rp, david_wgg, color='cyan', linestyle='--', label='David')

ax1.set_xscale('log')
ax1.set_xlim(xlim[0], xlim[1])
ax1.set_ylabel('$w_{gg}[Mpc]$')
ax1.axvspan(xlim[0], min_rp_scale_Mpc_h/h, alpha=0.5, color='gray')
ax1.axvspan(max_rp_scale_Mpc_h/h, xlim[1], alpha=0.5, color='gray')

ax1.axvspan(xlim[0], 10/h, alpha=0.1, color='gray')
ax1.axvspan(100/h, xlim[1], alpha=0.1, color='gray')

ax1.set_ylim(0, 125)

correct_tick_marks(ax1)

# --- wgg residuals ---
resid_wgg_romain = 100.0 * (wgg_measured["wgg_xip"].values - np.interp(wgg_rp, rp_romain, wgg_romain)) / wgg_measured["wgg_xip"].values
resid_wgg_your = 100.0 * (wgg_measured["wgg_xip"].values - wgg_aniruddh) / wgg_measured["wgg_xip"].values
resid_wgg_dennis = 100.0 * (wgg_measured["wgg_xip"].values - np.interp(wgg_rp, dennis_wgg_rp, dennis_wgg_xip)) / wgg_measured["wgg_xip"].values
resid_wgg_david = 100.0 * (wgg_measured["wgg_xip"].values - np.interp(wgg_rp, david_rp, david_wgg)) / wgg_measured["wgg_xip"].values

ax1_resid.plot(wgg_rp, resid_wgg_romain, 'o', color='blue', label='Romain')
ax1_resid.plot(wgg_rp, resid_wgg_your, 'o', color='green', label='Aniruddh')
ax1_resid.plot(wgg_rp, resid_wgg_dennis, 'o', color='red', label='Dennis')
ax1_resid.plot(wgg_rp, resid_wgg_david, 'o', color='cyan', label='David')

ax1_resid.axhline(0, color='k', lw=1)
ax1_resid.set_xscale('log')
ax1_resid.set_xlim(xlim[0], xlim[1])
ax1_resid.set_xlabel('$r_{p} [Mpc]$')
ax1_resid.set_ylabel(r'$\delta / \mathrm{signal}$ [%]')
ax1_resid.axvspan(xlim[0], min_rp_scale_Mpc_h/h, alpha=0.5, color='gray')
ax1_resid.axvspan(max_rp_scale_Mpc_h/h, xlim[1], alpha=0.5, color='gray')
ax1_resid.axvspan(xlim[0], 10/h, alpha=0.1, color='gray')
ax1_resid.axvspan(100/h, xlim[1], alpha=0.1, color='gray')
ax1_resid.set_ylim(-50, 50)
# ax1_resid.legend(frameon=False)
correct_tick_marks(ax1_resid)

# --- wgp main plot ---
ax2.errorbar(wgp_rp, wgp_measured["wgp_xip"].values, 
             yerr=np.sqrt(np.diag(cov_wgp)), fmt='o', color='black', label='Data')
ax2.plot(rp_romain, wgp_romain, color='blue', linestyle='--', label='Romain')
ax2.plot(wgp_rp, wgp_aniruddh, color='green', linestyle='--', label='Aniruddh')
ax2.plot(dennis_wgp_rp, dennis_wgp_xip, color='red', linestyle='--', label='Dennis (lin bias+NLA)')
ax2.plot(david_rp, david_wgp, color='cyan', linestyle='--', label='David')

ax2.set_xscale('log')
ax2.set_xlim(xlim[0], xlim[1])
ax2.set_ylabel('$w_{g+}[Mpc]$')
ax2.axvspan(xlim[0], min_rp_scale_Mpc_h/h, alpha=0.5, color='gray')
ax2.axvspan(max_rp_scale_Mpc_h/h, xlim[1], alpha=0.5, color='gray')
ax2.axvspan(xlim[0], 10/h, alpha=0.1, color='gray')
ax2.axvspan(100/h, xlim[1], alpha=0.1, color='gray')
ax2.set_ylim(0, 1.5)
ax2.legend(frameon=False)
correct_tick_marks(ax2)

# --- wgp residuals ---
resid_wgp_romain = 100.0 * (wgp_measured["wgp_xip"].values - np.interp(wgp_rp, rp_romain, wgp_romain)) / wgp_measured["wgp_xip"].values
resid_wgp_your = 100.0 * (wgp_measured["wgp_xip"].values - wgp_aniruddh) / wgp_measured["wgp_xip"].values
resid_wgp_dennis = 100.0 * (wgp_measured["wgp_xip"].values - np.interp(wgp_rp, dennis_wgp_rp, dennis_wgp_xip)) / wgp_measured["wgp_xip"].values
resid_wgp_david = 100.0 * (wgp_measured["wgp_xip"].values - np.interp(wgp_rp, david_rp, david_wgp)) / wgp_measured["wgp_xip"].values

ax2_resid.plot(wgp_rp, resid_wgp_romain, 'o', color='blue', label='Romain')
ax2_resid.plot(wgp_rp, resid_wgp_your, 'o', color='green', label='Aniruddh')
ax2_resid.plot(wgp_rp, resid_wgp_dennis, 'o', color='red', label='Dennis')
ax2_resid.plot(wgp_rp, resid_wgp_david, 'o', color='cyan', label='David')

ax2_resid.axhline(0, color='k', lw=1)
ax2_resid.set_xscale('log')
ax2_resid.set_xlim(xlim[0], xlim[1])
ax2_resid.set_xlabel('$r_{p} [Mpc]$')
ax2_resid.axvspan(xlim[0], min_rp_scale_Mpc_h/h, alpha=0.5, color='gray')
ax2_resid.axvspan(max_rp_scale_Mpc_h/h, xlim[1], alpha=0.5, color='gray')
ax2_resid.axvspan(xlim[0], 10/h, alpha=0.1, color='gray')
ax2_resid.axvspan(100/h, xlim[1], alpha=0.1, color='gray')
ax2_resid.set_ylim(-20, 20)
# ax2_resid.legend(frameon=False)
correct_tick_marks(ax2_resid)

# --- Save figure ---
plt.tight_layout()
plt.savefig('/disks/shear16/herle/code/plots/model_joint_full_data_two_resid.png', bbox_inches='tight')
plt.show()
