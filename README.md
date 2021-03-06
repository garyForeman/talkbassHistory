talkbassHistory
===============

Author: Gary Foreman  
email: gforema2@illinois.edu  
[talkbass thread](http://www.talkbass.com/threads/thread-count-tb-classifieds.1081726/)

Python Packages
---------------
- matplotlib.pyplot
- numpy
- pyquery

R Libraries
-----------
- forecast
- ggplot2

If you wish to run this code make sure `monthYearDicts.py`, `history.py`, and 
`plot.py` are in the same directory. `history.py` imports `monthYearDicts.py`. 
Run by entering `./history.py` at the command line, but beware, this code takes 
about a half hour to run. `./history.py` will store the thread count data as 
a numpy array in a file called `monthArray.npy`, this way, you don't need to 
rerun the analysis each time you want to edit the plots. To generate the 
plots, run `./plot.py` at the command line, and it will create two files 
`thread_count_[FORUM].png` and `months_only_[FORUM].png`. The thread_count plot
contains the plot of the number of threads posted per month over the history
of the talkbass classifieds. The months_only plot plots the number of basses 
sold each month summed over the years 2006-2013.

time_series_bass.R.ipynb is a Jupyter notebook containing R code for a time
series analysis of the monthly talkbass counts data. If you wish to run any of
the sells in this notebook, you'll need to perform the data scraping first.
The data that is presented in the notebook is truncated after January 2016.
The plotARIMA.R and plotValidation.R files contain helper function for the
Jupyter notebook.
