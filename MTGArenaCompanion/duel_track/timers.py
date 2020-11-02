from threading import Thread
from time import time, sleep

WIN_TITLE = 'Duel Tracker'


class TimerHistory(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.ledger = []

    def add(self, run_time):
        pass

    def write(self):
        pass

    def run(self):
        pass


def format_seconds_to_hhmmss(seconds):
    hours = seconds // (60 * 60)
    seconds %= (60 * 60)
    minutes = seconds // 60
    seconds %= 60
    return "%02i:%02i:%02i" % (hours, minutes, seconds)


class Timer(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.start_time = None
        self.is_running = False
        self.pause_start = time()
        self.pause_end = None
        self.total_pause_time = 0
        self.started = False
        self.paused = False
        self.was_paused = False
        self.mark_2 = None

    def get_elapsed(self, only_formatted=False, only_float=False, round_float=True):
        self.mark_2 = time()
        #print(self.mark_2)
        #print(self.start_time)

        diff = self.mark_2 - self.start_time
        #print(format_seconds_to_hhmmss(diff))

        print(self.total_pause_time)
        diff = diff - self.total_pause_time
        return format_seconds_to_hhmmss(diff)

    def reset(self):
        pass

    def run(self):
        self.start_time = time()
        self.started = True

    def pause(self):
        if not self.paused:
            self.pause_start = time()
            self.paused = True
        else:
            return False

    def unpause(self):
        if self.paused:
            self.pause_end = time()
            diff = self.pause_end - self.pause_start
            self.total_pause_time += diff
            self.paused = False
        else:
            return False
