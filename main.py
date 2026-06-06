from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLineEdit,
    QComboBox,
    QTableWidget,
    QTableWidgetItem,
)
import sys

from scheduler_fcfs import fcfs
from scheduler_sjf import sjf
from round_robin import round_robin
from priority_scheduling import priority_scheduling
from hrrn_scheduling import hrrn_scheduling
from process import Process
from round_robin import round_robin
from gantt_window import GanttChart


class CPUSchedulerUI(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("CPU Scheduling Simulator")
        self.resize(1000, 600)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.processes = []
        self.gantt_window = None  # ✅ FIX: avoid crash on reset/run

        self.build_input_ui()
        self.build_output_table()

        # optional UI styling
        self.setStyleSheet("""
            QWidget {
                background-color: #f4f6f7;
                font-family: Arial;
                font-size: 13px;
                color: #1a1a1a;
            }

            QLineEdit {
                background-color: #ffffff;
                color: #1a1a1a;
                padding: 6px;
                border: 1px solid #b0b0b0;
                border-radius: 5px;
            }

            QLineEdit::placeholder {
                color: #6f6f6f;
            }

            QPushButton {
                background-color: #3498db;
                color: white;
                padding: 6px;
                border-radius: 5px;
            }

            QPushButton:hover {
                background-color: #2980b9;
            }

            QComboBox {
                background-color: #ffffff;
                color: #1a1a1a;
                padding: 5px;
                border: 1px solid #b0b0b0;
                border-radius: 5px;
            }

            QComboBox QAbstractItemView {
                background-color: #ffffff;
                color: #1a1a1a;
                selection-background-color: #d6eaf8;
                selection-color: #000000;
            }

            QTableWidget {
                font-size: 14px;
                color: #1a1a1a;
                gridline-color: #ccc;
            }

            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 5px;
            }
        """)

    # ---------------- INPUT UI ----------------
    def build_input_ui(self):

        input_layout = QHBoxLayout()

        self.pid_input = QLineEdit()
        self.pid_input.setPlaceholderText("Process ID")

        self.at_input = QLineEdit()
        self.at_input.setPlaceholderText("Arrival Time")

        self.bt_input = QLineEdit()
        self.bt_input.setPlaceholderText("Burst Time")

        self.add_btn = QPushButton("Add Process")
        self.add_btn.clicked.connect(self.add_process)

        self.algo_box = QComboBox()
        self.algo_box.addItems(["FCFS", "SJF", "Round Robin", "Priority", "HRRN"])
        self.run_btn = QPushButton("Run Scheduler")
        self.run_btn.clicked.connect(self.run_scheduler)

        self.reset_btn = QPushButton("Reset")
        self.reset_btn.clicked.connect(self.reset_all)

        input_layout.addWidget(self.pid_input)
        input_layout.addWidget(self.at_input)
        input_layout.addWidget(self.bt_input)
        input_layout.addWidget(self.add_btn)
        input_layout.addWidget(self.algo_box)
        input_layout.addWidget(self.run_btn)
        input_layout.addWidget(self.reset_btn)

        self.layout.addLayout(input_layout)

    # ---------------- TABLE ----------------
    def build_output_table(self):

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(
            ["PID", "Waiting Time", "Turnaround Time", "Response Time"]
        )

        self.table.setStyleSheet("""
            QTableWidget {
                font-size: 14px;
                gridline-color: #ccc;
            }
            QHeaderView::section {
                background-color: #2c3e50;
                color: white;
                padding: 5px;
            }
        """)

        self.layout.addWidget(self.table)  # ✅ FIX: table was not added

    # ---------------- ADD PROCESS ----------------
    def add_process(self):

        pid = self.pid_input.text().strip()

        if not pid:
            return

        try:
            at = int(self.at_input.text())
            bt = int(self.bt_input.text())
        except:
            return

        self.processes.append(Process(pid, at, bt))

        self.pid_input.clear()
        self.at_input.clear()
        self.bt_input.clear()

    # ---------------- RESET ----------------
    def reset_all(self):

        self.processes = []
        self.table.setRowCount(0)

        if self.gantt_window:
            self.gantt_window.close()
            self.gantt_window = None

    # ---------------- RUN SCHEDULER ----------------
    def run_scheduler(self):

        if len(self.processes) == 0:
            return

        algo = self.algo_box.currentText()

        processes_copy = [
            Process(p.pid, p.arrival_time, p.burst_time) for p in self.processes
        ]

        if algo == "FCFS":
            processes_copy, gantt = fcfs(processes_copy)

        elif algo == "SJF":
            processes_copy, gantt = sjf(processes_copy)

        elif algo == "Round Robin":
            processes_copy, gantt = round_robin(processes_copy, quantum=2)

        elif algo == "Priority":
            processes_copy, gantt = priority_scheduling(processes_copy)

        elif algo == "HRRN":
            processes_copy, gantt = hrrn_scheduling(processes_copy)

        else:
            return

        # close previous gantt window
        if self.gantt_window:
            self.gantt_window.close()

        self.gantt_window = GanttChart(gantt)
        self.gantt_window.show()

        # update table
        self.table.setRowCount(len(processes_copy))

        for i, p in enumerate(processes_copy):
            self.table.setItem(i, 0, QTableWidgetItem(p.pid))
            self.table.setItem(i, 1, QTableWidgetItem(str(p.waiting_time)))
            self.table.setItem(i, 2, QTableWidgetItem(str(p.turnaround_time)))
            self.table.setItem(i, 3, QTableWidgetItem(str(p.response_time)))


# ---------------- RUN APP ----------------
app = QApplication(sys.argv)

window = CPUSchedulerUI()

window.show()

sys.exit(app.exec())
