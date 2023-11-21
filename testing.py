import os
import shutil
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        if event.src_path.endswith('.png'):
            move_file(event.src_path)

def move_file(source):
    destination = os.path.join(desktopPath, "PhotosTestFolder")
    shutil.move(source, destination)
    print(f"Successfully moved {os.path.basename(source)} to {destination}")

if __name__ == "__main__":
    desktopPath = "/Users/asmusaskovbaunstrup/Desktop"
    print(desktopPath)

    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, desktopPath, recursive=False)
    observer.start()

    try:
        print("Watching for changes on the desktop...")
        while True:
            pass
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
