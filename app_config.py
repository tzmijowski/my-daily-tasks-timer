import os
import datetime

class config():

    config_file = None

    def __init__(self, config, debug):
        self.config_file_path = config
        self.debug_file_path = debug
        self.reload_config()

    def save_debug_log(event):
        date = datetime.datetime.now()
        event = (str(date) + " - " + str(event))
        debug = open(self.debug_file_path, 'a+')
        debug.write(str(event) + "\n")
        debug.close()

    def print_debug_log(debug_file_path):
        debug = open(debug_file_path, 'r')
        debug_content = debug.readlines()
        debug.close()

        for line in debug_content:
            print(line)

    def reload_config(self):
        try:
           self.config_file = open(self.config_file_path,'r')
           config_data = self.config_file.read()

        except IOError as e:
            self.save_debug_log(e)
        except Exception as e:
            self.save_debug_log(e)
            self.config_file.close()