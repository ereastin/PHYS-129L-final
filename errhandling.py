#!/usr/bin/env python3
#systems to catch errors in user input
import sys

#while True:
#	SRCID = input('Input Numerical Data Source ID: ')
#	try:
#		n = int(SRCID)
#	except ValueError:
#		print("Your input was not an integer.  Try again.\n")
#	else:
#		break

#### 

#instr = None
#while instr not in {'CME', 'sunspot', 'active region', 'flare', 'coronal hole', 'coronal jet', 'coronal cavity', 'eruption', 'filament eruption'}:
#	print('Select a solar event: CME, sunspot, active region, flare, coronal hole, coronal jet, coronal cavity, eruption, or filament eruption')
#	instr = input('Input a selection: ')

#####

import re

while True:
	print('Select a time interval to search for solar events \n')
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

