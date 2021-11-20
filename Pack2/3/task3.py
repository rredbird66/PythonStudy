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

    def log(self, level, Msg):
        str_to_log = '[{}] {}: {}'.format(level.name, datetime.datetime.now().time(), Msg) + '\n'
        self.filedescr.write(str_to_log)

if __name__ == "__main__":

    logger = Logger("out.log")

    logger.log(logLevel.DEBUG, "Log msg 1")
    logger.log(logLevel.ERROR, "Log msg 2")  
    logger.log(logLevel.WARNING, "Log msg 3")
    logger.log(logLevel.INFO, "Log msg 4")

    same_log = Logger()
    same_log.log(logLevel.DEBUG, "Log msg 5")
    same_log.log(logLevel.ERROR, "Log msg 6")  
    same_log.log(logLevel.WARNING, "Log msg 7")
    same_log.log(logLevel.INFO, "Log msg 8")
 
