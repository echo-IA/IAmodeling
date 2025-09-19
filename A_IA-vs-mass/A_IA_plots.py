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
	#ax.set_ylim([5e-1, 5.e1])
	return fig, ax


def plot_A_IA_3D(xaxis_key, yaxis_key, zaxis_key, data_keys = fiducial_plot_order, fit_on_the_fly = False, colorbar_scheme = 'RdYlBu'):
	# assumes color bar will be dictated by zaxis
	for key in data_keys:
		if key not in data_dict.keys():
			raise ValueError("Proposed data key not currently listed in data_dict.")
	if fit_on_the_fly==True:
		print('To be implemented...')

	fig, ax = plt.subplots(figsize=(10,7), layout='tight')
	#cm = plt.cm.get_cmap(colorbar_scheme)
	zdatas_max = []
	zdatas_min = []
	for data_key in data_keys:
		data = data_dict[data_key]
		xdata, xerr = data.obtain_axis_data(xaxis_key)
		ydata, yerr = data.obtain_axis_data(yaxis_key)
		zdata, _ = data.obtain_axis_data(zaxis_key)
		if xdata.size == ydata.size and xdata.size == zdata.size and xdata.size > 0 and ydata.size > 0 and zdata.size > 0:
			zdatas_max.append(np.max(zdata))
			zdatas_min.append(np.min(zdata))


	cmap = mpl.cm.get_cmap(colorbar_scheme)
	cNorm = mpl.colors.Normalize(vmin=np.min(zdatas_min), vmax=np.max(zdatas_max))
	scalarMap = mpl.cm.ScalarMappable(norm=cNorm, cmap=cmap)

	for data_key in data_keys:
		data = data_dict[data_key]
		xdata, xerr = data.obtain_axis_data(xaxis_key)
		ydata, yerr = data.obtain_axis_data(yaxis_key)
		zdata, zerr = data.obtain_axis_data(zaxis_key)
		marker = data.marker_style
		color = data.marker_color
		label = data.plot_label
		if xdata.size == ydata.size and xdata.size == zdata.size and xdata.size > 0 and ydata.size > 0 and zdata.size > 0:
			if xerr.size == 0: xerr = None
			if yerr.size == 0: yerr = None
			zerr = None
			#color = cm.to_rgba(zdata)
			im = ax.scatter(xdata, ydata, marker=marker, c='k', label=label)
			#cb = fig.colorbar(im)
			#color = cb.to_rgba(zdata)
			colorVal = scalarMap.to_rgba(zdata)
			for i in range(len(xdata)):
				xerr_temp = xerr
				yerr_temp = yerr

				if xerr_temp is not None:
					s = xerr_temp.shape
					if len(s)==1:
						xerr_temp = xerr_temp[i]
					if len(s)==2:
						xerr_temp = [[xerr_temp[0][i]], [xerr_temp[1][i]]]

				if yerr_temp is not None:
					s = yerr_temp.shape
					if len(s)==1:
						yerr_temp = yerr_temp[i]
					if len(s)==2:
						yerr_temp = [[yerr_temp[0][i]], [yerr_temp[1][i]]]
				im = ax.errorbar(xdata[i], ydata[i], xerr=xerr_temp, yerr=yerr_temp, ls='', marker=marker, markersize=8, c=colorVal[i])

		ax.set_xlabel(data.axis_latex_labels[xaxis_key])
		ax.set_ylabel(data.axis_latex_labels[yaxis_key])
	clb = fig.colorbar(scalarMap, location = 'top')
	clb.set_label(data.axis_latex_labels[zaxis_key])
	# Shrink current axis by 20%
	box = ax.get_position()
	ax.set_position([box.x0, box.y0, box.width * 1, box.height])
	# Put a legend to the right of the current axis
	ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=12)
	ax.set_yscale('log')
	#ax.set_xlim([-1, 0.5])
	#ax.set_ylim([5e-1, 5.e1])
	return fig, ax