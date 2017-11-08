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
import cv2

vs = cv2.VideoCapture(0)

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

def destructor():
    top.destroy()
    vs.release()  # release web camera
    cv2.destroyAllWindows()

def video_loop():
    """ Get frame from the video stream and show it in Tkinter """
    ok, frame = vs.read()  # read frame from video stream
    if ok:  # frame captured without any errors
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)  # convert colors from BGR to RGBA
        current_image = Image.fromarray(cv2image)  # convert image for PIL
        imgtk = ImageTk.PhotoImage(image=current_image)  # convert image for tkinter
        label1.imgtk = imgtk  # anchor imgtk so it does not be deleted by garbage-collector
        label1.config(image=imgtk)  # show the image
    top.after(30, video_loop)

top.protocol('WM_DELETE_WINDOW', destructor)
        
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

video_loop()

top.mainloop()

