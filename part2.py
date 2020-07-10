#!/usr/bin/env python3

#129L Final Project Part 2 -- code to obtain and organize data on CMEs
#created 06Jun19 by Evan Eastin

import sunpy
from sunpy.net import hek
import numpy as np

client = hek.HEKClient()

t0 = '2012/01/01'
tf = '2012/01/02'
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

print('Select a solar event: CME, sunspot, active region, flare, coronal hole, coronal jet, coronal cavity, eruption, or filament eruption')
instr = input('Input a selection: ')
event_type = eventdict[instr]


data = client.query(hek.attrs.Time(t0, tf), hek.attrs.EventType(event_type))

x = np.array([elem['hpc_x'] for elem in data])
y = np.array([elem['hpc_y'] for elem in data])
tstart = [elem['event_starttime'] for elem in data]
tend = [elem['event_endtime'] for elem in data]
time = list(tuple(zip(tstart, tend)))
x0 = x[0]/12
y0 = y[0]/12
print(time[0][0])
r = time[0][0]
s = r[:r.find('T')]
print(s.replace('-', '/'))
