#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last modified: June 3, 2014
#Reads in and plots the <FILENAME> numpy array
################################################################################

import numpy as np
import matplotlib.pyplot as plt
from monthYearDicts import *

FILENAME = "bass_guitars_sales" #the .npy file you wish to plot

NUMBER_OF_YEARS = 8
MONTHS_PER_YEAR = 12

monthArray = np.load(FILENAME + ".npy")

plt.plot(monthArray[:yearDict['2014']+monthDict['Jun']])
plt.xlim(xmin=yearDict['2005']+monthDict['Sep'],
         xmax=yearDict['2014']+monthDict['Jun'])
plt.xticks([yearDict['2006'], yearDict['2007'], yearDict['2008'], 
            yearDict['2009'], yearDict['2010'], yearDict['2011'],
            yearDict['2012'], yearDict['2013'], yearDict['2014']],
           ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
            "2014"])
plt.xlabel("year", size="xx-large")
#plt.ylabel("number of threads", size="xx-large")
plt.ylabel('number of "sales"', size="xx-large")
plt.title(FILENAME, size="xx-large")
#plt.savefig("thread_count_" + FILENAME + ".png")
plt.savefig("sales_count_bass_guitars.png")
#plt.show()
plt.clf()

yearTotals = np.empty(NUMBER_OF_YEARS, dtype=np.float64)
percentArray = np.zeros((NUMBER_OF_YEARS, MONTHS_PER_YEAR), dtype=np.float64)
year = 2006

for i in xrange(NUMBER_OF_YEARS):
    yearTotals[i] = \
        np.sum(monthArray[yearDict[str(year)]:yearDict[str(year+1)]])
    percentArray[i,:] += \
        monthArray[yearDict[str(year)]:yearDict[str(year+1)]] / yearTotals[i]
    year += 1

plt.bar(np.arange(12.) - 0.5, np.mean(percentArray, axis=0)*100., 1.0,
        yerr=np.std(percentArray, axis=0)*100., color="None", ecolor="black")
plt.xlim(xmin=-0.5, xmax=11.5)
plt.xticks(range(12), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", 
                       "Sep", "Oct", "Nov", "Dec"], 
           rotation=45, size="xx-large")
plt.yticks(size="x-large")
#plt.ylabel("Percentage of thread posts per year", size="xx-large")
plt.ylabel('Percentage of "sales" per year', size="xx-large")
plt.title("2006 - 2013", size="xx-large")
plt.savefig("monthly_percentage_" + FILENAME + ".png")
#plt.show()
