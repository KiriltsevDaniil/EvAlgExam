import matplotlib.pyplot as plt


# View module from MVP pattern. Builds a pyplot on initialization
# and calls pyplot.show if pyplot was built successfully
class View:
    def __init__(self, f_max, generations, fitnesses, seed):
        self.chart = plt.figure()

        ax = self.chart.add_subplot(1, 1, 1)
        ax.xaxis.set_ticks_position('bottom')
        ax.yaxis.set_ticks_position('left')
        plt.axhline(y=f_max, color='r', label='Max Fitness')
        plt.plot(generations, fitnesses, 'b', label='Fitness')
        plt.grid()
        caption = f"seed: {seed}"
        plt.xlabel("Generation T")
        plt.ylabel("Fitness F")
        plt.legend(loc='upper left')
        plt.figtext(0.87, 0.01, caption, wrap=True, horizontalalignment='left', fontsize=12)

    def show(self):
        if self.chart is not None:
            plt.show()
        else:
            print("Nothing to show...")
