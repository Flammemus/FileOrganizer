import tkinter
from tkinter import ttk

fileTypeAmount = 1
data = {}

def increaseFileTypeAmount():
    global fileTypeAmount
    if fileTypeAmount < 6:
        fileTypeAmount += 1
        
        fileTypeLabel = tkinter.Label(folderNameFrame, text=f"File Type:")
        fileTypeLabel.grid(row=fileTypeAmount, column=0)

        fileNameEntry = tkinter.Entry(folderNameFrame)
        fileNameEntry.grid(row=fileTypeAmount, column=1)

def decreaseFileTypeAmount():
    global fileTypeAmount
    if fileTypeAmount > 1:
        fileTypeAmount -= 1
        for widget in reversed(folderNameFrame.winfo_children()):
            if int(widget.grid_info()["row"]) == fileTypeAmount + 1:
                widget.destroy()

def enterData():
    folderNameGUI = folderNameEntry.get()
    fileTypeGUI = fileNameEntry.get()
    data['folderName'] = folderNameGUI
    data['fileType'] = fileTypeGUI

window = tkinter.Tk()
window.title("FileOrganizer")

frame = tkinter.Frame(window)
frame.pack()

folderNameFrame = tkinter.LabelFrame(frame, text="Folder Names")
folderNameFrame.grid(row=0, column=0, padx=20, pady=20)

folderNameLabel = tkinter.Label(folderNameFrame, text="Folder Name:")
folderNameLabel.grid(row=0, column=0, pady=20)

folderNameEntry = tkinter.Entry(folderNameFrame)
folderNameEntry.grid(row=0, column=1)

for i in range(fileTypeAmount):
    fileTypeLabel = tkinter.Label(folderNameFrame, text=f"File Type:")
    fileTypeLabel.grid(row=i + 1, column=0)

    fileNameEntry = tkinter.Entry(folderNameFrame)
    fileNameEntry.grid(row=i + 1, column=1)

increaseFileType = tkinter.Button(folderNameFrame, text="+", command=increaseFileTypeAmount)
increaseFileType.grid(row=100, column=0)

decreaseFileType = tkinter.Button(folderNameFrame, text="-", command=decreaseFileTypeAmount)
decreaseFileType.grid(row=100, column=1)

enterDataButton = tkinter.Button(folderNameFrame, text="Done", command=enterData)
enterDataButton.grid(row=100, column=2)

window.mainloop()