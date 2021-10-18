
import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import QTimer
import gui
import numpy as np


class SilGui(QDialog):
    def __init__(self, parent=None):
        super(SilGui, self).__init__(parent)
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)

        self.number_of_drones = 5

        self.initialize_plot()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.plot)

        self.counter = 0
        self.timer.start(100)

    def initialize_plot(self):
        self.data = [self.gen_rand_line(100, 3) for index in range(self.number_of_drones)]
        self.lines = [self.ui.graphWidget.canvas.ax.plot(dat[0, 0:1], dat[1, 0:1], dat[2, 0:1])[0] for dat in self.data]
        self.ui.graphWidget.canvas.ax.set_xlim3d([0.0, 10.0])
        self.ui.graphWidget.canvas.ax.set_xlabel('X')
        self.ui.graphWidget.canvas.ax.set_ylim3d([0.0, 10.0])
        self.ui.graphWidget.canvas.ax.set_ylabel('Y')
        self.ui.graphWidget.canvas.ax.set_zlim3d([0.0, 10.0])
        self.ui.graphWidget.canvas.ax.set_zlabel('Z')

    def plot(self):
        self.lines = self.update_lines(self.counter, self.data, self.lines)
        self.ui.graphWidget.canvas.flush_events()
        self.ui.graphWidget.canvas.draw()
        self.counter += 1
        print(self.counter)
        if self.counter > 100:
            self.timer.stop()

    def gen_rand_line(self, length, dims=2):
        line_data = np.empty((dims, length))
        line_data[:, 0] = np.random.rand(dims)
        for index in range(1, length):
            step = (np.random.rand(dims) - 0.5) * 1
            line_data[:, index] = line_data[:, index - 1] + step
        return line_data

    def update_lines(self, num, data_lines, lines):
        for line, data in zip(lines, data_lines):
            line.set_data(data[0:2, :num])
            line.set_3d_properties(data[2, :num])
        return lines


def main():
    q_app = QApplication(sys.argv)
    sil_gui = SilGui()
    sil_gui.setWindowTitle("Squiddrone SiL")
    sil_gui.show()
    sys.exit(q_app.exec())


if __name__ == "__main__":
    main()
