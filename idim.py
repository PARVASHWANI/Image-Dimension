from tkinter import Tk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox as mb
from PIL import Image as img

# Createing a filepicker
Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file
# print("Path: ",filename)#@DEBUG 1

image = img.open(filename)
width,height = image.size
# print("Dimensions Are: ")
# print("Width: " + str(width))
# print("Height: " + str(height))

mb.showinfo('Dimensions',"Height: " + str(width)+'\n'+"Width: " + str(height))
