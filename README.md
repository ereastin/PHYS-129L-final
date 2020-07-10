Folder containing my final project for the PHYS 129L - Introduction to Scientific
Computation course at UCSB.

This program is intended to retrieve and display images of the sun
and specific solar events. Within the program, the user is 
instructed to enter a time interval to search, what specific solar event they
would like to see, what observatory/telescope/detector to use via the source ID,
and what colormap to use for plotting. The program, making use of sunpy, astropy,
and Pillow modules, queries the Heliophysics Event Knowledgebase (HEK) with the
entered time interval and event type and returns a list of recorded events within the
time interval and properties specific to each event. The program then parses the
information returned to retrieve the helioprojective cartesian x and y coordinates
(in arcseconds), as well as the start and end times of the event closest to the
start of the user requested time interval search. The start time of the event is
reformatted to match the required date format when querying Helioviewer.
The Helioviewer client request is then set up to retrieve and image at the requested
date. Lists containing the numerical detector IDs and colormap options are printed
for the user to select from. Once the desired source and colormap are selected,
the Helioviewer query returns a PNG image of the sun from the desired date.
Using Pillow, the PNG image is converted to JPG format, then split into RGB
components. The RGB component arrays are translated to FITS data types and
recompiled into a single FITS file for the sunpy Maps module to use. This file is
plotted in the user requested colormap centered at the center of solar disk.
The program then defines a region of interest centered on the coordinates of
the event, scaled to match that of the plotted image, returned by the HEK
query. This region of interest is mapped to a subplot that shows a zoomed in
image of the region of interest with a size of 120 by 120 arcseconds in the
same colormap as the original plot. A matplotlib module is used to clip the
brightest pixels out for better viewing, and the images are plotted. The fits
and jpg files created within the program are removed once the program has
finished running for continued use.

File descriptions

1. attrhelp.txt
  text file containing colormap keys, Helioviewer attribute names, and source
  IDs of telescope data sources available

2. FINALPROGRAM.py
  final python program. requires sunpy, astropy, and Pillow to run successfully.
  Pillow by default also requires the installation of 2 external libraries,
  libjpeg and zlib

3. CME1.png
  example output of a CME that can be returned by entering a time interval
  2011/06/07 to 2011/06/08, selecting CME, and selecting the AIA 193 data
  source with ID 11.
