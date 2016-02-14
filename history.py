#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last modified: February 13, 2016
#Reads in start dates of all threads in the given CLASSIFIEDS section, and 
#populates bins based on the number of threads started each month. Data begins
#in January 2005 and goes through February 2016
################################################################################

import csv
import numpy as np
from monthYearDicts import *
from pyquery import PyQuery as pq

CLASSIFIEDS = "for-sale-bass-guitars.126/"
#CLASSIFIEDS = "for-sale-amps-preamps-and-cabinets.127/"
#CLASSIFIEDS = "for-sale-accessories.129/"
NUM_PAGES = 2092
NUM_STICKY = 2 #used to discount the dates of the sticky threads
END_MONTH_YEAR = ['Feb', '2016'] #last month, year to from which to collect data

def get_page_url(i):
    """
    i : integer page number of classified section
    returns : full url path to desired page number
    """

    tb_classified_page = 'http://www.talkbass.com/forums/' + CLASSIFIEDS
    if i > 1: tb_classified_page += 'page-' + str(i)

    return tb_classified_page

def get_dates_list(d, page_number):
    """
    d : a PyQuery object containing web page html
    page_number: page number of classified forum. If one, makes sure to skip
                 sticky threads
    returns: list of lists where x[:,0] are months and x[:, 1] are years
    """

    start_dates = d('span.startDate').find('.DateTime').contents()
    if page_number == 1:
        start_dates = start_dates[NUM_STICKY:]

    start_dates_list = np.empty((30, 2), dtype=np.dtype('a4'))
    for i, date in enumerate(start_dates):
        date = date.split()
        start_dates_list[i] = [date[0], date[2]]

    return start_dates_list

def update_month_array(month_array, start_dates_list):
    """
    month_array: array tracking the number of threads started each month
    start_dates_list: new dates for which to add counts to month_array
    Adds counts to month_array to appropriate indices based on dates in
    start_dates_list
    """

    for date in start_dates_list:
        try:
            #KeyError will be thrown if year is before 2005
            month_array[year_dict[date[1]]+month_dict[date[0]]] += 1
        except KeyError:
            continue

def write_month_array(month_array, filename='thread_count.csv'):
    """
    month_array: array tracking the number of threads started each month
    filename: name of csv file to write, default: thread_count.csv
    Writes month array to csv format with three columns: year, month, and
    thread count. Month is stored as an integer from 1 to 12.
    """

    with open(filename, 'w') as outfile:
        csv_writer = csv.writer(outfile)
        for i in xrange(len(month_array)):
            year = 2005 + i / 12
            month = 1 + i % 12
            csv_writer.writerow([year, month, month_array[i]])

def main():
    month_array = np.zeros(year_dict[END_MONTH_YEAR[1]] + \
                          month_dict[END_MONTH_YEAR[0]] + 1, np.int32)

    for i in xrange(1, NUM_PAGES+1):
        tb_classified_page = get_page_url(i)

        #initialize PyQuery
        d = pq(tb_classified_page)

        start_dates_list = get_dates_list(d, i)
        update_month_array(month_array, start_dates_list)

        print("page", i, "finished")

    write_month_array(month_array, 'thread_count_for_sale_bass_guitars.csv')

if __name__ == "__main__":
    main()