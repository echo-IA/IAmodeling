import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from A_IA_data import *

data_dict = {'G25_red': G25_red,
			 'G25_hns': G25_hns,
			 'S23_rmh': S23_rmh,
			 'S23_rml': S23_rml,
			 'S23_cmass': S23_cmass,
			 's15_lowz': s15_lowz,
			 'J11': J11,
			 'J19': J19,
			 'F21': F21,
			 'NG25': NG25,
             'U17': U17,
			 }
fiducial_plot_order = data_dict.keys()


def plot_A_IA(xaxis_key, yaxis_key, data_keys = fiducial_plot_order, fit_on_the_fly = False):
	for key in data_keys:
		if key not in data_dict.keys():
			raise ValueError("Proposed data key not currently listed in data_dict.")
	if fit_on_the_fly==True:
		print('To be implemented...')

	fig, ax = plt.subplots(figsize=(10,7), layout='tight')
	for data_key in data_keys:
		data = data_dict[data_key]
		xdata, xerr = data.obtain_axis_data(xaxis_key)
		ydata, yerr = data.obtain_axis_data(yaxis_key)
		marker = data.marker_style
		color = data.marker_color
		label = data.plot_label

		if xdata.size == ydata.size and xdata.size > 0 and ydata.size > 0:
			if xerr.size == 0: xerr = None
			if yerr.size == 0: yerr = None
			ax.errorbar(xdata, ydata, xerr=xerr, yerr=yerr, ls='', marker=marker, markersize=8, c=color, label=label)
		ax.set_xlabel(data.axis_latex_labels[xaxis_key])
		ax.set_ylabel(data.axis_latex_labels[yaxis_key])

	# Shrink current axis by 20%
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 1, box.height])
	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
	ax.set_yscale('log')
	#ax.set_xlim([-1, 0.5])
	ax.set_ylim([5e-1, 5.e1])
	return fig, ax
