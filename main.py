import os
import tkinter
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
import shutil
import ntpath
from PIL import Image, ImageTk
top = tkinter.Tk()
import numpy as np

def copy_file(file,dst):
    shutil.copyfile(file,dst=dst)

def add_to_DB():
    file_path = filedialog.askopenfilename()
    cur_dir = os.getcwd()
    db_dir = os.path.join(cur_dir,'database')
    if not os.path.isdir(db_dir):
        os.makedirs(db_dir)

    filename = ntpath.basename(file_path)
    copy_file(file_path,os.path.join(db_dir,filename))

def load_and_recognize(top,label):
    print("before")
    file_path = filedialog.askopenfilename()
    print("after")
    image = Image.open(file_path)
    photo = ImageTk.PhotoImage(image)
    label.configure(image=photo)
    label.image = photo

print("from main", os.getcwd())
E1 = Entry(top,bd=5)
E1.grid(row=0)

B = Button(text="add to DB",command = add_to_DB)
B.grid(row=0,column=1)

#empty_photo = np.ones((200,200,3),np.uint8)*255

label1 = Label(top,text = "image to be displayed")
label1.grid(row=1)

B2 = Button(text="Load & Recognize",command = lambda: load_and_recognize(top,label1))
B2.grid(row=1,column=1)




top.mainloop()

