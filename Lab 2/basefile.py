import os
from datetime import datetime

class BaseFile:
    def __init__(self, filepath):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.creation_time = os.path.getctime(filepath)
        self.modification_time = os.path.getmtime(filepath)

    def info(self):
        print(f"Filename: {self.filename}")
        print(f"Extension: {os.path.splitext(self.filename)[1]}")
        print(f"Created at: {datetime.fromtimestamp(self.creation_time)}")
        print(f"Last modified at: {datetime.fromtimestamp(self.modification_time)}")

    def has_changed(self, snapshot_time):
        return self.modification_time > snapshot_time