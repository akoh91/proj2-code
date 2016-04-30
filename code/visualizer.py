import matplotlib.pyplot as plt
import numpy as np

class Visualizer(object):
    def __init__(self, log = False):
        self.opts = {}
        self.opts['log'] = log

        # Enable interactive mode.
        plt.ion()

        # Initialize the plot.
        fig = plt.figure()
        self.ax = fig.add_subplot(111)

    def setup(self, series):
        self.x = []
        self.y = { s: { 'color': np.random.rand(3,1), 'data': [] } for s in series }

        self._plot()

        # Create the legend.
        plt.legend(loc='upper left');

    def update(self):
        # Plot the data.
        self._plot()

        if self.opts['log']:
            self.ax.set_yscale('log')

        # A short pause so Mac OS X 10.11.3 doesn't break.
        plt.pause(0.0001)

    def add_data(self, x, data = {}):
        self.x.append(x)

        for label, datum in data.iteritems():
            self.y[label]['data'].append(datum)

    def _plot(self):
        for label, data_dict in self.y.iteritems():
            self.ax.scatter(self.x, data_dict['data'], c=data_dict['color'], label=label)