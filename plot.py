#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last modified: June 3, 2014
#Reads in and plots the monthArray numpy array
################################################################################

import numpy as np
import matplotlib.pyplot as plt
from monthYearDicts import *
from history import CLASSIFIEDS

monthArray = np.load("monthArray.npy")

plt.plot(monthArray[:yearDict['2014']+monthDict['Jun']])
plt.xlim(xmin=yearDict['2005']+monthDict['Sep'],
         xmax=yearDict['2014']+monthDict['Jun'])
plt.xticks([yearDict['2006'], yearDict['2007'], yearDict['2008'], 
            yearDict['2009'], yearDict['2010'], yearDict['2011'],
            yearDict['2012'], yearDict['2013'], yearDict['2014']],
           ["2006", "2007", "2008", "2009", "2010", "2011", "2012", "2013",
            "2014"])
plt.xlabel("year", size="xx-large")
plt.ylabel("number of threads", size="xx-large")
plt.title(CLASSIFIEDS, size="xx-large")
plt.savefig("thread_count_" + CLASSIFIEDS[:-5].replace("-", "_") + ".png")
#plt.show()
plt.clf()

monthsOnly = np.zeros(12, dtype=np.float64)
for i in xrange(len(monthArray[yearDict['2006']:yearDict['2014']])):
    monthsOnly[i % 12] += monthArray[i]

plt.bar(np.arange(12.) - 0.5, monthsOnly, 1.0)
plt.xlim(xmin=-0.5, xmax=11.5)
plt.xticks(range(12), ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", 
                       "Sep", "Oct", "Nov", "Dec"], 
           rotation=45, size="xx-large")
plt.yticks(size="xx-large")
plt.ylabel("Number of threads", size="xx-large")
plt.title("2006 - 2013", size="xx-large")
plt.savefig("months_only_" + CLASSIFIEDS[:-5].replace("-","_") + ".png")
