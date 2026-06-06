def sjf(processes):

    import copy
    processes = copy.deepcopy(processes)

    time = 0
    completed = 0
    n = len(processes)

    gantt = []
    is_completed = [False] * n

    while completed < n:

        # Step 1: Find ready processes
        ready_queue = []

        for i in range(n):
            p = processes[i]

            if p.arrival_time <= time and not is_completed[i]:
                ready_queue.append((i, p))

        # Step 2: CPU idle
        if len(ready_queue) == 0:
            next_arrival = min(
                processes[i].arrival_time
                for i in range(n)
                if not is_completed[i]
            )

            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        # Step 3: Pick shortest job
        i, p = min(ready_queue, key=lambda x: x[1].burst_time)

        start = time

        # READY state
        p.state = "READY"

        # RUNNING state
        p.state = "RUNNING"

        # response time
        if p.response_time == -1:
            p.response_time = start - p.arrival_time

        # execute
        time += p.burst_time

        # metrics
        p.completion_time = time
        p.turnaround_time = p.completion_time - p.arrival_time
        p.turn_around_time = p.turnaround_time
        p.waiting_time = p.turnaround_time - p.burst_time

        # TERMINATED state
        p.state = "TERMINATED"

        gantt.append((p.pid, start, time))

        is_completed[i] = True
        completed += 1

    return processes, gantt