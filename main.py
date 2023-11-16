import os
import shutil
import time
import tkinter as tk
from tkinter import messagebox

desktopPath = os.path.expanduser("~/Desktop")
desktopFiles = os.listdir(desktopPath)
pngFiles = [file for file in desktopFiles if file.endswith('.png')]
destinationFolder = os.path.join(desktopPath, "PhotoesTestFolder")

def showPopup(message):
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    messagebox.showinfo(message)

if pngFiles:
    print("Found the following .png files on the desktop:")
    showPopup("Found .png images, moving them now..")
    for pngFile in pngFiles:
        print(os.path.join(desktopPath, pngFile))

        pngFilePath = desktopPath + "/" + pngFile

        shutil.move(pngFilePath, destinationFolder)
else:
    print("No .png files found on the desktop.")
    showPopup("No .png files found on the desktop.")