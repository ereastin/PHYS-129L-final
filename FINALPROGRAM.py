#!/usr/bin/env python3

#129L Final Project FINAL -- program to plot full size and zoomed in view of region of interest

##Required Imports
import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib import patches
import matplotlib.colors as colors
import astropy.units as u
from astropy.io import fits
import sunpy
import sunpy.map
import sunpy.cm
from sunpy.net import hek
from sunpy.net.helioviewer import HelioviewerClient
from PIL import Image
import numpy as np
import re
import sys
import os
import pprint

##Section 1 -- setting up user-determined server request for Heliophysics Event Knowledgebase -- has the user input time interval to search within and type of solar event. Program returns start/end times for first matching event found, as well as Helioprojective x and y coordinates for later use in plotting. 

client = hek.HEKClient()

print('Select a time interval to search for solar events \n')

while True:
	t0 = input('Insert a start time in the form YYYY/MM/DD: ')
	if re.match('^[1-2]{1}[0,1,9]{1}[0-9]{2}/[0-9]{2}/[0-9]{2}$', t0):
		break
	else:
		print('\nStart date was not in the specified form or is invalid, try again \n')

while True:
	tf = input('Insert an end time in the form YYYY/MM/DD: ')
	if re.match('^[1-2]{1}[0,1,9]{1}[0-9]{2}/[0-9]{2}/[0-9]{2}$', tf):
		break
	else:
		print('\nEnd date was not in the specified form or is invalid, try again \n')

#dictionary of visible events
eventdict= {}
eventdict['CME'] = 'CE'
eventdict['sunspot'] = 'SS'
eventdict['active region'] = 'AR'
eventdict['flare'] = 'FL'
eventdict['coronal hole'] = 'CH'
eventdict['coronal jet'] = 'CJ'
eventdict['coronal cavity'] = 'CC'
eventdict['eruption'] = 'ER'
eventdict['filament eruption'] = 'FE'
eventdict.keys()

while True:
	instr = None
	while instr not in {'CME', 'sunspot', 'active region', 'flare', 'coronal hole', 'coronal jet', 'coronal cavity', 'eruption', 'filament eruption'}:
		print('Please select a solar event from the list: CME, sunspot, active region, flare, coronal hole, coronal jet, coronal cavity, eruption, or filament eruption.')
		instr = input('Input a selection: ')

	event_type = eventdict[instr]

	data = client.query(hek.attrs.Time(t0, tf), hek.attrs.EventType(event_type))

	x = np.array([elem['hpc_x'] for elem in data])
	y = np.array([elem['hpc_y'] for elem in data])
	tstart = [elem['event_starttime'] for elem in data]
	tend = [elem['event_endtime'] for elem in data]
	time = list(tuple(zip(tstart, tend)))
	try:
		t = time[0]
	except IndexError:
		print('Your search returned 0 results, please select another event')
	else:
		break

print('Time span of event closest to start of selected interval: ', time[0])

##Section2 -- setting up server request to Helioviewer.org that returns image of the sun nearest to requested event start time. User chooses which data source (instrument/detector) to obtain image from using the source ID. Each source has a unique imaging wavelength.

timex = time[0][0]
searchtime = timex[:timex.find('T')]
date = searchtime.replace('-', '/')

hv = HelioviewerClient()

print('List of Observatories: [sourceID]:\n SDO HMI Mag: 19 \n SDO HMI Int: 18 \n SDO AIA 4500: 17 \n SDO AIA 94: 8 \n SDO AIA 131: 9 \n SDO AIA 335: 14 \n SDO AIA 171: 10 \n SDO AIA 304: 13 \n SDO AIA 1600: 15 \n SDO AIA 211: 12 \n SDO AIA 1700: 16 \n SDO AIA 193: 11 \n STEREO_B COR2-B: 31 \n STEREO_B EUVI-B 304: 27 \n STEREO_B EUVI-B 284: 26 \n STEREO_B EUVI-B 195: 25 \n STEREO_B EUVI-B 171: 24 \n STEREO_B COR1-B: 30 \n Yohkoh SXT white-light: 35 \n Yohkoh SXT thin-Al: 34 \n Yohkoh SXT AlMgMn: 33 \n SOHO MDI Mag: 6 \n SOHO MDI Int: 7 \n SOHO LASCO C3: 5 \n SOHO LASCO C2: 4 \n SOHO EIT 304: 3 \n SOHO EIT 284: 2 \n SOHO EIT 195: 1 \n SOHO EIT 171: 0 \n PROBA2 SWAP 174: 32 \n STEREO_A COR2-A: 29 \n STEREO_A EUVI-A 304: 23 \n STEREO_A EUVI-A 284: 22 \n STEREO_A EUVI-A 195: 21 \n STEREO_A EUVI-A 171: 20 \n STEREO_A COR1-A: 28')

id_list = ['19', '18', '17', '8', '9', '14', '10', '13', '15', '12', '16', '11', '31', '27', '26', '25', '24', '30', '35', '34', '33', '6', '7', '5', '4', '3', '2', '1', '0', '32', '29', '23', '22', '21', '20', '28']

source = None
while source not in id_list:
	source = input('Please input an available numerical data source ID: ')

SRCID = int(source)

cmap_list = ['sohoeit304', 'soholasco3', 'irissji5000', 'yohkohsxtal', 'sohoeit171', 'hinodexrt', 'irissjiSJI_NUV', 'sdoaia94', 'irissji1400', 'rhessi', 'irissjiFUV', 'sdoaia1700', 'stereocor2', 'irissji1600', 'irissjiNUV', 'sdoaia131', 'traceWL', 'trace1600', 'sdoaia335', 'trace1700', 'trace171', 'irissji2832', 'sdoaia171', 'sohoeit284', 'soholasco2', 'irissji1330', 'trace284', 'hmimag', 'stereohi2', 'hinodesotintensity', 'trace1216', 'stereocor1', 'sdoaia304', 'sdoaia193', 'sdoaia211', 'sdoaia4500', 'trace1550', 'trace195', 'stereohi1', 'yohkohsxtwh', 'irissji2796', 'sdoaia1600', 'sohoeit195']

print('List of available color maps: ')
pprint.pprint(cmap_list)
color = None
while color not in cmap_list:
	color = input('Select a color map to display: ')

cmap = plt.get_cmap(color)

imgfile = hv.download_png(date, 6.0, [SRCID, 5.0, 100.0], x0=0, y0=0, width=512, height=512)

##Section 3 -- PNG image downloaded from Helioviewer is processed using Pillow. The image is first converted to a JPG file, then split into RGB components. From these component files, a FITS image is compiled that sunpy.maps can readily use for plotting.

im = Image.open(imgfile)
imRGB = im.convert('RGB')
imRGB.save('im.jpg')
image = Image.open('im.jpg')
xsize, ysize = image.size
r,g,b = image.split()
r_data = np.array(r.getdata())
g_data = np.array(g.getdata())
b_data = np.array(b.getdata())

r_data = r_data.reshape(ysize, xsize)
g_data = g_data.reshape(ysize, xsize)
b_data = b_data.reshape(ysize, xsize)

red = fits.PrimaryHDU(data=r_data)
red.writeto('red.fits')
green = fits.PrimaryHDU(data=g_data)
green.writeto('green.fits')
blue = fits.PrimaryHDU(data=b_data)
blue.writeto('blue.fits')

img_list = ['red.fits', 'green.fits', 'blue.fits']
img_concat = []

for i in img_list:
	img_concat.append(fits.getdata(i))
	
img_final = np.flip(np.sum(img_concat, axis=0), axis=0)
imfinal = fits.PrimaryHDU(data=img_final)
imfinal.writeto('im.fits') 

##Section 4 -- Main section of the program. The sunpy map module reads the FITS file for plotting. The region of interest is defined by the HPC coordinates given by the HEK requested data and a subplot within the figure is created.

smap = sunpy.map.Map('im.fits')

#defines region of interest based on returned event coordinates
l = 60*u.arcsec
x0 = (x[0]/12)*u.arcsec
y0 = (y[0]/12)*u.arcsec

#initialize subpmap of zoomed region
submap = smap.submap(u.Quantity([x0-l, x0+l]), u.Quantity([y0-l, y0+l]))

fig = plt.figure(figsize=(5,12))
ax1 = fig.add_subplot(2,1,1, projection=smap)
smap.plot(cmap=cmap)
smap.draw_limb() #ensures solar limb is included

bttmleft = u.Quantity([x0-l, y0-l]) #defines area of zoomed region
l2 = l*2
smap.draw_rectangle(bttmleft, l2, l2) #places rectangle of size of zoomed region on original image

ax2 = fig.add_subplot(2,1,2, projection=submap)
submap.plot(cmap=cmap)
ax2.set_title('Zoomed Image of Region of Interest')

#clips out brightest pixels for better viewing
norm = colors.Normalize(vmin=smap.min(), vmax=smap.mean() + 3*smap.std())

#Remove created files for program reuse
os.remove('red.fits')
os.remove('blue.fits')
os.remove('green.fits')
os.remove('im.jpg')
os.remove('im.fits')

#Plot map and submap with colorbar
plt.colorbar()
plt.show()

