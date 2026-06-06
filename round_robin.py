def round_robin(processes, quantum):

    import copy
    processes = copy.deepcopy(processes)

    n = len(processes)

    remaining_bt = [p.burst_time for p in processes]
    completion_time = [0] * n

    ready_queue = []
    gantt = []

    time = 0
    completed = 0
    arrived = [False] * n

    while completed < n:

        # Add newly arrived processes
        for i in range(n):
            if processes[i].arrival_time <= time and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        # CPU idle
        if not ready_queue:
            time += 1
            continue

        current = ready_queue.pop(0)
        p = processes[current]

        start_time = time

        # READY state
        if p.state != "RUNNING":
            p.state = "READY"

        # RUNNING state
        p.state = "RUNNING"

        # response time (first time only)
        if p.response_time == -1:
            p.response_time = time - p.arrival_time

        execute = min(quantum, remaining_bt[current])

        gantt.append((p.pid, time, time + execute))

        time += execute
        remaining_bt[current] -= execute

        # Add newly arrived processes during execution
        for i in range(n):
            if processes[i].arrival_time <= time and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        # If still not finished → back to READY queue
        if remaining_bt[current] > 0:
            ready_queue.append(current)
            p.state = "READY"
        else:
            completion_time[current] = time

            # TERMINATED state
            p.state = "TERMINATED"

            p.completion_time = time
            p.turnaround_time = time - p.arrival_time
            p.turn_around_time = p.turnaround_time
            p.waiting_time = p.turnaround_time - p.burst_time

            completed += 1

    return processes, gantt