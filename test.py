from process import Process
from scheduler_fcfs import fcfs

processes = [
    Process("P1", 2, 5,),
    Process("P2", 3, 4,),
    Process("P3", 3, 4,),
    Process("P4", 4, 1,),
]

gantt = fcfs(processes)

print("Gantt Chart:")
for g in gantt:
    print(g)

print("\nProcess Metrics")
for p in processes:
    print(
        p.pid,
        "WT:",p.waiting_time,
        "TAT:",p.turn_around_time,
        "RT:",p.response_time,
    )
