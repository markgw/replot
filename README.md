# Replottable plot

Simple tool to output re-plottable plots using pyplot.

## Why?

Let's say you have some heaving, throbbing machine-learning model training and 
you want to output some plots of its progress as it goes. 
[Pyplot](https://matplotlib.org/api/pyplot_api.html) is great for this: you simply 
output your plot to a PDF. Say you output a graph of your training loss as training 
goes on.

Then you want to write a report about your model afterwards. This training plot is 
*almost* perfect, but you want to tweak the axes, title, etc. Now you have to 
start from scratch. Hopefully you output the per-iteration loss you were plotting – 
you wouldn't have forgotten that, surely? Oops, you need to run the whole thing again 
just to sort out your plot.

## What does it do?

Instead, you can ouptut a plot using ``replot``. All it does is:
 * pickle the data you need for plotting;
 * write out the pyplot-based plotting code to a Python script;
 * run the script in a subprocess, so you get to see your plot straight away.
 
Now you can just take the code and data and adjust them all you like afterwards!

## Installation

Install replot using pip:
```shell script
pip install git+https://github.com/markgw/replot.git
```

## Usage

Now you can use replot to wrap your pyplot plotting. Here's a simple example:
```python
import numpy as np
from replot import plot

# Code the does the actual plotting
plotting_code = """\
import matplotlib.pyplot as plt
from replot import get_data

# Read in the input data
data = get_data()
values = data["values"]

# Plot the data
fig = plt.figure()
plt.bar(list(range(len(values))), values)
plt.savefig("plot.pdf")
"""

# Generate some data and plot it
data = {"values": np.random.randint(0, 10, 10)}
plot(".", plotting_code, data)

```

Now our plot is in ``plot.pdf`` and we can also customize it without re-running 
the original code, by editing ``plot.py`` and running it.

Or you can put your plotting code in a separate Python file:
```python
import numpy as np
from replot import plot

# Generate some data and plot it
data = {"values": np.random.randint(0, 10, 10)}
plot(".", "my_plotting_code.py", data)

```

For a slightly longer, runable example, see ``example.py``.

## License

Replot is licensed under the Apache license, so you can build on it if you want.

Feel free to improve and create pull requests!
