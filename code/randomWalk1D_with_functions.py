#! /usr/bin/env python

import numpy as np # Numerical library
from matplotlib import pyplot as plt # Plotting library
import time

# Written for Computational Methods in Earth Sciences class

# Input
ntracers = 5000
stepsize = 1
update_period = 10 # update every this many time steps
plot_period = 100  # Plot every this many time steps
final_time_step = 5000

# Setup
def setup(ntracers, stepsize):
  tracers = np.zeros(ntracers) # Array of 0's
  tracer_id = np.arange(ntracers) + 1 # 1--500; can't do this with just range()
                                      # because + with lists is concatenation
                                      # instead, would be range(1, 501)
  x = np.arange(-100, 101)

def plotSetup():
  fig = plt.figure(figsize=(6,9)) # Create a figure OBJECT named "fig"
  ax1 = fig.add_subplot(211)
  ax1.plot(tracers, tracer_id, 'ko', alpha=.25)
  ax1.set_xlim(-100, 100)
  ax1.set_ylabel('Tracer ID')
  ax2 = fig.add_subplot(212) # Add one subplot to it that fills the whole space
                             # This OBJECT is called "ax2" for "axes object"
  ax2.hist(tracers, bins=np.arange(-100, 101, 5)) # Histogram
  ax2.set_xlabel('Distance from starting point') # This could also be "plt.xlabel"
                                                 # to work on the current figure
  plt.ylabel('Frequency of occurrence here') # illustrating other way to do this
  # I have set xlim and ylim arbitrarily. How would we set better axis limits
  # based on what we know about diffusion?
  plt.xlim(-4*np.sqrt(final_time_step), 4*np.sqrt(final_time_step))
  plt.ylim(0, ntracers/5.)
  plt.tight_layout() # Automatically c
  plt.show(block=False) # Allow script to keep running while plot is shown
  time.sleep(0.1) # Time to look at plot

# Run
# "+1" because "range" is exclusive ( [0, 501) = [0, 1, ..., 499, 500] )
for t in range(1, final_time_step + 1):

def update():
  # This method wastes a lot of time steps doing nothing. Look at np.arange and 
  # think about how this could improve the way we loop through this function.
  if t % update_period == 0:
    tracers += 2*np.random.randint(2, size=ntracers) - 1
  if t % plot_period == 0:
    ax1.clear() # If we want to remove prior time steps
    ax2.clear()
    plt.xlim(-4*np.sqrt(final_time_step), 4*np.sqrt(final_time_step))
    ax1.set_ylabel('Tracer ID')
    plt.xlim(-4*np.sqrt(final_time_step), 4*np.sqrt(final_time_step))
    plt.ylim(0, ntracers/5.)
    # Plot again
    ax1.plot(tracers, tracer_id, 'ko', alpha=.25)
    # plt.hist works like ax.hist, just on current axes
    # so if we had multiple axes up, we would have to specify which one to use.
    # (hint: we do in this case)
    # Easier to name them at the start
    ax2.hist(tracers, bins=np.arange(-100, 101, 5), color='b') # Histogram
    # Floor division with integer update_period is good for this
    ax2.plot(x, 2*ntracers/(t/update_period)**.5 * \
             np.exp(-x**2/(2.*(t/update_period))), color='0.', linewidth=2)
    plt.draw()
    time.sleep(0.1) # Time to look at plot
    
