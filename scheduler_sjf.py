def sjf(processes):

    processes = processes

    time = 0
    completed = 0
    n = len(processes)

    gantt = []
    is_completed = [False] * n

    while completed < n:

        # Step 1: Find all arrived processes
        ready_queue = []

        for i in range(n):
            p = processes[i]

            if p.arrival_time <= time and not is_completed[i]:
                ready_queue.append((i, p))

        # Step 2: if no process is ready -> CPU idle
        if len(ready_queue) == 0:
            next_arrival = min(
                p.arrival_time for i, p in enumerate(processes) if not is_completed[i]
            )
            gantt.append(("IDLE", time, next_arrival))
            time = next_arrival
            continue

        # pick shortest job
        i, p = ready_queue[0]

        for item in ready_queue:
            if item[1].burst_time < p.burst_time:
                i, p = item

        start = time

        # response time
        if p.response_time == -1:
            p.response_time = start - p.arrival_time

        time += p.burst_time

        p.completion_time = time
        p.turnaround_time = time - p.arrival_time
        p.waiting_time = p.turnaround_time - p.burst_time

        gantt.append((p.pid, start, time))

        is_completed[i] = True
        completed += 1
        
    return gantt
