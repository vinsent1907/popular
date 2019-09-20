import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':

    app = QApplication(sys.argv)

    w = QWidget()
    w.resize(600, 600)
    w.move(200, 200)
    w.setWindowTitle('Pavel')
    w.show()

    sys.exit(app.exec_())
