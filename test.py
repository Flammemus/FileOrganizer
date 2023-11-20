import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

file_type_to_folder = {
    '.txt': 'TextFiles',
    '.jpg': 'ImageFiles',
    '.pdf': 'PDFFiles'
}

folders_to_check = ['Desktop']


user = str(os.path.expanduser("~"))
folders_to_check = [f"{user}/{folder}" for folder in folders_to_check]

for folder in file_type_to_folder.values():
    os.makedirs(user+f"/Desktop/{folder}", exist_ok=True)
# List of folders to be checked

print(folders_to_check)
file_type_to_folder = {t: f"{user}/Desktop/{folder}" for t, folder in file_type_to_folder.items()}

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        file_path = event.src_path
        file_name, file_extension = os.path.splitext(file_path)

        if file_extension.lower() in file_type_to_folder:
            destination_folder = file_type_to_folder[file_extension.lower()]
            destination_path = os.path.join(destination_folder, os.path.basename(file_path))

            # Move the file to the destination folder
            os.rename(file_path, destination_path)
            print(f"Moved {file_path} to {destination_path}")

def start_file_monitoring():
    event_handler = MyHandler()
    observer = Observer()

    # Set up the observer to watch for created events
    for folder in folders_to_check:
        folder_path = os.path.abspath(folder)
        observer.schedule(event_handler, folder_path, recursive=False)

    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

if __name__ == "__main__":
    # Create destination folders if they don't exist
    for folder in folders_to_check:
        if not os.path.exists(folder):
            os.makedirs(folder)

    # Start monitoring for file creation events
    start_file_monitoring()
