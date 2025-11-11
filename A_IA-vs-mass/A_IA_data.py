import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import sys
sys.path.append('./')
from A_IA_datastruct import *


'''
DESCRIPTION OF DATA STRUCTURE

'''
G25_red = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2025,
						A_IA_data = [2.44, 3.82, 4.14, 3.96, 8.07],
						A_IA_errorbars = [1.41, 1.59, 1.23, 1.18, 1.04],
						L_data = [10**(-0.74), 10**(-0.43), 10**(-0.24), 10**(-0.08), 10**(0.16)],
						marker_style = 'o',
						marker_color = 'xkcd:vermillion',
						plot_label = 'KiDS Bright red'
					)



G25_hns = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2025,
						A_IA_data = [0.51, 3.04, 3.03, 4.98, 6.54],
						A_IA_errorbars = [1.20, 1.30, 1.25, 1.61, 1.45],
						L_data = [10**(-0.77), 10**(-0.43), 10**(-0.24), 10**(0.08), 10**(0.16)],
						marker_style = 'v',
						marker_color = 'xkcd:mango',
						plot_label = 'KiDS Bright $n_s>2.5$'
					)

S23_rmh = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2023,
						A_IA_data = [3.47, 3.01, 4.13, 5.22],
						A_IA_errorbars = [[0.34, 0.31, 0.33, 1.11],[0.34, 0.31, 0.33, 1.11]],
						L_data = [0.49, 0.63, 0.83, 1.16],
						marker_style = 'd',
						marker_color = 'darkgreen',
						plot_label = 'DESY3 RMH'
					)


S23_rml = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2023,
						A_IA_data = [1.95, 2.86, 3.01, 4.39, 5.00],
						A_IA_errorbars = [[0.23, 0.29, 0.52, 0.20, 0.20],[0.23, 0.29, 0.51, 0.20, 0.21]],
						L_data = [0.19, 0.26, 0.35, 0.49, 0.73],
						marker_style = '<',
						marker_color = 'lime',
						plot_label = 'DESY3 RML'
					)

S23_cmass = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2023,
						A_IA_data = [2.23, 3.00, 3.78],
						A_IA_errorbars = [[0.92, 0.62, 0.49],[0.92, 0.61, 0.49]],
						L_data = [0.52, 0.79, 1.24],
						marker_style = '>',
						marker_color = 'mediumblue',
						plot_label = 'DESY3 CMASS'
					)


s15_lowz = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2015,
						A_IA_data = [8.5, 5, 4.7, 2.2],
						A_IA_errorbars = [0.9, 1., 1., 0.9],
						L_data = [1.55, 1.04, 0.87, 0.65],
                        z_data = [0.28, 0.28, 0.28, 0.28],
                        logMh_data = [14.06, 13.80, 13.68, 13.49],
                        logMh_errorbars = [0.048, 0.026, 0.027, 0.043],
						marker_style = '^',
						marker_color = 'darkmagenta',
						plot_label = 'LOWZ'
					)

J11 = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2011,
						A_IA_data = [5.91, 4.53, 4.51, 7.67, 9.98, 10.03, 12.93, 16.09, 1.20, 3.61],  # Megaz: lowz+highz (colour-cut); SDSS LRGs: faint, med, bright (lowz+highz resp.); SDSS Main: L4, L3 
						A_IA_errorbars = [[0.94, 1.17, 1.70, 1.71, 1.55, 1.49, 2.14, 2.75, 0.90, 2.06],[0.94, 1.16, 1.74, 1.75, 1.51, 1.45, 2.11, 2.76, 0.88, 2.09]],
						L_data = [0.91, 1.08, 1.06, 1.07, 1.50, 1.50, 2.13, 2.12, 0.33, 0.14],
                        z_data = [0.49, 0.59, 0.21, 0.32, 0.22, 0.31, 0.22, 0.31, 0.10, 0.07],
                        logMh_data = [13.55, 13.62, 13.87, 13.77, 14.11, 13.98, 14.35, 14.19, 12.65, 12.27],
                        logMh_errorbars = [0.056, 0.071, 0.037, 0.039, 0.065, 0.063, 0.105, 0.099, np.nan, np.nan],
						marker_style = 'h',
						marker_color = 'dimgrey',
						plot_label = 'J11'
					)

J19 = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2019,
						A_IA_data = [3.55, 3.63, 2.5],
						A_IA_errorbars = [[0.9, 0.79, 0.77],[0.82, 0.79, 0.73]],
						L_data = [1.47, 0.5, 0.29],
						marker_style = 'p',
						marker_color = 'black',
						plot_label = 'GAMA+SDSS'
					)

F21 = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2021,
						A_IA_data = [3.02, 1.21, 4.11, 3.02, 8.39, 1.80, 4.95, 5.71],  #D1-5, L1-3
						A_IA_errorbars = [[1.53, 1.63, 1.48, 2.37, 1.04, 0.96, 1.24, 1.57],[1.48, 1.64, 1.48, 2.33, 1.30, 0.95, 1.21, 1.60]],
						L_data = [0.21, 0.27, 0.35, 0.49, 0.89, 0.46, 0.65, 1.00],
                        z_data = [0.41, 0.42, 0.43, 0.45, 0.45, 0.53, 0.55, 0.56],
                        logMh_data = [12.43, 12.53, 12.65, 12.84, 13.32, 12.81, 13.02, 13.42],
                        logMh_errorbars = [[0.05, 0.06, 0.07, 0.08, 0.03, 0.08, 0.07, 0.02],[0.05, 0.06, 0.07, 0.08, 0.03, 0.08, 0.07, 0.05]],
						marker_style = 'x',
						marker_color = 'olive',
						plot_label = 'KiDS LRG'
					)

NG25 = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2025,
						A_IA_data = [2.54, 1.18, 3.91],
						A_IA_errorbars = [[1.90, 1.55, 1.50],[1.82, 1.57, 1.50 ]],
						L_data = [10**(-0.91), 10**(-0.58), 10**(-0.27)],
						marker_style = 'P',
						marker_color = 'deeppink',
						plot_label = 'PAUS'
					)


U17 = A_IA_survey(citation_url = "INSERT_url",
						pub_year = 2017,
						A_IA_data = [16.2, 48.0, 36.9, 10.4, 15.6, 19.1, 11.0, 10.9, 15.1],  # lowz, midz, highz with 3 bins of increasing richness each
						A_IA_errorbars = [11.8, 22.0, 11.3, 2.6, 3.0, 3.2, 3.1, 2.4, 2.4],
						L_data = [10**(-0.91), 10**(-0.58), 10**(-0.27)],
                        z_data = [0.127, 0.127, 0.127, 0.275, 0.273, 0.272, 0.383, 0.420, 0.465],
                        logMh_data = [14.088, 14.285, 14.608, 14.129, 14.333, 14.657, 14.188, 14.387, 14.726],
                        logMh_errorbars = [0.038, 0.032, 0.035, 0.039, 0.032, 0.035, 0.038, 0.032, 0.036],
						marker_style = 'H',
						marker_color = 'rosybrown',
						plot_label = 'SDSS RedMapper'
					)
