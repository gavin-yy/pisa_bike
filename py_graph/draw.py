import matplotlib.pyplot as plt
import numpy as np

def test():
    x = np.linspace(0, 6*np.pi, 100)
    y = np.sin(x)

    # You probably won't need this if you're embedding things in a tkinter plot...
    plt.ion()

    fig = plt.figure()
    ax = fig.add_subplot(111)
    line1, = ax.plot(x, y, 'r-') # Returns a tuple of line objects, thus the comma

    for phase in np.linspace(0, 10*np.pi, 500):
        line1.set_ydata(np.sin(x + phase))
        fig.canvas.draw()
        fig.canvas.flush_events()


class draw_img:
    x = []
    xmax = 0
    y1 = []
    y2 = []
    y3 = []
    fig = plt.figure()
    dict1 = {}
    dict2 = {}
    dict3 = {}

    def __init__(self):
        plt.ion()

        self.fig = plt.figure()
        self.ax1 = self.fig.add_subplot(111)
        self.ax1.set_xlim(-50, 50)
        self.ax1.set_ylim(-180, +180)

        self.line1, = self.ax1.plot(self.x, self.y1, 'r-', label='YAW') # Returns a tuple of line objects, thus the comma
        self.line2, = self.ax1.plot(self.x, self.y2, 'b-', label='PITCH')
        self.line3, = self.ax1.plot(self.x, self.y3, 'g-', label='ROLL')
        plt.legend()

    def append_data(self, d1,d2,d3):
        self.xmax += 1
        # self.x.append(self.xmax)
        # self.y1.append(d1)
        # self.y2.append(d2)
        # self.y3.append(d3)

        self.dict1[self.xmax] = d1
        self.dict2[self.xmax] = d2
        self.dict3[self.xmax] = d3

        #dynamic x range.
        xrange = list(range(self.xmax - 50, self.xmax))
        xlen = len(xrange)

        self.y1 = []
        self.y2 = []
        self.y3 = []
        for x in xrange:
            if x in self.dict1.keys():
                self.y1.append(self.dict1[x])
                self.y2.append(self.dict2[x])
                self.y3.append(self.dict3[x])
            else:
                self.y1.append(0)
                self.y2.append(0)
                self.y3.append(0)

        self.line1.set_xdata(xrange)
        self.ax1.set_xlim(self.xmax - 50, self.xmax)
        self.line1.set_ydata(self.y1)

        self.line2.set_xdata(xrange)
        self.ax1.set_xlim(self.xmax - 50, self.xmax)
        self.line2.set_ydata(self.y2)

        self.line3.set_xdata(xrange)
        self.ax1.set_xlim(self.xmax - 50, self.xmax)
        self.line3.set_ydata(self.y3)

        self.fig.canvas.draw()
        self.fig.canvas.flush_events()

    def append_data_array(self,ary):
        self.append_data(ary[0], ary[1],ary[2])

if __name__ == "__main__" :
    draw = draw_img()
    draw.append_data(10, 20, 80)
    draw.append_data(20, 30, 90)
    plt.pause(1000)
