#!/usr/bin/env python3

#129L Final Project Part 1 -- code to obtain and organize data on sunspots
#created 06Jun19 by Evan Eastin

import sunpy
from sunpy.net import hek
import numpy as np

client = hek.HEKClient()

t0 = '2000/01/01'
tf = '2000/01/03'
event_type = 'SS'

data = client.query(hek.attrs.Time(t0, tf), hek.attrs.EventType(event_type))

coord1 = np.array([elem['event_coord1'] for elem in data])
coord2 = np.array([elem['event_coord2'] for elem in data])
coord = np.column_stack((coord1, coord2))
tstart = [elem['event_starttime'] for elem in data]
tend = [elem['event_endtime'] for elem in data]
wavel = np.array([elem['obs_meanwavel'] for elem in data])*0.01
temp = 0.002898/wavel

nhemi = []
shemi = []

for i in range(0, len(coord1)):
	if coord1[i] > 0:
		nhemi.append(coord[i])
	else:
		shemi.append(coord[i])
		
print('Northern Hemisphere Events: ', nhemi)
print('Southern Hemisphere Events: ', shemi)
