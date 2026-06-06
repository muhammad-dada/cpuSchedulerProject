from process import Process
from round_robin import round_robin
from scheduler_fcfs import fcfs
from priority_scheduling import priority_scheduling
from hrrn_scheduling import hrrn_scheduling

processes = [
    Process("P1", 2, 5, 2),
    Process("P2", 3, 4, 1),
    Process("P3", 3, 4, 3),
    Process("P4", 4, 1, 2),
]

result, gantt = hrrn_scheduling(processes)

print("Gantt Chart:")
for g in gantt:
    print(g)

print("\nProcess Metrics")
for p in result:
    print(
        p.pid,
        "WT:",p.waiting_time,
        "TAT:",p.turn_around_time,
        "RT:",p.response_time,
    )
