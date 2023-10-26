import os
import time
from imagefield import ImageFile
from textfile import TextFile
from programfile import ProgramFile
from basefile import BaseFile

class FolderMonitor:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.snapshot_time = time.time()
        self.files = self.load_files()

    def load_files(self):
        files = {}
        for filename in os.listdir(self.folder_path):
            filepath = os.path.join(self.folder_path, filename)
            if os.path.isfile(filepath):
                ext = os.path.splitext(filename)[1].lower()
                if ext in ['.png', '.jpg']:
                    files[filename] = ImageFile(filepath)
                elif ext == '.txt':
                    files[filename] = TextFile(filepath)
                elif ext in ['.py', '.java']:
                    files[filename] = ProgramFile(filepath)
                else:
                    files[filename] = BaseFile(filepath)
        return files

    def commit(self):
        self.snapshot_time = time.time()
        print("Snapshot updated!")

    def info(self, filename):
        if filename in self.files:
            self.files[filename].info()
        else:
            print(f"File {filename} not found!")

    def status(self):
        for filename, file in self.files.items():
            if file.has_changed(self.snapshot_time):
                print(f"{filename} has changed since the last snapshot.")
            else:
                print(f"{filename} has not changed since the last snapshot.")

    def run(self):
        while True:
            action = input("Enter action (commit, info <filename>, status, or exit): ")
            if action == "commit":
                self.commit()
            elif action.startswith("info "):
                _, filename = action.split(maxsplit=1)
                self.info(filename)
            elif action == "status":
                self.status()
            elif action == "exit":
                break
            else:
                print("Invalid command.")

if __name__ == "__main__":
    monitor = FolderMonitor("C:/Users/user27/Documents/GitHub/OOP-clases/Lab 2/test")
    monitor.run()
# C:\Users\user27\Documents\GitHub\OOP-clases\Lab 2\test\test.txt
