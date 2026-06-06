def process_queue_model(processes):

    import copy
    processes = copy.deepcopy(processes)

    n = len(processes)

    time = 0
    arrived = [False] * n

    ready_queue = []
    completed = 0
    gantt = []
    completed_list = []

    while completed < n:

        # STEP 1: Fill ready queue
        for i in range(n):
            if processes[i].arrival_time <= time and not arrived[i]:
                ready_queue.append(i)
                arrived[i] = True

        # STEP 2: CPU idle
        if not ready_queue:
            time += 1
            continue

        # STEP 3: Take from ready queue
        current = ready_queue.pop(0)
        p = processes[current]

        start = time

        p.state = "RUNNING"

        if p.response_time == -1:
            p.response_time = time - p.arrival_time

        time += p.burst_time

        p.completion_time = time
        p.turnaround_time = time - p.arrival_time
        p.turn_around_time = p.turnaround_time
        p.waiting_time = p.turnaround_time - p.burst_time

        p.state = "TERMINATED"

        gantt.append((p.pid, start, time))

        completed.append(p)
        completed_list.append(p)
        completed += 1

    return processes, gantt, completed_list