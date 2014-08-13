import matplotlib.pyplot as plt
import numpy as np


class Visualiser:

    def __init__(self):
        pass

    def Q(self,Q_values, fig = None):
        action_ticks = []
        state_ticks = []
        for q in Q_values.iteritems():
            action_ticks.append(q[0][1])
            state_ticks.append(q[0][0])
        action_ticks = sorted(list(set(action_ticks)))
        state_ticks = sorted(list(set(state_ticks)))

        grid = []

        for action in action_ticks:

            grid_row = []
            for state in state_ticks:
                state_action = (state,action)
                grid_row +=[Q_values[state_action]]
            grid.append(grid_row)

        self.to_plt(grid, xtick_labels = state_ticks, ytick_labels = action_ticks,fig = fig)


    def to_grid(self, original_grid, mapping):
        """Convert a mapping from (x, y) to v into a [[..., v, ...]] grid."""
        self.rows=len(original_grid)
        self.cols=len(original_grid[0])
        grid = []
        for x in range(self.rows):
            line = []
            for y in range(self.cols):
                line += [mapping[x,y]]#
            grid.append(line)

        return grid

    def to_arrows(self, policy):
        """Print text arrows from a policy."""
        chars = {(1, 0):'v', (0, 1):'>', (-1, 0):'^', (0, -1):'<', None: '.'}
        return self.to_grid(dict([(s, chars[a]) for (s, a) in policy.items()]))

    def to_plt_arrows(self,original_grid, values, policy, fig = None):
        """Create an image from a values function and a policy ."""
        plt = self.to_plt(self.to_grid(original_grid, values))
        chars = {(1, 0):(0,0.2), (0, 1):(0.2,0), (-1, 0):(0,-0.2), (0, -1):(-0.2,0), None: None}
        #policy = dict([(s, chars[a]) for (s, a) in policy.items()])
        #print policy
        for x in range(self.rows):
            line = []
            for y in range(self.cols):
                #print x,y,  policy[x,y], "policy"
                val = chars[policy[x,y]]
                if(val is not None):
                    plt.arrow(y,x,val[0],val[1], hold = True)
        if (fig is not None):
            plt.savefig(fig)

        return plt


    def to_plt(self, grid, xtick_labels = None, ytick_labels = None,fig = None):
        """Create an image from a grid, intensity representing reward ."""
        #import numpy as np

        plt.clf()
        # Choose gray colormap
        cmap = plt.get_cmap("gist_gray")
        # Set ticks to the way we like them

        xticks = np.arange(0, len(grid[0]), 1)
        yticks = np.arange(0, len(grid), 1.0)
        plt.xticks(xticks)
        plt.yticks(yticks)




        extent = np.array([- 0.5,len(grid[0])- 0.5, len(grid) - 0.5, - 0.5])
        # create the image
        cax = plt.imshow(grid, cmap = cmap, interpolation="nearest", aspect='equal', extent=extent, origin='upper')
        #cax = plt.imshow(grid, cmap = cmap, interpolation="nearest")

        # Add colorbar
        cbar = plt.colorbar(cax, ticks=[-1, 0, 1])
        #plt.grid(True)
        for tick in yticks[:-1]: plt.axhline(tick + 0.5)
        for tick in xticks: plt.axvline(tick + 0.5)
        plt.hold(True)

        if(xtick_labels is not None):
            ax = plt.gca()
            ax.set_xticklabels(xtick_labels)
            ax.set_yticklabels(ytick_labels)

        if (fig is not None):
            plt.savefig(fig)
        return plt