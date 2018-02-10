import os
import datetime

from app_config import config
from main_screen import main_screen
from new_task import new_task





#Load config from file

config_file_path = "my-daily-tasks-timer.conf"
debug_file_path = "my-daily-tasks-timer_debug.txt"

if not os.path.isfile(debug_file_path):
    print("Plik debug nie istnieje!")

myconfig = config(config_file_path, debug_file_path)
#myconfig.reload_config()
#print_debug_log(debug_file_path)

#------------------

#initialize new task
t1 = new_task()

#initirialize main screen
ms = main_screen(t1)

while True:
    ms.print_current_task()
    ms.print_options()
    ms.read_option()



