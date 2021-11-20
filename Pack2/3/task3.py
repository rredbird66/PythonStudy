#! /usr/bin/python3

import datetime
from enum import Enum

class logLevel(Enum):
    TRACE = 0
    DEBUG = 1
    INFO = 2
    WARNING = 3
    ERROR = 4
    CRITICAL = 5

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]
     
class Logger(metaclass=Singleton):

    def __init__(self, filename):
        self.filename = filename
        self.filedescr = open(filename, "w")
    def __del__(self):
        self.filedescr.close()

    def flush(self):
        self.filedescr.flush()

    def Debug(self, Msg):
        str_to_log = '[{}] {}: {}'.format(logLevel.DEBUG.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)

    def Info(self, Msg):
        str_to_log = '[{}] {}: {}'.format(logLevel.INFO.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)
    
    def Warning(self, Msg):
        str_to_log = '[{}] {}: {}'.format(logLevel.WARNING.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)

    def Error(self, Msg):
        str_to_log = '[{}] {}: {}'.format(logLevel.ERROR.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)
        self.filedescr.flush()

    def Critical(self, Msg):
        str_to_log = '[{}] {}: {}'.format(logLevel.CRITICAL.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)
        self.filedescr.flush()

if __name__ == "__main__":

    logger = Logger("out.log")

    logger.Info("Log msg 1")
    logger.Debug("Log msg 2")  
    logger.Error("Log msg 3")
    logger.Warning("Log msg 4")

    same_log = Logger()

    same_log.Debug("Log msg 9")
    same_log.Error("Log msg 10")  
    same_log.Warning("Log msg 11")
    same_log.Info("Log msg 12")


