def sort_by_arrival(processes):
    n = len(processes)

    for i in range(n):
        swapped = False

        for j in range(n - i - 1):
            if processes[j].arrival_time > processes[j + 1].arrival_time:
                processes[j], processes[j + 1] = processes[j + 1], processes[j]
                swapped = True

        if not swapped:
            break


def fcfs(processes):

    sort_by_arrival(processes)

    time = 0
    gantt = []

    for p in processes:

        # CPU idle
        if time < p.arrival_time:
            gantt.append(("IDLE", time, p.arrival_time))
            time = p.arrival_time

        # READY state (process is now in queue and selected)
        p.state = "READY"

        start_time = time

        # RUNNING state
        p.state = "RUNNING"

        # response time
        p.response_time = start_time - p.arrival_time

        time += p.burst_time

        p.completion_time = time

        # TERMINATED state
        p.state = "TERMINATED"

        # metrics
        p.turnaround_time = p.completion_time - p.arrival_time
        p.turn_around_time = p.turnaround_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, start_time, time))

    return processes, gantt