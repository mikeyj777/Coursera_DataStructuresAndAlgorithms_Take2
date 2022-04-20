from datetime import datetime as dt

class Log:
    
    def __init__(self, time = "", IP = ""):
        
        self.time = time
        self.IP = IP

class service_access:
    
    log = Log()

    def __init__(self):
        pass

    def main_loop(self, i = 0, j = 0, C = {}):
        a = self.update_access_list(i, j, C)

    def update_access_list(self, i, j, C):

        now = dt.now() #convert to seconds

        while self.log[i].time <= now:
            C[self.log[i].IP] += 1
            i += 1

        while self.log[i].time <= now - 3600:
            C[self.log[j].IP] -= 1
            j += 1
 

    def accessed_last_hour(self, IP):
        return self.C[IP] > 0