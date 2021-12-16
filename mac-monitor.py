import psutil
import pprint
import time

POLL_PERIOD = 5 # value in seconds on how often to check

def get_cpu_percent():
    """
    Gets the CPU Percent of the system
    """
    print ('CPU Usage: ', psutil.cpu_percent())
    print ('All CPU Cores: ', psutil.cpu_percent(percpu=True))


def get_memory():
    """
    Gets the system memory stats
    """
    print ('Memory: ', psutil.virtual_memory())


def get_load_avg():
    """
    Gets the system load average
    """
    print('Load Average: ', psutil.getloadavg())

def get_process_list_show_cpu():
    """
    Gets a process listing showing the cpu usage
    """
    print ('Process Listing: ')
    for process in psutil.process_iter():
        process_info = process.as_dict(attrs=['name', 'cpu_percent'])
        print(process_info)

while True:
    get_process_list_show_cpu()
    get_cpu_percent()
    get_memory()
    get_load_avg()
    time.sleep(POLL_PERIOD)
