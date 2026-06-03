from process import Process
from scheduler_sjf import sjf

from PyQt6.QtWidgets import QApplication
from gantt_window import GanttChart
import sys

processes = [
    Process("P1", 0, 8),
    Process("P2", 1, 4),
    Process("P3", 2, 2),
    Process("P4", 3, 1),
]

gantt = sjf(processes)

app = QApplication(sys.argv)

window = GanttChart(gantt)
window.show()

sys.exit(app.exec())
