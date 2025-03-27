"""
3_Encapsulation.py

This file demonstrates the concept of encapsulation in Python.
It explains how to use private attributes and controlled access methods.
The example also incorporates the `enum` module to manage log levels efficiently.
"""

from enum import Enum
from datetime import datetime

class LogLevel(Enum):
    """
    Enum for defining different levels of logging.
    """
    INFO = "INFO"
    WARNING = "WARNING"
    ERROR = "ERROR"
    DEBUG = "DEBUG"

class Logger:
    """
    A simple logging system demonstrating encapsulation.
    """
    def __init__(self):
        # Private attribute to store logs
        self.__logs = []

    def add_log(self, level: LogLevel, message: str):
        """
        Adds a log entry with a specified log level.
        
        :param level: The log level (INFO, WARNING, ERROR, DEBUG)
        :param message: The log message
        """
        log_entry = f"{datetime.now()} - {level.value}: {message}"
        self.__logs.append(log_entry)

    def get_logs(self):
        """
        Provides a copy of logs to prevent direct modification.
        
        :return: List of log entries
        """
        return self.__logs.copy()

    def clear_logs(self):
        """
        Clears the log history.
        """
        self.__logs.clear()

# Usage Example
logger = Logger()
logger.add_log(LogLevel.INFO, "System started.")
logger.add_log(LogLevel.WARNING, "Low disk space.")
logger.add_log(LogLevel.ERROR, "File not found.")

# Accessing logs (encapsulated, so direct modification is not allowed)
for log in logger.get_logs():
    print(log)

# Expected Output (Varies based on execution time)
# 2025-03-21 12:30:00 - INFO: System started.
# 2025-03-21 12:30:05 - WARNING: Low disk space.
# 2025-03-21 12:30:10 - ERROR: File not found.
