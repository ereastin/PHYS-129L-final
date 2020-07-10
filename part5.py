#!/usr/bin/env python3


import matplotlib.pyplot as plt
from matplotlib.image import imread
import astropy.units as u
from matplotlib import patches
from sunpy.net import HelioviewerClient
hv = HelioviewerClient()
imgfile = hv.download_png('2099/01/01', 4.8, [13, 1.0, 100.0], x0=0, y0=0, width=512, height=512)
fig, ax = plt.subplots(figsize=(5,4))

im = imread(imgfile)
ax.imshow(im, interpolation='nearest', origin='lower')
axins = ax.Axes.inset_axes([0.5, 0.5, 0.5, 0.5])
axins.imshow(im, interpolation='nearest', origin='lower')
x1, x2, y1, y2 = -1.5, -1.0, -2.5, -1.0
axins.set_xlim(x1, x2)
axins.set_ylim(y1, y2)
ax.Axes.indicate_inset_zoom(axins)

plt.show()

