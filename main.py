import os

import datetime

def save_debug_log(event):
    date = datetime.datetime.now()
    event = (str(date) + " - " + str(event))
    debug = open(debug_file_path, 'a+')
    debug.write(str(event) + "\n")
    debug.close()

def print_debug_log(debug_file_path):
    debug = open(debug_file_path, 'r')
    debug_content = debug.readlines()
    debug.close()

    for line in debug_content:
        print(line)

class config():

    config_file = None

    def __init__(self, config):
        self.config_file_path = config
        self.reload_config()

    def reload_config(self):
        try:
           self.config_file = open(self.config_file_path,'r')
           config_data = self.config_file.read()

        except IOError as e:
            save_debug_log(e)
        except Exception as e:
            save_debug_log(e)
            self.config_file.close()


#Load config from file

config_file_path = "my-daily-tasks-timer.conf"
debug_file_path = "my-daily-tasks-timer_debug.txt"

if not os.path.isfile(debug_file_path):
    print("Plik debug nie istnieje!")

myconfig = config(config_file_path)
#myconfig.reload_config()

print_debug_log(debug_file_path)