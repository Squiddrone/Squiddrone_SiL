
import sys
from PyQt5.QtWidgets import QApplication, QDialog
import gui


class SilGui(QDialog):
    def __init__(self, parent=None):
        super(SilGui, self).__init__(parent)
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)
        self.plot()

    def plot(self):
        x = range(0, 10)
        y = range(0, 20, 2)
        self.ui.graphWidget.canvas.ax.plot(x, y)


def main():
    q_app = QApplication(sys.argv)
    sil_gui = SilGui()
    sil_gui.setWindowTitle("Squiddrone SiL")
    sil_gui.show()
    sys.exit(q_app.exec())


if __name__ == "__main__":
    main()
