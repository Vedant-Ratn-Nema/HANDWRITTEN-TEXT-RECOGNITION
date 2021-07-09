import tkinter as tk
from tkinter import messagebox
import os, io
from google.cloud import vision_v1
from google.cloud.vision_v1 import types
import pandas as pd
from PIL import ImageTk, Image


def gettext(x):
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = r'C:\Users\Lenovo\Desktop\PROJECTS\HCI\serviceauth.json'
    client = vision_v1.ImageAnnotatorClient()

    FOLDER_PATH = r'C:\Users\Lenovo\Desktop\PROJECTS\HCI'
    IMAGE_FILE = x
    FILE_PATH = os.path.join(FOLDER_PATH, IMAGE_FILE)

    with io.open(FILE_PATH, 'rb') as image_file:
        content = image_file.read()

    image = vision_v1.types.Image(content=content)
    response = client.document_text_detection(image=image)

    docText = response.full_text_annotation.text
    return docText


root= tk.Tk()
root.title("Image to Text")

frame = tk.LabelFrame(root, text="Please put your file in the HCI folder on the Desktop to convert it into text", padx=50, pady=50)
frame.pack(padx=10,pady=10)
frame1 = tk.LabelFrame(frame, text="Enter File Name on the HCI folder", padx=100, pady=100)
frame1.pack()


entry1 = tk.Entry(frame1, width=50, font='Helvetica')
entry1.grid(row= 4, padx=10, pady=10,  columnspan= 3) 


def getSquareRoot ():  
    x1 = entry1.get()   
    label1 = tk.Label(frame1, text= gettext(x1), font='Helvetica')
    label1.grid(row=8, padx=10, pady=10, columnspan= 3)

button10 = tk.Button(frame1, text='Get the text', command=getSquareRoot, fg="white", bg="Blue",)
button10.grid(row= 6, padx=10, pady=10, columnspan= 3)


root.mainloop()
