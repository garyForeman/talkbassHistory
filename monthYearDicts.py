#! /usr/bin/env python

################################################################################
#Author: Gary Foreman
#Last modified: June 2, 2014
#Sets up two dictionaries. One that translates a month string to an integer 
#0-12, and one that translates a year string year-2005 * 12
################################################################################

month_dict = {'Jan': 0, 'Feb': 1, 'Mar': 2, 'Apr': 3, 'May': 4, 'Jun': 5, 
              'Jul': 6, 'Aug': 7, 'Sep': 8, 'Oct': 9, 'Nov': 10, 'Dec': 11}

year_dict = {'2005': 0, '2006': 12, '2007': 24, '2008': 36, '2009': 48, 
             '2010': 60, '2011': 72, '2012': 84, '2013': 96, '2014': 108,
             '2015': 120, '2016': 132}

#dayNormalizer is used to remove the effect of months with more days naturally
#have more posts
day_normalizer = {'Jan': 1., 'Feb': 31./28., 'Mar': 1., 'Apr': 31./30., 
                  'May': 1., 'Jun': 31./30., 'Jul': 1., 'Aug': 1.,
                  'Sep': 31./30., 'Oct': 1., 'Nov': 31./30, 'Dec': 1.}
