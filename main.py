
import sys
from PyQt6.QtWidgets import QApplication, QDialog
import gui


class SilGui(QDialog):
    def __init__(self, parent=None):
        super(SilGui, self).__init__(parent)
        self.ui = gui.Ui_Dialog()
        self.ui.setupUi(self)


def main():
    q_app = QApplication(sys.argv)
    sil_gui = SilGui()
    sil_gui.setWindowTitle("Squiddrone SiL")
    sil_gui.show()
    sys.exit(q_app.exec())


if __name__ == "__main__":
    main()
