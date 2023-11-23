import os
import shutil
import time
from gui import data

main = True
startup = False
run = False

while main:

    desktopPath = "/Users/asmusaskovbaunstrup/Desktop"
    desktopFiles = os.listdir(desktopPath)

    foldersInDesktop = [item for item in desktopFiles if os.path.isdir(os.path.join(desktopPath, item))]

    print("\nAll folders on the desktop:", foldersInDesktop)

    startup = True
    while startup:

        folderNameGUI = data.get('folderName', '')
        fileTypeGUI = data.get('fileType', '')

        print(f"\nName of folder: {folderNameGUI}")
        print(f"File type: {fileTypeGUI}")
        
        if folderNameGUI in desktopFiles:
            destination = os.path.join(desktopPath, folderNameGUI)

            fileType = fileTypeGUI

            # if not fileType.startswith("."):
            #     fileType = "." + fileType

            print(f"\nMoving all {fileType} to {folderNameGUI}\n")
            startup = False
        
        else:
            print("Folder not found")

    run = True
    while run:

        desktopFiles = os.listdir(desktopPath)
        pngFiles = [file for file in desktopFiles if file.endswith(fileTypeGUI)]

        if pngFiles:

            print(f"\nFound the following {fileTypeGUI} files on the desktop:")

            for i in pngFiles:
                print(i)

            print(f"\nMoving the file(s) to {destination}\n")

            for pngFile in pngFiles:
                source = os.path.join(desktopPath, pngFile)

                shutil.move(source, destination)
                print(f"Successfully moved {pngFile} to {destination}\n")

        time.sleep(2)

    if input("Type 'exit' to stop the program: ").lower() == "exit":
        main = False