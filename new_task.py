import datetime

class new_task():
    def __init__(self):
        self.task_name = None
        self.task_start_time = None
        self.task_stop_time = None


    def set_task_name(self):
        print("Task name (ID/SD/INC/C): ", end='')
        self.task_name = input()

    def start_task(self):
        self.task_start_time = datetime.datetime.now()
        print("New task %s has started: %s" % (self.task_name, self.task_start_time))

    def stop_task(self):
        self.task_stop_time = datetime.datetime.now()
        print("Task %s has stopped: %s" % (self.task_name, self.task_start_time))