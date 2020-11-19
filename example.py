"""
Example usage of replot to output replottable plots with Pyplot.

"""
import numpy as np
from replot import plot

# Code the does the actual plotting
# You can also put this in a separate .py file and specify the path to it
plotting_code = """\
import matplotlib
# Force matplotlib to not use any Xwindows backend.
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from replot import get_data

# Read in the input data
data = get_data()

values = data["values"]

# Plot the data
fig = plt.figure()
ax = fig.add_subplot(111)

bars = ax.bar(list(range(len(values))), values)
ax.tick_params(
    axis='x',          # changes apply to the x-axis
    which='both',      # both major and minor ticks are affected
    bottom='off',      # ticks along the bottom edge are off
    top='off',         # ticks along the top edge are off
    labelbottom='off'
)

# Output the plot
plt.savefig("plot.pdf")
"""

# Now generate some data to plot
values = np.random.randint(0, 10, 10)
# Put the data in a dictionary
# In this case, it's just the values, but we might have other data structures too
data = {"values": values}

# Output the plotting code, data and the plot itself
plot(".", plotting_code, data)

# Now we've output the plot to plot.pdf
# but you can also edit the plotting code afterwards in plot.py and re-run
# the plotting by just calling that script!
