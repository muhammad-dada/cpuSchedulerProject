from process import Process
from scheduler_sjf import sjf

processes = [
    Process("P1", 0, 8),
    Process("P2", 1, 4),
    Process("P3", 2, 2),
    Process("P4", 3, 1),
]

gantt = sjf(processes)

print("Gantt Chart:")
for g in gantt:
    print(g)

print("\nProcess Metrics:")

for p in processes:
    print(
        p.pid, "WT:", p.waiting_time, "TAT:", p.turnaround_time, "RT:", p.response_time
    )
