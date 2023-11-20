import os
import shutil

desktopPath = os.path.expanduser("/Users/asmusaskovbaunstrup/Desktop")
desktopFiles = os.listdir(desktopPath)
pngFiles = [file for file in desktopFiles if file.endswith('.png')]
destination = os.path.join(desktopPath, "PhotosTestFolder")

if pngFiles:

    print("Found the following .png files on the desktop:")
    print()

    for i in pngFiles:
        print(i)

    print()
    print(F"Moving the file(s) to {destination}")
    print()

    for pngFile in pngFiles:
        source = os.path.join(desktopPath, pngFile)

        shutil.move(source, destination)
        print(f"Successfully moved {pngFile} to {destination}")

    print()

else:
    print(), print("No .png files found on the desktop."), print()