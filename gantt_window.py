from PyQt6.QtWidgets import QWidget
from PyQt6.QtGui import QPainter, QColor, QPen, QFont
from PyQt6.QtCore import Qt


class GanttChart(QWidget):

    def __init__(self, gantt):
        super().__init__()

        self.gantt = gantt

        self.setWindowTitle("Gantt Chart Viewer")
        self.resize(1000, 250)

        # color palette
        self.colors = [
            "#4FC3F7", "#81C784", "#FFB74D", "#E57373",
            "#BA68C8", "#4DB6AC", "#FFD54F", "#90A4AE"
        ]

    def paintEvent(self, event):

        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)

        x = 50
        y = 80
        height = 60
        scale = 30  # pixels per unit time

        font = QFont("Arial", 10)
        painter.setFont(font)

        # ---------------- DRAW BLOCKS ----------------
        for i, item in enumerate(self.gantt):
            pid, start, end = item
            width = (end - start) * scale

            color = self.colors[i % len(self.colors)]

            painter.setBrush(QColor(color))
            painter.setPen(QPen(Qt.GlobalColor.black))

            # draw process block
            painter.drawRect(x, y, width, height)

            # process ID (centered)
            painter.drawText(
                x,
                y,
                width,
                height,
                Qt.AlignmentFlag.AlignCenter,
                str(pid)
            )

            # time range (below block)
            painter.drawText(
                x,
                y + height + 15,
                width,
                20,
                Qt.AlignmentFlag.AlignCenter,
                f"{start} - {end}"
            )

            x += width

        # ---------------- TIMELINE ----------------
        painter.setPen(QPen(Qt.GlobalColor.black))

        line_y = y + height + 30
        painter.drawLine(50, line_y, x, line_y)

        current_x = 50

        for item in self.gantt:
            _, start, end = item
            width = (end - start) * scale

            painter.drawText(current_x, line_y + 20, str(start))
            current_x += width

        # last endpoint
        if self.gantt:
            painter.drawText(current_x, line_y + 20, str(self.gantt[-1][2]))

        painter.end()