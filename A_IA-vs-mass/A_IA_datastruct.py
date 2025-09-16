import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

class A_IA_survey:
	def __init__(self, citation_url, pub_year,
				marker_style, marker_color, plot_label,
				A_IA_data=[], A_IA_errorbars=[],
				z_data=[], z_errorbars=[],
				L_data=[], L_errorbars=[],
				logMstar_data=[], logMstar_errorbars=[],
				logMh_data=[], logMh_errorbars=[],
				**kwargs):

		self.citation_url = citation_url
		self.pub_year = pub_year
		self.marker_style = marker_style
		self.marker_color = marker_color
		self.plot_label = plot_label
		self.A_IA_data = np.array(A_IA_data)
		self.A_IA_errorbars = np.array(A_IA_errorbars)
		self.z_data = np.array(z_data)
		self.z_errorbars = np.array(z_errorbars)
		self.L_data = np.array(L_data)
		self.L_errorbars = np.array(L_errorbars)
		self.logMstar_data = np.array(logMstar_data)
		self.logMstar_errorbars = np.array(logMstar_errorbars)
		self.logMh_data = np.array(logMh_data)
		self.logMh_errorbars = np.array(logMh_errorbars)
		self.__dict__.update(kwargs)
		self.axis_latex_labels = {"A_IA": r'$A_\mathrm{{IA}}$',
								  "z": r'$z$',
								  "logL": r'$\log(\langle L \rangle/L_0)$',
								  "L": r'$\langle L \rangle/L_0$',
								  "logMh": r'$\log(\langle M_h \rangle/M_0)$',
								  "Mh": r'$\langle M_h \rangle/M_0$',
								  "logMstar": r'$\log(\langle M_* \rangle/M_0)$',
								  "Mstar": r'$\langle M_* \rangle/M_0$',
								}
		self.axis_keys = self.axis_latex_labels.keys()


	def obtain_axis_data(self, key):
		if key not in self.axis_keys:
			raise ValueError("Not Implemented.")
		if key == "A_IA":
			return self.A_IA_data, self.A_IA_errorbars
		if key == "z":
			return self.z_data, self.z_errorbars
		if key == "logL":
			return np.log10(self.L_data), np.log10(self.L_errorbars)
		if key == "L":
			return self.L_data, self.L_errorbars
		if key == "logMh":
			return self.logMh_data, self.logMh_errorbars
		if key == "Mh":
			return 10**self.logMh_data, 10**self.logMh_errorbars
		if key == "logMstar":
			return self.logMstar_data, self.logMstar_errorbars
		if key == "Mstar":
			return 10**self.logMstar_data, 10**self.logMstar_errorbars
		return [], []