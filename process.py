class Process:
    def __init__(self, pid, arrival_time, burst_time, priority=0):
        # Input values
        self.pid = pid
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority

        # Runtime Values
        self.remaining_time = burst_time
        self.completion_time = 0
        self.waiting_time = 0
        self.turn_around_time = 0
        self.response_time = -1

        # For debugging / tracking
        self.started = False

    def __str__(self):
        return f"{self.pid} (AT={self.arrival_time}, BT={self.burst_time}, PR={self.priority})"
