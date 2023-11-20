import io
import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QRectF


class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        self.do_paint = False
        uic.loadUi('UI.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.paint_round(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def paint_round(self, qp):
        qp.setPen(QColor(255, 255, 0))
        qp.setBrush(QColor(255, 255, 0))
        for i in range(randint(4, 30)):
            self.dim = randint(20, 100)
            qp.drawEllipse(randint(50, 500), randint(50, 500), self.dim, self.dim)
        self.do_paint = False


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = Square1()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
