import matplotlib.pyplot as plt
import numpy as np

class Visualizer(object):
    def __init__(self, log_scale=False, series=()):
        """
        Creates a new Visualizer.

        Args:
            log: Boolean. Whether to use the log scale.

        Returns:
            A new Visualizer instance.

        """

        # Set whether or not to use a log scale.
        self.log_scale = log_scale

        # Set the data series for the graph.
        self.series = series

        # Enable interactive mode.
        plt.ion()

        # Initialize the plot.
        fig = plt.figure()
        self.ax = fig.add_subplot(111)
        self._setup()

    def update(self):
        """
        Updates the scatter plot, re-rendering it for viewing by the user.

        Args:
            None.

        Returns:
            None.

        """

        # Plot the data.
        self._plot()

        # If the log scale option has been provided, plot the data using a
        # log-scale.
        if self.log_scale:
            self.ax.set_yscale('log')

        # A short pause so Mac OS X 10.11.3 doesn't break.
        plt.pause(0.0001)

    def add_data(self, x, data={}):
        """
        Adds data for plotting.

        Args:
            x: Integer. A data point for the x-axis on the graph.
            data: Dictionary. Should be a dictionary of the form:
                { 'series1': Integer, 'series2': Integer }
                The provided integer data points will be appended to the
                existing data arrays for each of the provided series.

        Returns:
            None.

        """

        # Append the given x-axis data point.
        self.x.append(x)

        # For each provided series, append the given data point to the list
        # for the correct series.
        for label, datum in data.iteritems():
            self.y[label]['data'].append(datum)

    # Private methods

    def _setup(self):
        """ Sets up the plot. Initializes each series and adds a legend. """

        self.x = []
        self.y = { s: { 'color': np.random.rand(3,1), 'data': [] } for s in self.series }

        self._plot()

        # Create the legend.
        plt.legend(loc='upper left');

    def _plot(self):
        """ Re-renders the plot. """
        
        for label, data_dict in self.y.iteritems():
            self.ax.scatter(self.x, data_dict['data'], c=data_dict['color'], label=label)