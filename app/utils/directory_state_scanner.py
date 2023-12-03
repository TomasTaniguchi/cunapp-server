import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

class DirScannerHandler(FileSystemEventHandler):
    
    def on_created(self, event):
        print("New script added")
    def on_deleted(self, event):
        print("some script deleted")


path="../scripts"
event_handler = DirScannerHandler()
observer = Observer()
observer.schedule(event_handler,path, recursive=False)
observer.start()

try:
    while True:
        time.sleep(1)
finally:
    observer.stop()
    observer.join()
