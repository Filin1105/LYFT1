
"""
1.ОКНО+
2 КНОПКИ , НОВЫЙ ФАЙЛ+ СОХРАНЕНИЕ ЦВЕТА КИСТЬ ЛАСТИК ,РАЗМЕР ШРИФТА , ПРЯМОУГОЛЬНИК ELIPSE , 
""" 
import sys
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets  import QApplication, QMainWindow, QWidget, QToolButton,  QPushButton, QColorDialog 
from PyQt5.QtGui import QIcon, QPainter, QPen, QColor, QImage
from PyQt5.QtCore import Qt


class Okno (QMainWindow ):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Пример окна PyQt5")
        self.setGeometry(100, 100, 800, 600)  # Устанавливаем размер и позицию окна
    

        self.canvas = QImage(self.size(),QImage.Format_RGB32)
        self.canvas.fill(Qt.white)
        self.last_point = None
        self.pen = QPen(QColor(0, 0, 0), 2, Qt.SolidLine)  # Правильное определение self.pe
        self.Newfail = QPushButton("", self)
        self.Newfail.clicked.connect(self.clearCanvas)
        self.Newfail.setIcon(QIcon("path_to_icon"))
        self.Newfail.clicked.connect(self.clearCanvas)
        self.Newfail.setGeometry(0, 0, 40, 40)
        self.color_button = QPushButton("", self)
        self.color_button.setIcon(QIcon("цвета"))
        self.color_button.setGeometry(30, 0, 40, 40)
        self.color_button.clicked.connect(self.showColorDialog)
        



    def showColorDialog(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.pen.setColor(color)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.drawImage(self.rect(), self.canvas, self.canvas.rect())
        
    def mousePressEvent(self, event):
         if event.button() == Qt.LeftButton:
            self.last_point = event.pos()   

    def mouseMoveEvent(self, event):
        if event.buttons() and Qt.LeftButton:
            painter = QPainter(self.canvas)
            painter.setPen(self.pen)  # Установка ручки перед рисованием
            painter.drawLine(self.last_point, event.pos())
            self.last_point = event.pos()
            self.update()

    def clearCanvas(self):
             self.canvas.fill(Qt.white)
             self.update()

        
    def NewfailS(self):
        self.canvas.fill(Qt.white)
        self.update()



def main():
        app = QApplication(sys.argv)
        window = Okno()
        window.show()
        sys.exit(app.exec_())
    
if __name__ == "__main__":
    main()

