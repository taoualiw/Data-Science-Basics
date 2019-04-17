import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
# Set the global font to be DejaVu Sans, size 10 (or any other sans-serif font of your choice!)
rc('font',**{'family':'sans-serif','sans-serif':['Arial'],'size':10})
# Set the font used for MathJax - more on this later
rc('mathtext',**{'default':'regular'})

# The following %config line changes the inline figures to have a higher DPI.
# You can comment out (#) this line if you don't have a high-DPI (~220) display.
#%config InlineBackend.figure_format = 'retina'
plt.rcParams["axes.titlesize"]='medium'

def custom_lineplot(ax, x, y, error, xlims, ylims, color='red'):
    """Customized line plot with error bars."""

    ax.errorbar(x, y, yerr=error, color=color, ls='--', marker='o', capsize=5, capthick=1, ecolor='black')

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_scatterplot(ax, x, y, error, xlims, ylims, color='green', markerscale=100):
    """Customized scatter plot where marker size is proportional to error measure."""

    markersize = error * markerscale

    ax.scatter(x, y, color=color, marker='o', s=markersize, alpha=0.5)

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_barchart(ax, x, y, error, xlims, ylims, error_kw, color='lightblue', width=0.75):
    """Customized bar chart with positive error bars only."""

    error = [np.zeros(len(error)), error]

    ax.bar(x, y, color=color, width=width, yerr=error, error_kw=error_kw, align='center')

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax

def custom_boxplot(ax, x, y, error, xlims, ylims, mediancolor='magenta'):
    """Customized boxplot with solid black lines for box, whiskers, caps, and outliers."""

    medianprops = {'color': mediancolor, 'linewidth': 2}
    boxprops = {'color': 'black', 'linestyle': '-'}
    whiskerprops = {'color': 'black', 'linestyle': '-'}
    capprops = {'color': 'black', 'linestyle': '-'}
    flierprops = {'color': 'black', 'marker': 'x'}

    ax.boxplot(y,
               positions=x,
               medianprops=medianprops,
               boxprops=boxprops,
               whiskerprops=whiskerprops,
               capprops=capprops,
               flierprops=flierprops)

    ax.set_xlim(xlims)
    ax.set_ylim(ylims)

    return ax
def stylize_axes(ax, title, xlabel, ylabel, xticks=[], yticks=[], xticklabels=[], yticklabels=[]):
    """Customize axes spines, title, labels, ticks, and ticklabels."""
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.xaxis.set_tick_params(top=False, direction='out', width=1)
    ax.yaxis.set_tick_params(right=False, direction='out', width=1)
    ax.set_title(title)
    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)
    if len(xticks)>0:
        ax.set_xticks(xticks)
    if len(yticks)>0:
        ax.set_yticks(yticks)
    if len(xticklabels)>0:
        ax.set_xticklabels(xticklabels)
    if len(yticklabels)>0:
        ax.set_yticklabels(yticklabels)

def cm2inch(value):
    return value/2.54
def goldenRatio(width):
    height = width / (.5*np.sqrt(5) + .5) #1.6
    return height
# PNAS Figure Sizes
oneColumnWidth = cm2inch(8.7)#3.42
oneandhalfColumnWidth = cm2inch(11.4)#4.5
twoColumnWidth = cm2inch(17.8)#7
maxheight = cm2inch (22.5)
# Text size minimum 6-8 points
