class main_screen():

    options = {
            '1': 'new_task',
            '2': 'todays_tasks',
            '3': 'show_entire_history'
    }

    def __init__(self, task):
        self.task = task
        self.current_option = None

    def print_current_task(self):
        if self.task.task_start_time:
            print("Current task: %s" % self.task.task_name)

    def print_options(self):
        for k,v in self.options.items():
            print("%s : %s" % (k,v))

    def read_option(self):
        while True:
            print("Select option: ", end='')
            self.current_option = input()
            if self.validate_option():
                if self.current_option == "1":

                    #of task has start time then stop it first
                    if self.task.task_start_time:
                        self.task.stop_task()

                    self.task.__init__()
                    self.task.set_task_name()
                    self.task.start_task()

                break

    def validate_option(self):
        if self.current_option in self.options:
            validated_status= True
        else:
            validated_status= False
        return validated_status
