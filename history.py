#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last modified: June 3, 2014
#Reads in start dates of all threads in the given CLASSIFIEDS section, and 
#populates bins based on the number of threads started each month. Data begins
#in January 2005 and goes through May 2014
################################################################################

import numpy as np
import urllib
from monthYearDicts import *

CLASSIFIEDS = "for-sale-bass-guitars.126/"
NUM_PAGES = 1705
NUM_STICKY = 3 #used to discount the dates of the sticky threads

monthArray = np.zeros(yearDict['2014']+monthDict['Jul'], np.float64)

if __name__ == "__main__":
    for i in xrange(1, NUM_PAGES+1):
        tbClassifiedPage = "http://www.talkbass.com/forums/" + CLASSIFIEDS
        if i > 1: tbClassifiedPage += "page-" + str(i)

        content = urllib.urlopen(tbClassifiedPage)
        lines = content.readlines()
        content.close()

        k = 0 #use this index to remove the first three sticky thread dates
        for j, line in enumerate(lines):
            #searches for the "Thread starter" html class string because the
            #line below that is where the OP date is contained
            if line.find("Thread starter") > 0:
                if i == 1 and k < NUM_STICKY:
                    k += 1
                    continue
                dateString = lines[j+1].split(">")[2].split("<")[0].split(" ")
                month = dateString[0]
                year = dateString[2]
                monthArray[yearDict[year]+monthDict[month]] += \
                    dayNormalizer[month]

        print "page", i, "finished"

    np.save("monthArray", monthArray)
