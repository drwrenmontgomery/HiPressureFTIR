# HiPressureFTIR
Python tools for the manipulation and presentation of FTIR data, following analysis with fityk (a peakfitting tool).

muncher.py: reads in a ".peaks" file generated from fityk, extracts the peak centers and amplitudes (can be modified for peak widths) as file "allpeaksandamps.csv."

pressurepeakplotter.py: takes data from "allpeaksandamps.csv" (which may have been cleaned up by a researcher before plotting) and plots the pressure vs. peak center.

truncator.py: extracts a section of the FTIR spectrum, based on data index. (a version which truncates by wavenumber will be forthcoming.)  Useful for generating smaller (take up less memory) figures.

plot_transferulic_v1.py: very basic plotting script, each datafile is loaded individually

plotter.py: more sophisticated plotting script, accepts the folder containing datafiles as an argument, normalizes them to the largest peak in each and plots them with a specified offset.

[Source code](https://github.com/drwrenmontgomery/HiPressureFTIR)
