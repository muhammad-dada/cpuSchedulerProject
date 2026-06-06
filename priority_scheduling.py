def priority_scheduling(processes):

    import copy
    processes = copy.deepcopy(processes)

    n = len(processes)
    time = 0
    completed = 0
    completed_flag = [False] * n

    gantt = []

    while completed < n:

        # Find ready processes
        ready = []

        for i in range(n):
            if processes[i].arrival_time <= time and not completed_flag[i]:
                ready.append(i)

        # CPU idle case
        if not ready:
            time += 1
            continue

        # Pick highest priority (LOWER number = higher priority)
        current = min(ready, key=lambda i: processes[i].priority)

        p = processes[current]

        start_time = time

        # Response time (first execution only)
        if p.response_time == -1:
            p.response_time = start_time - p.arrival_time

        # Execute fully (non-preemptive)
        time += p.burst_time

        # Completion time
        p.completion_time = time

        # Turnaround time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.turn_around_time = p.turnaround_time  # backward compatibility

        # Waiting time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, start_time, time))

        completed_flag[current] = True
        completed += 1

    return processes, gantt