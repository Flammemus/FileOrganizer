import os
import shutil
import time

main = True
startup = False
run = False

while main:

    desktopPath = "/Users/asmusaskovbaunstrup/Desktop"
    desktopFiles = os.listdir(desktopPath)

    foldersInDesktop = [item for item in desktopFiles if os.path.isdir(os.path.join(desktopPath, item))]

    print("@*===============================*@")

    print("\nAll folders on the desktop:")
    for i in foldersInDesktop:
        print("* " + i)

    startup = True
    while startup:

        folderName = input("\nName of folder: ")
        
        if folderName in desktopFiles:
            destination = os.path.join(desktopPath, folderName)

            fileType = input("Filetype you want to move ( .png .txt etc ): ")

            if not fileType.startswith("."):
                fileType = "." + fileType

            print(f"\nMoving all {fileType} to {folderName}\n")
            startup = False
        
        else:
            print("Folder not found")

    run = True
    while run:

        desktopFiles = os.listdir(desktopPath)
        pngFiles = [file for file in desktopFiles if file.endswith(fileType)]

        if pngFiles:

            print(f"\nFound the following {fileType} files on the desktop:")

            for i in pngFiles:
                print(i)

            print(f"\nMoving the file(s) to {destination}\n")

            for pngFile in pngFiles:
                source = os.path.join(desktopPath, pngFile)

                shutil.move(source, destination)
                print(f"Successfully moved {pngFile} to {destination}\n")

        time.sleep(2)