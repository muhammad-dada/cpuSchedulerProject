from PyQt6.QtWidgets import QApplication, QWidget
from PyQt6.QtGui import QPainter
from PyQt6.QtCore import Qt
import sys


class GanttChart(QWidget):

    def __init__(self, gantt):
        super().__init__()

        self.gantt = gantt

        self.setWindowTitle("CPU Scheduling SImulator")
        self.resize(900, 250)

    def paintEvent(self, event):

        painter = QPainter(self)

        x = 50
        y = 80
        height = 60
        scale = 40  # pixels per time unit

        for pid, start, end in self.gantt:

            width = (end - start) * scale

            painter.drawRect(x, y, width, height)

            painter.drawText(x + width // 2 - 10, y + 35, pid)

            painter.drawText(x, y + 80, str(start))

            x += width

        painter.drawText(x, y + 80, str(self.gantt[-1][2]))
