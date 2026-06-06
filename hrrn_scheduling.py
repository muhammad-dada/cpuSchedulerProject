def hrrn_scheduling(processes):

    import copy
    processes = copy.deepcopy(processes)

    n = len(processes)
    time = 0
    completed = 0

    completed_flag = [False] * n
    gantt = []

    while completed < n:

        ready = []

        for i in range(n):
            if processes[i].arrival_time <= time and not completed_flag[i]:
                ready.append(i)

        # CPU idle
        if not ready:
            time += 1
            continue

        # Response Ratio formula
        def response_ratio(i):
            p = processes[i]
            waiting_time = time - p.arrival_time
            return (waiting_time + p.burst_time) / p.burst_time

        # Pick highest ratio
        current = max(ready, key=response_ratio)
        p = processes[current]

        start_time = time

        # READY state
        p.state = "READY"

        # RUNNING state
        p.state = "RUNNING"

        # Response time
        if p.response_time == -1:
            p.response_time = start_time - p.arrival_time

        # Execute fully (non-preemptive)
        time += p.burst_time

        # Completion
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.turn_around_time = p.turnaround_time
        p.waiting_time = p.turnaround_time - p.burst_time

        # TERMINATED state
        p.state = "TERMINATED"

        gantt.append((p.pid, start_time, time))

        completed_flag[current] = True
        completed += 1

    return processes, gantt