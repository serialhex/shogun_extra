#/usr/bin/env python

# python script to test cool normal-distribution thing in shogun
# this code is under the "All Ur Base R Belong To Us" license
# what that entails exactly i'm not sure...
# so if you figure it out let me know ok?
# --serialhex

# must have the Shogun toolbox (http://www.shogun-toolbox.org/)
# && Matplotlib (http://matplotlib.sourceforge.net/) installed to use
from shogun.Library import Math
import pylab

def fill_list(x):
  a = 0
  b = []
  while a < x:
    b.append(Math.normal_random())
    a += 1
  return b

# how many values do you want to test this with?
nums = fill_list(1000000)

# thanks to Sergey Lisitsyn for (most of) the following...
# i still need to wake up!
n, bins, patches = pylab.hist(nums, 100)
pylab.plot(bins,pylab.normpdf(bins,0,1),'k--')
pylab.show()