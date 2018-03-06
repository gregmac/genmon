# PURPOSE: manage threads
#
#  AUTHOR: Jason G Yates
#    DATE: 04-Mar-2017
#
# MODIFICATIONS:
#------------------------------------------------------------

import threading

# ---------- MyThread--------------------------------
class MyThread():
    #Thread class with a stop() method. The thread itself has to check
    # regularly for the stopped() condition.

    # ---------- MyThread::MyThread------------------
    def __init__(self, ThreadFunction, Name = None):
        self.StopEvent = threading.Event()
        self.ThreadObj = threading.Thread(target = ThreadFunction, name = Name)
        self.ThreadObj.daemon = True
        self.ThreadObj.start()       # start thread

    # ---------- MyThread::Stop------------------
    def GetThreadObject(self):
        return self.ThreadObj

    # ---------- MyThread::Stop------------------
    def Stop(self):
        self.StopEvent.set()

    # ---------- MyThread::StopSignaled------------------
    def StopSignaled(self):
        return self.StopEvent.is_set()

    # ---------- MyThread::IsAlive------------------
    def IsAlive(self):
        return self.ThreadObj.is_alive()

    # ---------- MyThread::Name------------------
    def Name(self):
        return self.ThreadObj.name

    # ---------- MyThread::Name------------------
    def WaitForThreadToEnd(self, Timeout = None):
        return self.ThreadObj.join(Timeout)

