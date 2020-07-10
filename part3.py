#!/usr/bin/env python3

#129L Final Project Part 3 -- user customizable program to plot locations of CMEs and sunspots on corresponding images

#import sunpy.map
from sunpy.net.helioviewer import HelioviewerClient
from matplotlib.image import imread
import matplotlib.pyplot as plt
from matplotlib import patches
hv = HelioviewerClient()



DAT = input('Date yyyy/m/d: ')
#IMRES = input('Image Resolution in arcseconds/pixel: ')
SRCID = input('Data Source ID: ')
#VIS = input('Visibility: ')
#OP = input('Opacity: ')
XFOC = input('Specify x-coord: ')
YFOC = input('Specify y-coord: ')

##include image size in a function, make dict for source ids, make optional args for composite images

IN = [SRCID, XFOC, YFOC]
FLIN = list(map(float, IN))

imgfile = hv.download_png(DAT, 6.0, [FLIN[0], 1.0, 100.0], x0=FLIN[1], y0=FLIN[2], width=512, height=512)


im = imread(imgfile)
plt.imshow(im)
plt.show()
 
