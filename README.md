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
