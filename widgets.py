# widgets
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox as msg
import tkinter as tk
from tkinter.filedialog import asksaveasfilename as save
from tkinter.filedialog import askopenfilename as openfile
import tkinter.font as tkFont
from tkinter.colorchooser import *
from tkinterhtml import HtmlFrame
from os import path
from threading import Thread
from math import *
import time
from datetime import datetime
from tk_tools import Calendar
from pygame import mixer
from stdout import stdoutIO
from urllib.request import urlopen
import pyscreenshot as ImageGrab
import cv2, pytesseract, io, os, re, jedi, glob
from random import shuffle
from ttkwidgets.autocomplete import AutocompleteCombobox
import belfrywidgets as belfry
from chromium import Chromium
from gooey import *
import gooey
from tkinter import Canvas, Frame, Menu
from ttkwidgets.autocomplete import AutocompleteCombobox
from idlelib.multicall import MultiCallCreator
from xcanvas import XCanvas
from highlighter import *
from PIL import ImageTk, Image
#from idlelib.textview import AutoHideScrollbar






class CustomNotebook(ttk.Notebook):
    """A ttk Notebook with close buttons on each tab"""

    __initialized = False

    def __init__(self, *args, **kwargs):
        if not self.__initialized:
            self.__initialize_custom_style()
            self.__inititialized = True

        kwargs["style"] = "CustomNotebook"
        ttk.Notebook.__init__(self, *args, **kwargs)

        self._active = None

        self.bind("<ButtonPress-1>", self.on_close_press, True)
        self.bind("<ButtonRelease-1>", self.on_close_release)

    def on_close_press(self, event):
        """Called when the button is pressed over the close button"""

        element = self.identify(event.x, event.y)

        if "close" in element:
            index = self.index("@%d,%d" % (event.x, event.y))
            self.state(['pressed'])
            self._active = index

    def on_close_release(self, event):
        """Called when the button is released over the close button"""
        if not self.instate(['pressed']):
            return

        element =  self.identify(event.x, event.y)
        index = self.index("@%d,%d" % (event.x, event.y))

        if "close" in element and self._active == index:
            self.forget(index)
            self.event_generate("<<NotebookTabClosed>>")

        self.state(["!pressed"])
        self._active = None

    def __initialize_custom_style(self):
        style = ttk.Style()
        self.images = (
            PhotoImage("img_close", data='''
                R0lGODlhCAAIAMIBAAAAADs7O4+Pj9nZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
                '''),
            PhotoImage("img_closeactive", data='''
                R0lGODlhCAAIAMIEAAAAAP/SAP/bNNnZ2cbGxsbGxsbGxsbGxiH5BAEKAAQALAAA
                AAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU5kEJADs=
                '''),
            PhotoImage("img_closepressed", data='''
                R0lGODlhCAAIAMIEAAAAAOUqKv9mZtnZ2Ts7Ozs7Ozs7Ozs7OyH+EUNyZWF0ZWQg
                d2l0aCBHSU1QACH5BAEKAAQALAAAAAAIAAgAAAMVGDBEA0qNJyGw7AmxmuaZhWEU
                5kEJADs=
            ''')
        )

        style.element_create("close", "image", "img_close",
                            ("active", "pressed", "!disabled", "img_closepressed"),
                            ("active", "!disabled", "img_closeactive"), border=8, sticky='')
        style.layout("CustomNotebook", [("CustomNotebook.client", {"sticky": "nswe"})])
        style.layout("CustomNotebook.Tab", [
            ("CustomNotebook.tab", {
                "sticky": "nswe", 
                "children": [
                    ("CustomNotebook.padding", {
                        "side": "top", 
                        "sticky": "nswe",
                        "children": [
                            ("CustomNotebook.focus", {
                                "side": "top", 
                                "sticky": "nswe",
                                "children": [
                                    ("CustomNotebook.label", {"side": "left", "sticky": ''}),
                                    ("CustomNotebook.close", {"side": "left", "sticky": ''}),
                                ]
                        })
                    ]
                })
            ]
        })
    ])




class HTML(HtmlFrame):
    def __init__(self, root):
        super().__init__(root, horizontal_scrollbar="auto")
        self.pack(expand=1, fill=BOTH, side=RIGHT)
        self.set("<html></html>")

    def set(self, html):
        self.set_content(html)

    def seturl(self, url):
        self.set_content(urlopen(url).read().decode())

    def setfile(self, filename):
        with open(filename) as file: self.set_content(file.read())


class ProgressBar(belfry.ProgressBar):
    def __init__(self, master, max=200, delay=0.1, bd="#446", fg="red", bg="cyan"):
        v = DoubleVar(value=0)
        super().__init__(master, mode=belfry.DETERMINATE, maximum=max, variable=v, bordercolor=bd, foreground=fg, background=bg)
        self.delay = int(delay*1000)
        self.master = master
        self.max = max
        self.v = v
        self.pack(fill=BOTH, expand=1, padx=10, pady=10)

    def start(self):
        self.v.set(self.v.get()+1)
        if self.v.get() < self.max:
            self.after(self.delay, self.start)

class Wiz(belfry.Wizard):
    def __init__(self, cancel, finish):
        super().__init__(width=640, height=480, cancelcommand=cancel, finishcommand=finish)
        self.show = self.show_pane

    def add(self, name, label, last=False, entry=lambda:1, prev=lambda:1, next=lambda:1):
        if last:
            def entry():
                entry()
                self.set_finish_enabled(True)
            def prev():
                prev()
                self.set_finish_enabled(False)
        super().add_pane(name, label, entrycommand=entry, prevcommand=prev, nextcommand=next)


def isValidGmail(email):
    if len(email) > 10: return bool(re.match("^.+@gmail.com", email))


class GetUserNamePassword(simpledialog.Dialog):

    def body(self, master):

        Label(master, text="Email:").grid(row=0)
        Label(master, text="Password:").grid(row=1)

        self.e1 = Entry(master)
        self.e2 = Entry(master, show="\u2022")

        self.e1.grid(row=0, column=1)
        self.e2.grid(row=1, column=1)
        return self.e1 # initial focus

    def apply(self):
        first = str(self.e1.get())
        second = str(self.e2.get())
        if isValidGmail(first):
            self.result = (first, second) # or something


def get_image(url):
    fd = urlopen(url)
    image_file = io.BytesIO(fd.read())
    im = Image.open(image_file)
    return im

class WallPaper(ttk.Frame):
    def __init__(self, master):
        super().__init__(master)
        #self.state('zoomed')
        #self.resizable(False, False)
        #self.title('Image Slider')
        self.cnt = 1
        self.images = list(map(Image.open, glob.glob('C:/Users/Prannaya/PQRS/images/*.png')))
        #for i in range(150): self.images[i] = ImageTk.PhotoImage(self.images[i])
        #self.images = [get_image(url) for url in self.images]
        shuffle(self.images)

        #self.pictures = cycle(self.images)
        #self.b = Button(self, text='Show', font=('System', 20), command=self.show_images)
        #self.b.pack(side=TOP)
        img = ImageTk.PhotoImage(self.images[0])
        self.pic = Label(self, bg='black', image=img)
        self.pic.image = img
        self.pic.pack(fill=BOTH, expand=1)
        self.pic.bind('<Enter>', self.show_images)
        #self.mainloop()

    def show_images(self, event=None):
        img_object = ImageTk.PhotoImage(self.images[self.cnt%150])
        #img_object = ImageTk.PhotoImage(get_image(next(self.pictures)))
        self.pic.configure(image=img_object)
        self.pic.image = img_object
        self.cnt += 1
        self.after(1000, self.show_images)

    def alter(self):
        alpha = 0
        img_object = self.images[self.cnt%150]
        current_object = self.images[self.cnt%150-1]
        for alpha in range(100):
            current_object = Image.blend(current_object,img_object,alpha/100)
            time.sleep(0.05)
            self.pic.configure(image=ImageTk.PhotoImage(current_object))
            self.pic.image = ImageTk.PhotoImage(current_object)

    
        

class Stopwatch():
    def __init__(self, master):
        self.counter = IntVar(value=-3)
        self.running = BooleanVar(value=False)
        self.frame = Frame(master, bg='white')
        self.frame.pack(fill=BOTH, expand=1)

        self.label = Label(self.frame, text="Welcome!", fg="black", bg='white', font=("Quicksand", 30, "bold") ) #Bahnschrift Light
        self.label.pack(fill=BOTH, expand=1, side=TOP) 
        self.start = Button(self.frame, text='Start', fg="black", bg='white', width=15, command=self.Start) 
        self.stop = Button(self.frame, text='Stop', fg="black", bg='white', width=15, state='disabled', command=self.Stop) 
        self.reset = Button(self.frame, text='Reset', fg="black", bg='white', width=15, state='disabled', command=self.Reset) 
        self.start.pack(fill=BOTH, expand=1, side=TOP) 
        self.stop.pack(fill=BOTH, expand=1, side=TOP) 
        self.reset.pack(fill=BOTH, expand=1, side=TOP) 


    def counter_label(self): 
        if self.running.get():
            if self.counter.get() >= 0:
                self.label['text']= str(self.counter.get()) 
                self.label.after(1000, self.counter_label)
            else:
                self.label['text']= ["Ready", "Set", "Go"][self.counter.get()] 
                self.label.after(300, self.counter_label)
            self.counter.set(self.counter.get()+1)
                    

    # start function of the stopwatch 
    def Start(self): 
        self.running.set(value=True)
        self.counter_label() 
        self.start['state']='disabled'
        self.stop['state']='normal'
        self.reset['state']='normal'

    # Stop function of the stopwatch 
    def Stop(self): 
        self.running.set(value=False)
        self.start['state']='normal'
        self.stop['state']='disabled'
        self.reset['state']='normal'

    # Reset function of the stopwatch 
    def Reset(self):
        self.counter.set(-3)
        self.label['text']=''

        # If rest is pressed after pressing stop. 
        if not self.running.get(): self.reset['state']='disabled'

class Canva(Canvas):
    def __init__(self, root=None, bg='white'):
        image_file = openfile()
        if root is None:
            master = Tk()
            master.title('Canva - An Improved Image Mover')
            master.state('zoomed')
        else: master = root
        self.photo = ImageTk.PhotoImage(Image.open(image_file), master=master)
        self.frame = Frame(master, bg='white')
        self.frame.pack(fill='both', expand=1)
        Canvas.__init__(self, self.frame, bg=bg)
        self.pack(fill='both', expand=1)
        self.img = self.create_image((0, 0), image=self.photo, state="normal", anchor='nw')
        self.bind("<B3-Motion>", self.move_image)
        if root is None: master.mainloop()

    def move_image(self, event):
        self.delete(self.img)
        x = event.x
        y = event.y
        self.img = self.create_image(x, y, image=self.photo, anchor='nw')
        self.update()

class Webcam(Frame):
    def __init__(self, master):
        Frame.__init__(self, master, bg='white')
        self.root = Frame(master, bg='white')
        width, height = 800, 600
        self.cap = cv2.VideoCapture(0)
        self.cap.set(cv2.CAP_PROP_FRAME_WIDTH, width)
        self.cap.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
        label = Label(self.root, text='Webcam Footage', fg="red", font=('Trebuchet MS', 15), bg='white')
        label.pack(side=TOP)
        self.lmain = Label(self.root)
        self.lmain.pack(fill=BOTH, expand=1, side=TOP)
        Button(self.root, text='Play', bg='#19A7A7', fg='white', command=self.toggle_show).pack(side=BOTTOM)
        self.boolean = False
        
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        
    def pack(self, *args, **kwargs):
        self.root.pack(*args, **kwargs)

    def toggle_show(self):
        self.boolean = not self.boolean
        self.show()
        

    def show(self):
        _, frame = self.cap.read()
        frame = cv2.flip(frame, 1)
        cv2image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGBA)
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(image=img)
        self.lmain.imgtk = imgtk
        self.lmain.configure(image=imgtk)
        if self.boolean:
            self.lmain.after(10, self.show)

'''
def download_music():
    url.urlretrieve("https://i.stack.imgur.com/IgD2r.png", "lenna.png")
    url.urlretrieve("https://i.stack.imgur.com/sML82.gif", "lenna.gif")'''



def cal():
    root = Tk()
    root.title('clock')
    root.iconbitmap('clock.ico')
    Calendar(root).pack(fill=BOTH, expand=True) 
    root.mainloop()
    

def calc(master=None):
    if master is None: window = Tk()
    else: window = Frame(master)

    ans = None
    
    def btn_click(item):
        expression = express.get()
        expression = expression + str(item)
        input_text.set(expression)
        express.set(expression)

    def btn_clear():
        express.set("")
        input_text.set("")
     
    def btn_equal():
        expression = express.get()
        result = str(eval(expression, globals())) # 'eval' function evalutes the string expression directly
        input_text.set(result)
        ans = eval(result)
        express.set('')
     
        #expression = ""
     
    express = StringVar(value='')
    input_text = StringVar()

    name = Label(window, text='Calculator', fg="red", font=('Trebuchet MS', 15))
    name.pack(side=TOP)
     
    input_frame = Frame(window, width = 312, height = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
    input_frame.pack(side = TOP)

    input_field = Entry(input_frame, font=('Trebuchet MS', 12), textvariable = input_text, width = 33, bg = "#eee", justify=LEFT)
    input_field.pack(side=BOTTOM)

    input_field.pack(ipady = 10) # 'ipady' is internal padding to increase the height of input field
    btns_frame = Frame(window, width = 312, height = 272.5, bg = "grey")
    btns_frame.pack()

    # first row
    clear = Button(btns_frame, text = "C", fg = "black", width = 30, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_clear()).grid(row = 0, column = 0, columnspan = 3, padx = 0.5, pady = 0.5)
    #ans = Button(btns_frame, text = "ans", fg = "black", width = 15, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("ans")).grid(row = 0, column = 2, columnspan = 1, padx = 0.5, pady = 0.5)
    divide = Button(btns_frame, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("/")).grid(row = 0, column = 3, padx = 0.5, pady = 0.5)
     
    # second row
    seven = Button(btns_frame, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(7)).grid(row = 1, column = 0, padx = 0.5, pady = 0.5)
    eight = Button(btns_frame, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(8)).grid(row = 1, column = 1, padx = 0.5, pady = 0.5)
    nine = Button(btns_frame, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(9)).grid(row = 1, column = 2, padx = 0.5, pady = 0.5)
    multiply = Button(btns_frame, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("*")).grid(row = 1, column = 3, padx = 0.5, pady = 0.5)
     
    # third row
    four = Button(btns_frame, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(4)).grid(row = 2, column = 0, padx = 0.5, pady = 0.5)
    five = Button(btns_frame, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(5)).grid(row = 2, column = 1, padx = 0.5, pady = 0.5)
    six = Button(btns_frame, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(6)).grid(row = 2, column = 2, padx = 0.5, pady = 0.5)
    minus = Button(btns_frame, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("-")).grid(row = 2, column = 3, padx = 0.5, pady = 0.5)
     
    # fourth row
    one = Button(btns_frame, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(1)).grid(row = 3, column = 0, padx = 0.5, pady = 0.5)
    two = Button(btns_frame, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(2)).grid(row = 3, column = 1, padx = 0.5, pady = 0.5)
    three = Button(btns_frame, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(3)).grid(row = 3, column = 2, padx = 0.5, pady = 0.5)
    plus = Button(btns_frame, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("+")).grid(row = 3, column = 3, padx = 0.5, pady = 0.5)

    # fifth row
    zero = Button(btns_frame, text = "0", fg = "black", width = 10, height = 3, bd = 0, bg = "#fff", cursor = "hand2", command = lambda: btn_click(0)).grid(row = 4, column = 0, padx = 0.5, pady = 0.5)
    point = Button(btns_frame, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click(".")).grid(row = 4, column = 1, padx = 0.5, pady = 0.5)
    equals = Button(btns_frame, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_equal()).grid(row = 4, column = 2, padx = 0.5, pady = 0.5)
    floor = Button(btns_frame, text = "//", fg = "black", width = 10, height = 3, bd = 0, bg = "#eee", cursor = "hand2", command = lambda: btn_click("//")).grid(row = 4, column = 3, padx = 0.5, pady = 0.5)

    if master is None: window.mainloop()
    else: return window

class Clock(Label):
    """ Class that contains the clock widget and clock refresh """

    def __init__(self, parent=None, seconds=True, colon=False):
        """
        Create and place the clock widget into the parent element
        It's an ordinary Label element with two additional features.
        """
        Label.__init__(self, parent)

        self.display_seconds = seconds
        if self.display_seconds:
            self.time     = time.strftime('%H:%M:%S')
        else:
            self.time     = time.strftime('%I:%M %p').lstrip('0')
        self.display_time = self.time
        self.configure(text=self.display_time)

        if colon:
            self.blink_colon()

        self.after(200, self.tick)


    def tick(self):
        """ Updates the display clock every 200 milliseconds """
        if self.display_seconds:
            new_time = time.strftime('%H:%M:%S')
        else:
            new_time = time.strftime('%I:%M %p').lstrip('0')
        if new_time != self.time:
            self.time = new_time
            self.display_time = self.time
            self.config(text=self.display_time)
        self.after(200, self.tick)


    def blink_colon(self):
        """ Blink the colon every second """
        if ':' in self.display_time:
            self.display_time = self.display_time.replace(':',' ')
        else:
            self.display_time = self.display_time.replace(' ',':',1)
        self.config(text=self.display_time)
        self.after(1000, self.blink_colon)

def clock(master=None, bg='white', fg='black', font=('Courier', 20)):
    if master is None:
        frame  = Tk()
        frame.title('clock')
        frame.iconbitmap('clock.ico')
    else: frame = Frame(master)
    clock1 = Clock(frame)
    clock1.configure(bg=bg,fg=fg,font=font)
    clock1.pack()
    if master is None: frame.mainloop()
    else: return frame


class StatusBar(Frame):
    """
    This class implements a statusbar.
    """

    def __init__(self, master):
        Frame.__init__(self, master)
        self.config(border=1)

        self.msg = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.msg.pack(side='left', expand=True, fill=X)

        self.column = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.column.config(text='Col: 0')
        self.column.pack(side='right', fill=X)

        self.line = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.line.config(text='Line: 1')
        self.line.pack(side='right', fill=X)


        self.mode = Label(self, bd=1, relief=SUNKEN, anchor=W)
        self.mode.config(text='Mode: Light')
        self.mode.pack(side='right', fill=X)


    def set_msg(self, data):
        """
        Set statusbar msg.
        """

        self.msg.config(text=data)
        self.msg.update_idletasks()

    def clear_msg(self):
        """
        Clear statusbar msg.
        """

        self.msg.config(text="")
        self.msg.update_idletasks()


    def set_column(self, col):
        """
        Set the column field with col.
        """

        self.column.config(text='Col: %s' % col)
        self.column.update_idletasks()

    def set_line(self, line):
        """
        Set the line field.
        """

        self.line.config(text='Line: %s' % line)
        self.line.update_idletasks()

    def set_mode(self, mode):
        """
        Set the mode field.
        """

        self.mode.config(text='Mode: %s' % mode)
        self.mode.update_idletasks()


class Paint(object):

    DEFAULT_PEN_SIZE = 10.0
    DEFAULT_COLOR = 'black'

    def __init__(self, master=None):
        if master is None:
            self.root = Tk()
            self.root.title('TK Paint')
            self.root.state('zoomed')
        else:
            self.root = Frame(master)
            self.root.pack(fill=BOTH, expand=1)

        self.c = Canvas(self.root, bg='white', width=600, height=600)
        self.c.pack(fill=BOTH, expand=1, side=TOP)
        self.sizex = self.c.winfo_width()
        self.sizey = self.c.winfo_height()

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen, fg='black', bg='white')
        self.pen_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush, fg='black', bg='white')
        self.brush_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.color_button = Button(self.root, text='Choose a Color', command=self.choose_color, fg='black', bg='white')
        self.color_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.bg_button = Button(self.root, text='Choose a Background Color', command=self.choose_bg, fg='black', bg='white')
        self.bg_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser, fg='black', bg='white')
        self.eraser_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.clear_button = Button(self.root, text='Clear', command=self.clear, fg='black', bg='white')
        self.clear_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.save_button = Button(self.root, text='Save Canva', command=self.savec, fg='black', bg='white')
        self.save_button.pack(side=LEFT, fill=BOTH, expand=1)

        Label(self.root, text='Size: ', fg='black', bg='white').pack(side=LEFT, fill=BOTH)

        self.var = IntVar(value=10)
        self.eraservar = IntVar(value=50)
        self.choose_size_button = Spinbox(self.root, from_=1, to=400, width=5, textvariable=self.var, fg='black', bg='white')
        self.choose_size_button.pack(side=LEFT, fill=BOTH, expand=1)

        self.setup()
        if master is None: self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.bg = "white"
        self.line_width = self.var.get()
        self.color = self.DEFAULT_COLOR
        self.img = ImageTk.PhotoImage(Image.new('RGB', (640, 480), self.bg), master=self.root)
        self.colorp = True
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<ButtonPress-1>', self.paint)
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        self.root.bind('<Control-s>', self.savec)

    def use_pen(self):
        self.activate_button(self.pen_button)
        self.choose_size_button.config(textvariable=self.var)

    def use_brush(self):
        self.activate_button(self.brush_button)
        self.choose_size_button.config(textvariable=self.var)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def choose_bg(self):
        self.bg = askcolor(color=self.color)[1]
        self.c.config(bg=self.bg)
        self.img = ImageTk.PhotoImage(Image.new('RGB', (640, 480), self.bg), master=self.root)

    def saveit(self, widget):
        x2 = self.root.winfo_rootx() + self.c.winfo_x()
        y2 = self.root.winfo_rooty() + self.c.winfo_y()
        x1 = x2 + self.c.winfo_width()
        y1 = y2 + self.c.winfo_height()
        try: file = self.filename
        except: file = save(title="Select file to save as:",
                            filetypes = (("PNG Image Files","*.png"),("JPEG Image Files","*.jpg"),("GIF Image Files","*.gif"),("Icon Image Files","*.ico")))
        finally:
            if file:
                ImageGrab.grab().crop((x2,y2,x1,y1)).save(file)
                self.filename = file

    def savec(self, event=None):
        self.saveit(self.c)

    def clear(self):
        self.c.delete("all")
        self.photo = self.c.create_image((0, 0), image=self.img, state="normal", anchor='nw')

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)
        self.choose_size_button.config(textvariable=self.eraservar)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED, bg='black', fg='white')
        some_button.config(relief=SUNKEN, fg='black', bg='white')
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.var.get() + 2*bool(self.active_button==self.brush_button) if not self.eraser_on else self.eraservar.get()
        paint_color = self.bg if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None

class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        Canvas.__init__(self, *args, **kwargs)
        self.textwidget = None
        self.color = "black"
        self.background = "white"

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
        self.delete("all")
        self.config(bg=self.background)
        i = self.textwidget.index("@0,0")
        while True :
            dline= self.textwidget.dlineinfo(i)
            if dline is None: break
            color = self.color
            y = dline[1]
            linenum = str(i).split(".")[0]
            font = tkFont.Font(family=self.textwidget.family.get(), size=self.textwidget.size.get(), weight='bold') if i.split('.')[0] == self.textwidget.index(INSERT).split('.')[0] else self.textwidget.font
            self.create_text(2.5,y,anchor="nw", text=linenum,  font=font, fill=color)
           
            i = self.textwidget.index("%s+1line" % i)


#Text widget
class CustomText(Text, IPyText):
    def __init__(self, *args, **kwargs):
        Text.__init__(self, *args, **kwargs)

        # create a proxy for the underlying widget
        self._orig = self._w + "_orig"
        self.tk.call("rename", self._w, self._orig)
        self.tk.createcommand(self._w, self._proxy)
        self.family = StringVar(value='Quicksand') #Bahnschrift Light
        self.size = IntVar(value=10)
        self.weight = "normal"
        self.slant = "roman"
        self.overstrike = False
        self.underline = False
        self.raw_font = (self.family, self.size)
        self.font = tkFont.Font(family=self.family.get(), size=self.size.get())
        self.configure(font=self.font, tabs=40)
        self.lexer = PythonLexer
        self.lastfind = None
        self.bind('<Control-F>', self.onFind)
        self.bind('<Control-Shift-KeyPress-F>', self.onRefind)
        self.textoutput = None
        IPyText.__init__(self, baseclass=tk.Text, widget=self, text="")
        self.pack(fill=BOTH, expand=1, side=RIGHT)


    def _proxy(self, *args):
        # let the actual widget perform the requested action
        cmd = (self._orig,) + args
        result = self.tk.call(cmd)

        # generate an event if something was added or deleted,
        # or the cursor position changed
        if (args[0] in ("insert", "replace", "delete") or 
            args[0:3] == ("mark", "set", "insert") or
            args[0:2] == ("xview", "moveto") or
            args[0:2] == ("xview", "scroll") or
            args[0:2] == ("yview", "moveto") or
            args[0:2] == ("yview", "scroll")
        ):
            self.event_generate("<<Change>>", when="tail")

        # return what the actual widget returned
        return result
    '''
    def __setitem__(self, key, val):
        IPyText.__setitem__(self, key, val)

    def __getitem__(self, key):
        return IPyText.__getitem__(self, key)'''

    def change_lexer(self, extens):
        for i in extensions:
            if extens.lower() in i:
                self.lexer = i[-1]
                IPyText._update(self)
                return
        self.lexer = TextLexer
        IPyText._update(self)

    def updatelexer(self):
        IPyText._update(self)

    def onGoto(self, event=None, forceline=None):
        line = forceline or simpledialog.askinteger('GoTo', 'Enter line number')
        Text.update(self)
        Text.focus(self)
        if line is not None:
            maxindex = Text.index(self, END+'-1c')
            maxline  = int(maxindex.split('.')[0])
            if line > 0 and line <= maxline:
                Text.mark_set(self, INSERT, '%d.0' % line)      # goto line
                Text.tag_remove(self, SEL, '1.0', END)          # delete selects
                Text.tag_add(self, SEL, INSERT, 'insert + 1l')  # select line
                Text.see(self, INSERT)                          # scroll to line
            else:
                msg.showerror('GoTo', 'Bad line number')

    def onFind(self, event=None, lastkey=None):
        key = lastkey or simpledialog.askstring('Search Dialog', 'Enter search string')
        Text.update(self)
        Text.focus(self)
        self.lastfind = key
        if key:                                                    # 2.0: nocase
            nocase = dict().get('caseinsens', True)               # 2.0: config
            where = self.text.search(key, INSERT, END, nocase=nocase)
            if not where:                                          # don't wrap
                msg.showerror('Search Dialog', 'String not found')
            else:
                pastkey = where + '+%dc' % len(key)           # index past key
                Text.tag_remove(self, SEL, '1.0', END)         # remove any sel
                Text.tag_add(self, SEL, where, pastkey)        # select key
                Text.mark_set(self, INSERT, pastkey)           # for next find
                Text.see(self, where)                          # scroll display

    def onRefind(self, event=None):
        self.onFind(event, self.lastfind)


def PanedText(master, **kwargs):
    textwid = CustomText(master, **kwargs)
    textwid
    return textwid


#Markdown
def NotePad(root, buttons=False):
    if buttons:
        frame_button = gooey.Frame(root)

        def change_font(event=None):
            text.family.set(fontbox.get())
            text.font.configure(family=text.family.get())
            text.tag_config("bt", font=tkFont.Font(family=text.family.get(), size=text.size.get(), weight='bold'))
            text.tag_config("it", font=tkFont.Font(family=text.family.get(), size=text.size.get(), slant='italic'))
            text.tag_config("ut", underline=True)
            text.tag_config("st", overstrike=True)

        #Font
        fontbox = AutocompleteCombobox(frame_button, completevalues=list(tkFont.families()))
        fontbox.pack(fill=BOTH, side=LEFT)
        
        def OnBigger():
            text.size.set(text.size.get() + 2 if text.size.get() < 96 else text.size.get())
            text.font.configure(size=text.size.get())
            text.tag_config("bt", font=tkFont.Font(family=text.family.get(), size=text.size.get(), weight='bold'))
            text.tag_config("it", font=tkFont.Font(family=text.family.get(), size=text.size.get(), slant='italic'))
            text.tag_config("ut", underline=True)
            text.tag_config("st", overstrike=True)

        def OnSmaller():
            text.size.set(text.size.get() - 2 if text.size.get() > 8 else text.size.get())
            text.font.configure(size=text.size.get())
            text.tag_config("bt", font=tkFont.Font(family=text.family.get(), size=text.size.get(), weight='bold'))
            text.tag_config("it", font=tkFont.Font(family=text.family.get(), size=text.size.get(), slant='italic'))
            text.tag_config("ut", underline=True)
            text.tag_config("st", overstrike=True)

        #Size
        img1 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/IncreaseA.png").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img1, compound="top", bg='white', command=OnBigger)
        button.image = img1
        button.pack(side=LEFT, fill=BOTH)
        
        img1 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/DecreaseA.png").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img1, compound="top", bg='white', command=OnSmaller)
        button.image = img1
        button.pack(side=LEFT, fill=BOTH)
        #size = ttk.Label(frame_button, text=(lambda: text.size)()

        def make_bold(event=None):
            try:
                if 'bt' in text.tag_names("sel.first"):
                    text.tag_remove("bt", "sel.first", "sel.last")
                else:
                    text.tag_add("bt", "sel.first", "sel.last")
            except:
                if 'ut' in text.tag_names(CURRENT):
                    text.tag_remove("bt", "insert wordstart", "insert wordend")
                else:
                    text.tag_add("bt", "insert wordstart", "insert wordend")

        #Bold
        img1 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/BoldB.ico").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img1, compound="top", bg='white', command=make_bold)
        button.image = img1
        button.pack(side=LEFT)

        def make_italic(event=None):
            try:
                if 'it' in text.tag_names("sel.first"):
                    text.tag_remove("it", "sel.first", "sel.last")
                else:
                    text.tag_add("it", "sel.first", "sel.last")
            except:
                if 'ut' in text.tag_names(CURRENT):
                    text.tag_remove("it", "insert wordstart", "insert wordend")
                else:
                    text.tag_add("it", "insert wordstart", "insert wordend")

        #Italic
        img2 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/ItalicI.jpg").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img2, compound="top", bg='white', command=make_italic)
        button.image = img2
        button.pack(side=LEFT)

        def make_under(event=None):
            try:
                if 'ut' in text.tag_names("sel.first"):
                    text.tag_remove("ut", "sel.first", "sel.last")
                else:
                    text.tag_add("ut", "sel.first", "sel.last")
            except:
                if 'ut' in text.tag_names(CURRENT):
                    text.tag_remove("ut", "insert wordstart", "insert wordend")
                else:
                    text.tag_add("ut", "insert wordstart", "insert wordend")
        #Underline
        img3 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/UnderU.png").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img3, compound="top", bg='white', command=make_under)
        button.image = img3
        button.pack(side=LEFT)

        def make_strike(event=None):
            try:
                if 'st' in text.tag_names("sel.first"):
                    text.tag_remove("st", "sel.first", "sel.last")
                else:
                    text.tag_add("st", "sel.first", "sel.last")
            except:
                if 'st' in text.tag_names(CURRENT):
                    text.tag_remove("st", "insert wordstart", "insert wordend")
                else:
                    text.tag_add("st", "insert wordstart", "insert wordend")

        #Strikethrough
        img4 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/StrikeS.jpg").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img4, compound="top", bg='white', command=make_strike)
        button.image = img4
        button.pack(side=LEFT)

        def make_high(event=None):
            color = askcolor()[-1]
            text.tag_config('ht'+color, background=color)
            try: text.tag_add('ht'+color, "sel.first", "sel.last")
            except: text.tag_add('ht'+color, "insert wordstart", "insert wordend")

        #Highlight
        img5 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/highlight.jfif").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img5, compound="top", bg='white', command=make_high)
        button.image = img5
        button.pack(side=LEFT)

        def make_color(event=None):
            color = askcolor()[-1]
            try: text.tag_add('ct'+color, "sel.first", "sel.last")
            except: text.tag_add('ct'+color, "insert wordstart", "insert wordend")

        #Color
        img6 = ImageTk.PhotoImage(Image.open("C:/Users/Prannaya/PQRS/colorpal.png").resize((50, 50)), master=frame_button)
        button = Button(frame_button, image = img6, compound="top", bg='white', command=make_color)
        button.image = img6
        button.pack(side=LEFT)

        def indent_left(event=None):
            #text.tag_add('left', "1.0", END)
            try:
                text.tag_remove('right', "sel.first linestart", "sel.last lineend")
                text.tag_remove('center', "sel.first linestart", "sel.last lineend")
                text.tag_add('left', "sel.first linestart", "sel.last lineend")
            except: text.tag_add('left', "current linestart", "current lineend")

        def indent_center(event=None):
            #text.tag_add('left', "1.0", END)
            try: text.tag_add('center', "sel.first linestart", "sel.last lineend")
            except: text.tag_add('center', "current linestart", "current lineend")

        def indent_right(event=None):
            #text.tag_add('left', "1.0", END)
            try: text.tag_add('right', "sel.first linestart", "sel.last lineend")
            except: text.tag_add('right', "current linestart", "current lineend")


        #frame_button.grid()
        frame_button.pack(side=TOP)

    
    frame = Frame(root)
    frame.pack(fill="both", expand=True)

    def OnVsb(*args): text.yview(*args)
    vsb = Scrollbar(frame, orient="vertical", command=OnVsb)
    vsb.pack(side=RIGHT, fill=Y)
    
    linenumbers = TextLineNumbers(frame, width=50, bg="white")
    linenumbers.pack(side="left", fill="y")
    text = PanedText(frame, wrap=WORD, yscrollcommand=vsb.set, undo=True)
    text.linenumbers = linenumbers
    text.frame = frame
    linenumbers.attach(text)
    def _on_change(event): linenumbers.redraw()
    text.bind("<<Change>>", _on_change)
    text.bind("<Configure>", _on_change)

    def backspace(e=None):
        if e.widget.get('current -4 chars', CURRENT) == ' '*4:
            e.widget.delete('current -4 chars', CURRENT)
            return "break"

    text.bind('<BackSpace>', backspace)
    text.config(font=text.font)

    
    if buttons:
        def enterauto(event=None):
            fontbox.autocomplete()
            fontbox.event_generate("<<ComboboxSelected>>")
        text.bind("<Control-b>", make_bold)
        text.bind("<Control-i>", make_italic)
        text.bind("<Control-u>", make_under)
        text.bind("<Control-h>", make_high)
        fontbox.current(sorted(tkFont.families()).index(text.family.get()))
        fontbox.bind("<<ComboboxSelected>>", change_font)
        fontbox.bind("<Return>", enterauto)

        def show_menu(e):
            the_menu = Menu(text, tearoff=0)
            the_menu.add_command(label="Cut", accelerator="Ctrl+X", command=lambda: text.event_generate("<<Cut>>"))
            the_menu.add_command(label="Copy", accelerator="Ctrl+C", command=lambda: text.event_generate("<<Copy>>"))
            the_menu.add_command(label="Paste", accelerator="Ctrl+V", command=lambda: text.event_generate("<<Paste>>"))
            the_menu.add_command(label="Bold", accelerator="Ctrl+B", command=make_bold)
            the_menu.add_command(label="Italic", accelerator="Ctrl+I", command=make_italic)
            the_menu.add_command(label="Underline", accelerator="Ctrl+U", command=make_under)
            the_menu.add_command(label="Strikethrough", command=make_strike)
            the_menu.add_command(label="Highlight", accelerator="Ctrl+H", command=make_high)
            the_menu.add_command(label="Color", command=make_color)
            the_menu.add_command(label="Align Left", command=indent_left)
            the_menu.add_command(label="Center", command=indent_center)
            the_menu.add_command(label="Align Right", command=indent_right)
            
            the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)


        
        text.tag_config("bt", font=tkFont.Font(family=text.family.get(), size=text.size.get(), weight='bold'))
        text.tag_config("it", font=tkFont.Font(family=text.family.get(), size=text.size.get(), slant='italic'))
        text.tag_config("ut", underline=True)
        text.tag_config("st", overstrike=True)
        for i in ("left", "center", "right"):
            text.tag_config(i, justify=i)
        

    else:
        the_menu = Menu(root, tearoff=0)
        the_menu.add_command(label="Cut", accelerator="Ctrl+X")
        the_menu.add_command(label="Copy", accelerator="Ctrl+C")
        the_menu.add_command(label="Paste", accelerator="Ctrl+V")

        def show_menu(e):
            w = e.widget
            the_menu.entryconfigure("Cut",
            command=lambda: w.event_generate("<<Cut>>"))
            the_menu.entryconfigure("Copy",
            command=lambda: w.event_generate("<<Copy>>"))
            the_menu.entryconfigure("Paste",
            command=lambda: w.event_generate("<<Paste>>"))
            #the_menu.tk_popup(e.x, e.y)
            the_menu.tk.call("tk_popup", the_menu, e.x_root, e.y_root)
    text.bind("<Button-3>", show_menu)
    return text
