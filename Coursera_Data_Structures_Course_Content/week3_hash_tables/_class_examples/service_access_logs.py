from datetime import datetime as dt

class Log:
    
    def __init__(self, time = "", IP = ""):
        
        self.time = time
        self.IP = IP

def main_loop(log = '', i = 0, j = 0, C = {}):
    a = update_access_list(log, i, j, C)

def update_access_list(log, i, j, C):

    while log[i].time <= dt.now():
        C[log[i].IP] += 1
        i += 1

    while log[i].time <= dt.now() - 3600:
        C[log[j].IP] -= 1
        j += 1
    
    return None