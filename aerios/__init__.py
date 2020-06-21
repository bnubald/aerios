from aerios.flight import Flight
from aerios.airport import Airport
from aerios.airplane import Airplane
import numpy as np
import os, sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import rc
params = {'legend.fontsize': 16,
          'font.size' : 16.0,
          'font.family': 'sans-serif',
          'axes.labelsize': 16,
          'axes.titlesize': 16,
          'axes.axisbelow': True,
          'xtick.labelsize' :16,
          'ytick.labelsize': 16,
          'mathtext.fontset': 'cm',
          'mathtext.rm': 'sans',
          'font.variant':'small-caps',
          'image.cmap' : 'jet',
          'font.serif': 'Computer Modern Roman',
          'font.family': 'serif'
         }
rc('text', usetex=True)
matplotlib.rcParams.update(params)