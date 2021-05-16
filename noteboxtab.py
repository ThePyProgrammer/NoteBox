from pytools import *
from tkinter import *
from tkinter import simpledialog
from tkinter import ttk
from tkinter import messagebox as msg
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
from PIL import ImageTk, Image
import pyscreenshot as ImageGrab
import cv2, pytesseract, io, os, re, jedi, glob
from gooey import *
import gooey
from tkinter import Canvas, Frame, Menu
from widgets import *
from idlelib.statusbar import MultiStatusBar
from reversio import othello


# =============================  FUNCTIONS  =============================#
def isName(name):  #
    try:
        exec(f'{name} = 1')  #
    except:
        return False  #
    else:
        return True  #
    #
    #


fDir = path.dirname(__file__)  #
# I Feel You (Avengers Infinity War, Alan Silvestri, 2018)               #
mDir1 = 'C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Alan-Silvestri-I-Feel-You-_From-_Avengers_-Infinity-War__Audio-Only_.mp3'
# Portals (Avengers Endgame, Alan Silvestri, 2019)                       #
mDir2 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Alan-Silvestri-Portals-_From-_Avengers_-Endgame__Audio-Only_.mp3"
# Avengers Endgame Trailer 2 Music (2019)                                #
mDir3 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Avengers-Endgame-Trailer-2-Music-Full-Trailer-Version.mp3"
# Avengers Infinity War Trailer Music (2018)                             #
mDir4 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Avengers-Infinity-War-Trailer-Music.mp3"


#
# ============================= IMAGE CANVAS ============================#
class ImageCanvas(Paint):
    def __init__(self, image_file, nb):
        self.actimage = self.ogimage = Image.open(image_file)
        frame = ttk.Frame(nb)
        super().__init__(frame)
        nb.add(frame, text=image_file.split("/")[-1].center(50))
        self.image = ImageTk.PhotoImage(self.actimage, master=self.c)
        self.photo = self.c.create_image(400, 400, image=self.image)
        # self.pack(fill=BOTH, expand=TRUE, side=TOP)
        self.c.bind('<B3-Motion>', self.move_image)

        Label(self.root, text='Rotate by: ', fg='black', bg='white').pack(side=LEFT, fill=BOTH)

        self.angle = IntVar(value=0)
        self.intangle = 0
        self.angle_button = Spinbox(self.root, from_=0, to=360, width=5, textvariable=self.angle, fg='black',
                                    bg='white', command=self.rotate)
        self.angle_button.bind("<Return>", self.rotate)
        self.angle_button.pack(side=LEFT, fill=BOTH, expand=1)

    def move_image(self, event=None):
        self.c.delete(self.photo)
        x = event.x
        y = event.y
        self.photo = self.c.create_image(x, y, image=self.image, anchor='nw')
        self.c.update()

    def rotate(self, event=None):
        self.actimage = self.actimage.rotate(self.angle.get() - self.intangle)
        self.image = ImageTk.PhotoImage(self.actimage, master=self.c)
        self.intangle = self.angle.get()
        self.c.delete(self.photo)
        x = 400 if event is None else event.x
        y = 400 if event is None else event.y
        self.photo = self.c.create_image(x, y, image=self.image, anchor='nw')
        self.c.update()


# ==============================  OTHELLO  ==============================#
class Othello(Frame):
    def __init__(self, root):
        super().__init__(root, background="#008000")
        othello(self)
        self.pack(fill=BOTH, expand=1)


def othellonb(nb):
    othframe = ttk.Frame(nb)
    nb.add(othframe, text='Othello'.center(50))
    Othello(othframe)


# ==============================   PIANO   ==============================#
def pianonb(nb):
    pass


# =========================   Visual HyperText   ========================#
class VisualHT(Frame):
    def __init__(self, master=None):
        if master is None:
            self.master = Tk()
            self.master.title('Visual HyperText')
            self.master.state('zoomed')
        else:
            self.master = master

        super().__init__(self.master)
        self.text = NotePad(self, True)
        self.text.change_lexer('html')
        self.html = HTML(self)
        self.text.bind("<<Configure>>", self.modify, add="+")
        self.text.bind("<<Change>>", self.modify, add="+")
        self.pack(expand=1, fill=BOTH)
        self.text.insert("1.0", """<!DOCTYPE html>
<html>
<body>

<div style="background-color:black;color:white;padding:20px;">
  <h2>Visual HyperText</h2>
  <p>Visual HyperText is a software that simply allows you to visualise HTML. Not everything is integrated, but what is helps.</p>
<code>
print("Hello from Prannaya")<br>
print("Python is cool")<br>
</code>
</div>
<h1>My <span style="color:red">NOT</span> First Heading in Visual HyperText</h1>
<p> Start coding. HTML is counting on you. </p>
</body>
</html>""")
        self.text.updatelexer()
        self.text.frame.pack_forget()
        self.html.pack_forget()
        self.text.frame.pack(side=LEFT, fill=BOTH)
        self.html.pack(side=LEFT, fill=BOTH, expand=1)
        if master is None: self.master.mainloop()

    def modify(self, *args, **kw):
        try:
            self.html.set(self.text.get("1.0", END))
            self.text.updatelexer()
        except:
            pass

    def setfile(self, filename):
        self.html.setfile(filename)
        self.text.delete("1.0", END)
        with open(filename) as file: self.text.insert("1.0", file.read())

    def seturl(self, url):
        self.html.seturl(url)
        self.text.delete("1.0", END)
        self.text.insert("1.0", urlopen(url).read().decode())


def VisualHTnb(nb, filename=None):
    frame = ttk.Frame(nb)
    if filename is None:
        savelocation = 'untitled'
        nb.add(frame, text='VHT - *untitled'.center(50))
    else:
        savelocation = filename
        nb.add(frame, text=('VHT - ' + savelocation.split('/')[-1]).center(50))

    def openit(event=None):
        openlocation = openfile(title="Select file to open:")
        if len(openlocation): noteui(nb, openlocation)

    def saveas(event=None):
        t = text.get("1.0", END)
        templocation = save(title="Select file to save as:",
                            filetypes=(("HTML files", ".html"), ("Text files", ".txt"), ("All files", "*.*")))
        if len(templocation):
            savelocation = templocation
            file1 = open(savelocation, "w+")
            file1.write(t)
            file1.close()
            nb.tab(frame, text=('VHT - ' + savelocation.split('/')[-1]).center(50))
            text.bind('<<Configure>>', saveit, add='+')
            text.bind('<<Change>>', saveit, add='+')

    def saveit(event=None):
        if savelocation == 'untitled':
            saveas()
        else:
            file = open(savelocation, 'w+')
            file.write(text.get("1.0", END))
            file.close()

    def new(event=None):
        VisualHTnb(nb, None)

    vht = VisualHT(frame)
    text = vht.text
    html = vht.html

    if filename is not None:
        vht.setfile(filename)
        text.bind('<<Configure>>', saveit, add='+')
        text.bind('<<Change>>', saveit, add='+')

    text.focus()
    text.bind('<F5>', vht.modify)
    text.bind('<Control-s>', saveit)
    text.bind('<Control-o>', openit)
    text.bind('<Control-n>', new)
    text.focus_set()
    frame.bind('<Control-s>', saveit)
    frame.bind('<Control-o>', openit)
    frame.bind('<Control-n>', new)
    frame.bind('<F5>', vht.modify)
    frame.update()


# ===============================  CANVA  ===============================#
#
def canvaa(nb):  #
    new_frame = ttk.Frame(nb)  #
    nb.add(new_frame, text='Canva'.center(50))  #
    frame = gooey.Frame(new_frame)  #
    frame.pack(expand=1, fill=BOTH)  #
    paint = Paint(frame)  #
    paint.root.bind('<Control-n>', lambda event=None: canvaa(nb))  #
    #


# ========================  NOTE USER INTERFACE  ========================#
#
def noteui(nb, filename=None):  #
    if filename is not None:
        if filename.split('.')[-1].lower() in ['jpg', 'jpeg', 'jfif', 'png', 'ico', 'bmp', 'eps', 'epsf', 'epsi', 'gif',
                                               'dib', 'icns', 'im', 'jpe', 'jif', 'jfi', 'pcx', 'pbm', 'pgm', 'ppm',
                                               'pnm', 'sgi', 'rgb', 'rgba', 'bw', 'int', 'inta', 'spi', 'tiff', 'tif',
                                               'webp', 'xbm']:
            ImageCanvas(image_file=filename, nb=nb)
            return None, None, None
        if filename.split('.')[-1].lower() in ['html', 'htm']:
            VisualHTnb(nb, filename)
            return None, None, None

    root1 = ttk.Frame(nb)  #
    if filename is None:  #
        savelocation = 'untitled'  #
        nb.add(root1, text='NoteBox - untitled'.center(50))  #
    else:  #
        savelocation = filename  #
        nb.add(root1, text=('Notebox - ' + savelocation.split('/')[-1]).center(50))
        #

    def printf(*args, event=None, sep=" ", end="\n"):  #
        bits = sep.join(list(map(str, args))) + end  #
        textoutput.configure(state='normal')  #
        textoutput.insert(END, bits)  #
        textoutput.configure(state='disabled')  #
        #

    def func2(event=None):  #
        def execut():  #
            excepto = ''  #
            with stdoutIO() as s:  #
                try:
                    exec(execute(text.get("1.0", END)))  #
                except Exception as e:
                    excepto = str(e)  #
                #
            printf(s.getvalue())  #
            if len(excepto): printf('Error: ', excepto)  #
            #

        printf(' Starting Editor '.center(50, '='))  #
        try:
            execut()  #
        except Exception as e:
            msg.showerror('Error in Editor', str(e))  #
        printf(' Executed Editor '.center(50, '='))  #
        #

    def OnVsb(*args):
        text.yview(*args)  #

    #
    def openit(event=None):  #
        openlocation = openfile(title="Select file to open:")  #
        if len(openlocation): noteui(nb, openlocation)  #
        #

    def saveas(event=None):  #
        t = text.get("1.0", END)  #
        templocation = save(title="Select file to save as:")  #
        if len(templocation):  #
            savelocation = templocation  #
            file1 = open(savelocation, "w+")  #
            file1.write(t)  #
            file1.close()  #
            nb.tab(root1, text=('Notebox - ' + savelocation.split('/')[-1]).center(50))
            text.change_lexer(savelocation.split('.')[-1])  #

    def saveit(event=None):
        if savelocation == 'untitled':
            saveas()
        else:
            file = open(savelocation, 'w+')
            file.write(text.get("1.0", END))
            file.close()

    def new(event=None):
        root1 = ttk.Frame(nb)
        noteui(nb, None)

    def notsaved(event=None):
        nb.tab(root1, text='Notebox - *untitled')

    frame_text = gooey.Frame(root1)
    frame_text.pack(fill=BOTH, side=LEFT, expand=True)

    label = Label(frame_text, text='Editor', fg="red", font=('Trebuchet MS', 15))
    label.pack()

    text = NotePad(frame_text, True)
    xscroll = Scrollbar(frame_text, orient=HORIZONTAL)
    xscroll.pack(side=BOTTOM, fill='x')
    text.config(xscrollcommand=xscroll)
    # self.font = tkFont.Font(family=self.family, size=self.size)
    # text.config(font=text.font)
    xscroll.pack_forget()
    # , True
    # text.grid()
    # text.pack(fill=BOTH, side=RIGHT, expand=True)
    # text.place(x = 1, y = 0, height = 993, width = 1925)
    if filename != None:
        try:
            file = open(filename, 'r')
        except:
            file = open(filename, 'rb')
        text.insert(END, file.read())
        file.close()
        text.change_lexer(filename.split('.')[-1])
        text.bind('<<Configure>>', saveit, add='+')
        text.bind('<<Change>>', saveit, add='+')
        text.config(font=text.font)
    else:
        text.bind('<<Configure>>', notdone, add='+')
        text.bind('<<Change>>', notdone, add='+')

    text.focus()
    text.bind('<F5>', func2)
    text.bind('<Control-s>', saveit)
    text.bind('<Control-o>', openit)
    text.bind('<Control-n>', new)

    # pack_forget()

    frame = gooey.Frame(root1)
    frame.pack(fill=BOTH, side=RIGHT, expand=True)

    textoutput = NotePad(frame)
    textoutput.configure(state='disabled')
    textoutput.pack(fill=BOTH)
    frame_text.textoutput = textoutput
    text.textoutput = textoutput
    root1.textoutput = textoutput

    frame.pack_forget()

    msb = MultiStatusBar(root1)
    msb.setlabel("one", text='© 2019, Prannaya Gupta, Text Editor')
    msb.pack(side=BOTTOM, fill='x')

    text.focus_set()
    root1.bind('<Control-s>', saveit)
    root1.bind('<Control-o>', openit)
    root1.bind('<Control-n>', new)
    root1.bind('<F5>', func2)
    root1.update()

    return text, textoutput, savelocation


# =============================  PyFunction INTERFACE  =============================

def new_func(nb, name=True, done=False):
    if name:
        name = save(title='New PyFunc', filetypes=[('Python Function Files', '.pyf')]).split('/')[-1]
        if not len(name): return
        while not isName(name):
            name = simpledialog.askstring('PyFunc.Error',
                                          f'Name your new function {name} again, the previous was not accepted. Do NOT add the .pyf extension.').strip()
        file = open(f'{name}.pyf', 'w+')
        file.write(f"def {name}():" + '\n\t')
        file.close()

    else:
        name = openfile(title='Open PyFunc', filetypes=[('Python Function Files', '.pyf')]).split('/')[-1][:-4]
        if not len(name): return
        # open(f'{name}.pyf', 'w+').close()

    root1 = ttk.Frame(nb)
    nb.add(root1, text=('Notebox.PyFunc.' + name).center(50))

    def printf(*args, sep=" ", end="\n"):
        bits = sep.join(list(map(str, args))) + end
        textoutput.configure(state='normal')
        textoutput.insert(END, bits)
        textoutput.configure(state='disabled')

    setup = globals()
    setup.update({'print': printf})

    def func2(event=None):
        exec(execute(text.get("1.0", END) + f'{name}()'), setup)
        over = f' EXECUTED {name} '.center(75, '=')
        printf('\n' + over)
        save()

    def saveit(event=None):
        savelocation = open(f'{name}.pyf', 'w+')
        savelocation.write(text.get("1.0", END))
        savelocation.close()

    def new(event=None):
        new_func(nb)

    def openfunc(event=None):
        new_func(nb, False)

    mainframe = gooey.Frame(root1)
    mainframe.pack(fill=BOTH, expand=True)

    frame_text = Frame(mainframe)
    frame_text.pack(fill=BOTH, side=LEFT, expand=True)
    file = open(f'{name}.pyf', 'r')
    text = NotePad(frame_text, True)
    text.insert(INSERT, file.read())
    file.close()
    text.focus()
    text.bind('<F5>', func2)
    text.bind('<Control-s>', saveit)
    text.bind('<<Change>>', saveit, add='+')
    text.bind('<<Configure>>', saveit, add='+')
    text.bind('<Control-n>', new)
    text.bind('<Control-o>', openfunc)
    text.focus_set()

    frame_bottom = Frame(frame_text)
    frame_bottom.pack(side=BOTTOM)
    label_new = Label(frame_bottom, text='© 2019, Prannaya Gupta, Text Editor', font=('Helvetica', 5))
    label_new.pack()

    frame = Frame(mainframe)
    textoutput = NotePad(frame)
    textoutput.configure(state='disabled')
    frame_text.textoutput = textoutput
    text.textoutput = textoutput
    root1.textoutput = textoutput
    frame.pack(fill=BOTH, side=RIGHT, expand=True)


# =============================  PyClass INTERFACE  =============================

def new_class(nb, name=True, done=False):
    if done:
        pass
    elif name:
        name = save(title='New PyClass', filetypes=[('Python Class Files', '.pycl')]).split('/')[-1]
        if not len(name): return
        while not isName(name):
            name = simpledialog.askstring('PyClass.Error',
                                          f'Name your new class {name} again, the previous was not accepted. Do NOT add the .pycl extension.').strip()
        file = open(f'{name}.pycl', 'w+')
        file.write(f"class {name}():" + "\n\n\tpublic static void main():\n\t\t")
        file.close()

    else:
        name = openfile(title='Open PyClass', filetypes=[('Python Class Files', '.pycl')]).split('/')[-1][:-5]
        if not len(name): return

    root1 = ttk.Frame(nb)
    nb.add(root1, text=('Notebox.PyClass.' + name).center(50))

    def printf(*args, sep=" ", end="\n"):
        bits = sep.join(list(map(str, args))) + end
        textoutput.configure(state='normal')
        textoutput.insert(END, bits)
        textoutput.configure(state='disabled')

    setup = globals()
    setup.update({'print': printf})

    def func2(event=None):
        execxt = execute(text.get("1.0", END) + f'{name}.main()')

        def execut():
            excepto = ''
            with stdoutIO() as s:
                try:
                    exec(execxt, setup)
                except Exception as e:
                    excepto = str(e)

            printf(s.getvalue())
            if len(excepto): printf('Error: ', excepto)

        printf(f' Starting Notebox.PyClass.{name} '.center(50, '='))
        try:
            execut()
        # with Thread(target=execute) as t: t.start()
        except Exception as e:
            msg.showerror(f'Error in Notebox.PyClass.{name}', str(e))
        printf(f' Executed Notebox.PyClass.{name} '.center(50, '='))
        save()

    def saveit(event=None):
        savelocation = open(f'{name}.pycl', 'w+')
        savelocation.write(text.get("1.0", END))
        savelocation.close()

    def new(event=None):
        new_class(nb)

    def openclass(event=None):
        new_class(nb, False)

    mainframe = gooey.Frame(root1)
    mainframe.pack(fill=BOTH, expand=True)

    frame_text = Frame(mainframe)
    frame_text.pack(fill=BOTH, side=LEFT, expand=True)

    text = NotePad(frame_text, True)
    file = open(f'{name}.pycl')
    text.insert(INSERT, file.read())
    file.close()
    text.focus()

    def tab(event=None):
        text.insert(CURRENT, '\t')

    text.bind('<F5>', func2)
    text.bind('<Return>', tab)
    text.bind('<Control-s>', saveit)
    text.bind('<<Change>>', saveit, add='+')
    text.bind('<<Configure>>', saveit, add='+')
    text.bind('<Control-n>', new)
    text.bind('<Control-o>', openclass)
    text.focus_set()

    frame = Frame(mainframe)
    textoutput = NotePad(frame)
    textoutput.configure(state='disabled')
    text.textoutput = textoutput
    frame_text.textoutput = textoutput
    root1.textoutput = textoutput
    frame.pack(fill=BOTH, side=RIGHT, expand=True)


# =============================  PyProgram INTERFACE  =============================

def new_prog(nb, name=True):
    if name:
        name = save(title='New PyProg', filetypes=[('Python Programming Files', '.pyprog')]).split('/')[-1]
        if not len(name): return
        file = open(f'{name}.pyprog', 'w+')
        file.write(f"\n\nint main():\n\t")
        file.close()

    else:
        name = openfile(title='Open PyProg', filetypes=[('Python Programming Files', '.pyprog')]).split('/')[-1][:-7]
        if not len(name): return

    root1 = ttk.Frame(nb)
    nb.add(root1, text=('Notebox.PyProg.' + name).center(50))

    def printf(*args, sep=" ", end="\n"):
        bits = sep.join(list(map(str, args))) + end
        textoutput.configure(state='normal')
        textoutput.insert(END, bits)
        textoutput.configure(state='disabled')

    setup = globals()
    setup.update({'print': printf})

    def func2(event=None):
        execxt = text.get("1.0", END) + f'\nmain()'

        def execut():
            excepto = ''
            with stdoutIO() as s:
                try:
                    exec(execute(execxt), setup)
                except Exception as e:
                    excepto = str(e)
                    raise e

            # printf(s.getvalue())
            if len(excepto):
                Beep(200, 500)
                printf('Error: ', excepto)
                return

            excepto = ''
            with stdoutIO() as s:
                try:
                    exec('main()', setup)
                except Exception as e:
                    excepto = str(e)
                    raise e

            printf(s.getvalue())
            if len(excepto): printf('Error: ', excepto)

        printf(f' Starting Notebox.PyProg.{name} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} '.center(75, '='))
        execut()
        # with Thread(target=execute) as t: t.start()
        printf(f' Executed Notebox.PyProg.{name} at {datetime.now().strftime("%d/%m/%Y %H:%M:%S")} '.center(75, '='))
        saveit()

    def saveit(event=None):
        savelocation = open(f'{name}.pyprog', 'w+')
        savelocation.write(text.get("1.0", END))
        savelocation.close()

    def new(event=None):
        new_class(nb)

    def openclass(event=None):
        new_class(nb, False)

    mainframe = gooey.Frame(root1)
    mainframe.pack(fill=BOTH, expand=True)

    frame_text = Frame(mainframe)
    frame_text.pack(fill=BOTH, side=LEFT, expand=True)

    text = NotePad(frame_text, True)
    file = open(f'{name}.pyprog')
    text.insert(INSERT, file.read())
    file.close()
    text.focus()

    def tab(event=None):
        text.insert(CURRENT, '\t')

    text.bind('<F5>', func2)
    text.bind('<Return>', tab)
    text.bind('<Control-s>', saveit)
    text.bind('<<Change>>', saveit, add='+')
    text.bind('<<Configure>>', saveit, add='+')
    text.bind('<Control-n>', new)
    text.bind('<Control-o>', openclass)
    text.focus_set()

    def null(e=None):
        return "break"

    frame = Frame(mainframe)
    textoutput = NotePad(frame)
    textoutput.configure(state='disabled', foreground='#42a5f5')
    textoutput.bind('<Return>', null)
    text.textoutput = textoutput
    frame_text.textoutput = textoutput
    root1.textoutput = textoutput
    frame.pack(fill=BOTH, side=RIGHT, expand=True)


def notebox(filename=None):
    window = gooey.Tk()
    window.state('zoomed')
    # window.resizable(False, False)
    window.minsize(600, 550)
    try:
        window.iconbitmap('NoteBoxIcon.ico')
    except:
        pass
    style = ttk.Style(window)
    style.theme_use('vista')

    if filename is None:
        savelocation = 'untitled'
    else:
        savelocation = filename

    mixer.init()
    resize = BooleanVar(value=False)
    calcval = BooleanVar(value=True)
    window.title('NoteBox')

    def saveas(event=None):
        try:
            tex = event.widget
        except:
            tex = text
        t = tex.get("1.0", "end-1c")
        templocation = save(parent=window, initialdir=fDir, title="Select file to save as:")
        if len(templocation):
            savelocation = templocation
            file1 = open(savelocation, "w+")
            file1.write(t)
            file1.close()
            nb.tab(root, text=('Notebox - ' + savelocation.split('/')[-1]).center(50))
            tex.change_lexer(savelocation.split('.')[-1])
            tex.bind("<<Configure>>", savenow)
            tex.bind("<<Change>>", savenow)
            # nb.tab(root)['text'] = ('Notebox - '+savelocation.split('/')[-1]).center(50)
            # window.title('Notebox - '+savelocation.split('/')[-1])

    def toggle_size():
        boo = resize.get()
        if not boo: window.state('zoomed')
        window.resizable(boo, boo)
        resize.set(not boo)

    hidden = BooleanVar(value=True)
    wrap = BooleanVar(value=True)

    def printf(*args, event=None, sep=" ", end="\n"):
        bits = sep.join(list(map(str, args))) + end
        textoutput.configure(state='normal')
        textoutput.insert(END, bits)
        textoutput.configure(state='disabled')

    setup = globals()
    setup.update({'print': printf})
    globe = StringVar(value=str(setup))

    '''
    def openfile(event=None):
        openlocation = filedialog.openfile(parent=window, initialdir=fDir,title = "Select file to open:")
        if len(openlocation): notebox(openlocation)'''

    def openit(event=None):
        openlocation = openfile(parent=window, initialdir=fDir, title="Select file to open:")
        if len(openlocation):
            noteui(nb, openlocation)
        else:
            noteui(nb, None)

    def opennow(event=None):
        if event is None:
            openit()
        else:
            event.widget.event_generate("<Control-O>")

    def find(event=None):
        event.widget.onFind(event)

    def new(event=None):
        # notebox()
        noteui(nb, None)

    def undo(event=None):
        try:
            text.edit_undo()
        except:
            pass

    def redo(event=None):
        try:
            text.edit_redo()
        except:
            pass

    def saveit(event=None):
        if savelocation == 'untitled':
            t = text.get("1.0", "end-1c")
            templocation = save(parent=window, initialdir=fDir, title="Select file to save as:")
            if len(templocation):
                file1 = open(templocation, "w+")
                file1.write(t)
                file1.close()
                window.title('Notebox - ' + templocation.split('/')[-1])
                window.destroy()
            else:
                MsgBox = msg.askyesnocancel('Exit Application', 'Are you sure you don\'t want to save the notebox?',
                                            icon='warning')
                if MsgBox is None:
                    print('Escaped')
                elif MsgBox:
                    window.destroy()
                else:
                    saveit()
        else:
            MsgBox = msg.askyesnocancel('Exit Application', 'Do you want to save the notebox?', icon='warning')
            if MsgBox is None:
                print('Escaped')
            elif MsgBox:
                save()
            else:
                window.destroy()

    def savenow(event=None):
        if savelocation == 'untitled':
            saveas()
        else:
            text = text if event is None else event.widget
            file = open(savelocation)
            file.write(text.get("1.0", "end-1c"))
            file.close()

    def func2(event=None):
        def execut():
            excepto = ''
            with stdoutIO() as s:
                try:
                    exec(execute(text.get("1.0", END)))
                except Exception as e:
                    excepto = str(e)

            printf(s.getvalue())
            if len(excepto): printf('Error: ', excepto)

        frame.pack()
        hidden.set(False)
        try:
            # t = Thread(target=execute)
            # t.start()
            printf(' Starting Editor '.center(50, '='))
            execut()
        except Exception as e:
            msg.showerror('Error in Editor', str(e))
        printf(' Executed Editor '.center(50, '='))

    def word_wrap(event=None):
        if wrap.get():
            text.config(wrap=NONE)
            xscroll.pack(side=BOTTOM, fill='x')

        else:
            text.config(wrap=WORD)
            xscroll.pack_forget()
        wrap.set(not wrap.get())

    def toggle_show(event=None):
        if hidden.get():
            frame.pack()
        else:
            frame.pack_forget()
        hidden.set(not hidden.get())

    def show(event=None):
        frame.pack()

    def _play():
        # while True:
        mixer.music.load(mDir1)
        mixer.music.play()

    def play_():
        try:
            pygame.mixer.music.unpause()
        except:
            pass

    def pause():
        try:
            mixer.music.pause()
        except:
            pass

    def stop():
        try:
            mixer.music.fadeout(600)
        except:
            pass

    def m1(event=None):
        mixer.music.load(mDir1)
        mixer.music.play()

    def vht(event=None):
        VisualHTnb(nb)

    # Portals (Avengers Endgame, Alan Silvestri, 2019)
    mDir2 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Alan-Silvestri-Portals-_From-_Avengers_-Endgame__Audio-Only_.mp3"
    # Avengers Endgame Trailer 2 Music (2019)
    mDir3 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Avengers-Endgame-Trailer-2-Music-Full-Trailer-Version.mp3"
    # Avengers Infinity War Trailer Music (2018)
    mDir4 = "C:/Users/Prannaya/Documents/Education/NUS High/Year 2/EL2131/Crime Trailer/Avengers-Infinity-War-Trailer-Music.mp3"

    def m2():
        mixer.music.load(mDir2)
        mixer.music.play()

    def m3():
        mixer.music.load(mDir3)
        mixer.music.play()

    def m4():
        mixer.music.load(mDir4)
        mixer.music.play()

    def playm(musicnum):
        mixer.music.load(musicnum)
        mixer.music.play()

    def clear():
        text.delete('1.0', END)

    playlist = ['musix', mDir1, mDir2, mDir3, mDir4]

    def music(event=None):
        tempmusic = openfile(master=window, initialdir=fDir, title="Select your cool music track",
                             filetypes=(("mp3 Music Files", "*.mp3"), ("m4a Music Files", "*.m4a")))
        if len(tempmusic):
            mixer.music.load(tempmusic)
            mixer.music.play()

    def canva():
        canvaa(nb)

    dark = BooleanVar(value=False)

    def GreyMode():
        text.configure(background="#f6f8fa", foreground="black", insertbackground="#0A0806")
        window.tk_setPalette(background='#f6f8fa', foreground='black', activeBackground='grey80')
        text.linenumbers.color = "black"
        text.linenumbers.background = "#f6f8fa"
        text.linenumbers.redraw()

    def DarkMode():
        text.configure(background="#333333", foreground="white", insertbackground="white")
        window.tk_setPalette(background='#333333', foreground='black', activeBackground='grey80')
        text.linenumbers.color = "white"
        text.linenumbers.background = "#333333"
        text.linenumbers.redraw()

    def BrightMode():
        text.configure(background="white", foreground="black", insertbackground="black")
        window.tk_setPalette(background='white', foreground='black', activeBackground='grey80')
        text.linenumbers.color = "black"
        text.linenumbers.background = "white"
        text.linenumbers.redraw()

    def newfunc(event=None):
        new_func(nb)

    def openfunc(event=None):
        new_func(nb, False)

    def newclass(event=None):
        new_class(nb)

    def openclass(event=None):
        new_class(nb, False)

    def newprog(event=None):
        new_prog(nb)

    def openprog(event=None):
        new_prog(nb, False)

    def yout(event=None):
        youtube(nb)

    def oth(event=None):
        othellonb(nb)

    def pia(event=None):
        pianonb(nb)

    window.protocol('WM_DELETE_WINDOW', saveit)

    # window.bind('Undo', undo)

    window.bind('<Control-m>', music)
    # window.bind("<Button-3>",show_menu)

    menubar = Menu(window)

    filemenu = Menu(menubar, tearoff=0)
    filemenu.add_command(label="New", command=new, accelerator='Ctrl-N')
    filemenu.add_command(label="Open", command=openit, accelerator='Ctrl-O')
    filemenu.add_command(label="New PyFunc", command=newfunc)
    filemenu.add_command(label="Open PyFunc", command=openfunc)
    filemenu.add_command(label="New PyClass", command=newclass)
    filemenu.add_command(label="Open PyClass", command=openclass)
    filemenu.add_command(label="New PyProg", command=newprog)
    filemenu.add_command(label="Open PyProg", command=openprog)
    filemenu.add_command(label="New VHT", command=vht)
    filemenu.add_command(label="Canva", command=canva)
    filemenu.add_command(label="Open...", command=opennow)
    filemenu.add_command(label="Save", command=savenow, accelerator='Ctrl-S')
    filemenu.add_command(label="Save As...", command=saveas, accelerator='Ctrl-Shift-S')
    filemenu.add_separator()
    filemenu.add_command(label="Close", command=window.destroy)
    filemenu.add_command(label="Exit", command=window.destroy)
    menubar.add_cascade(label="File", menu=filemenu)

    editmenu = Menu(menubar, tearoff=0)

    def cut(event=None):
        if event is None:
            text.event_generate("<<Cut>>")
        else:
            event.widget.event_generate("<<Cut>>")

    def copy(event=None):
        if event is None:
            text.event_generate("<<Copy>>")
        else:
            event.widget.event_generate("<<Copy>>")

    def paste(event=None):
        if event is None:
            text.event_generate("<<Paste>>")
        else:
            event.widget.event_generate("<<Paste>>")

    def undo(event=None):
        if event is None:
            text.event_generate("<Control-z>")
        else:
            event.widget.event_generate("<Control-z>")

    def backs(event=None):
        if event is None:
            text.event_generate("<Backspace>")
        else:
            event.widget.event_generate("<BackSpace>")

    def google(event=None):
        import webbrowser as wb
        word = text.get('insert wordstart', 'insert wordend')
        url = f'https://www.google.com/search?q={word}'
        wb.open(url)

    def chrome(event=None):
        nb.add(Chromium(nb), text='Chromium'.center(50))

    editmenu.add_command(label="Undo", accelerator='Ctrl+Z', command=undo)
    editmenu.add_separator()
    editmenu.add_command(label="Cut", accelerator="Ctrl+X", command=cut)
    editmenu.add_command(label="Copy", accelerator="Ctrl+C", command=copy)
    editmenu.add_command(label="Paste", accelerator="Ctrl+V", command=paste)
    editmenu.add_command(label="Delete", accelerator='Backspace', command=backs)
    editmenu.add_separator()

    """
    fontmenu = Menu(editmenu, tearoff=0)
    fontmenu.add_command(label="Original", command=FontCN)
    for font in tkinter.font.families():
        exec(f'''
def Font{''.join(font.split())}():
    global text
    text.config(font="{font}")
fontmenu.add_command(label="{font}", command=Font{''.join(font.split())}())''', globals())
    fontmenu.add_command(label="Courier", command=lambda : text.config(font="Courier"))
    fontmenu.add_command(label="Helvetica", command=lambda : text.config(font="Courier"))
    fontmenu.add_command(label="Arial", command=lambda : text.config(font="Courier"))
    fontmenu.add_command(label="Times New Roman", command=FontTNR)
    """
    # editmenu.add_cascade(label="Font", menu=fontmenu)
    editmenu.add_checkbutton(label='Notepad Wrap', command=word_wrap, accelerator='Ctrl-W')
    editmenu.add_command(label='Toggle Python Interpreter', command=toggle_show, accelerator='Ctrl-P')
    editmenu.add_command(label='Clear', command=clear)
    # intmenu.add_radiobutton(label='Hide Python Interpreter', command=unshow)
    menubar.add_cascade(label="Edit", menu=editmenu)
    menubar.add_command(label='Run Python', command=func2, accelerator='F5')

    musicmenu = Menu(menubar, tearoff=0)
    musicmenu.add_command(label='I Feel You (Avengers Infinity War, Alan Silvestri, 2018)', command=m1)
    musicmenu.add_command(label='Portals (Avengers Endgame, Alan Silvestri, 2019)', command=m2)
    musicmenu.add_command(label='Avengers Endgame Trailer 2 Music (2019)', command=m3)
    musicmenu.add_command(label='Avengers Infinity War Trailer Music (2018)', command=m4)
    musicmenu.add_command(label='Open Music File', accelerator='Ctrl-M', command=music)
    musicmenu.add_command(label='(Re)play Music File', command=play_)
    musicmenu.add_command(label='Pause Music File', command=pause)
    musicmenu.add_command(label='Stop Music File', command=stop)
    menubar.add_cascade(label='Play Music', menu=musicmenu)
    menubar.add_command(label='Full Screen', command=toggle_size)

    # widmenu = Menu(menubar, tearoff=0)
    # widmenu.add_command(label='Clock', command=clock)
    # widmenu.add_command(label='Calendar', command=cal)
    # widmenu.add_command(label='Calculator', command=toggle_calc)
    # menubar.add_cascade(label='Widgets', menu=widmenu)
    menubar.add_command(label="Canva", command=canva)
    menubar.add_command(label="Othello", command=oth)
    menubar.add_command(label="Piano", command=pia)
    # menubar.add_command(label="Chromium", command=chrome)

    modemenu = Menu(menubar, tearoff=0)
    modemenu.add_command(label="Dark Mode", command=DarkMode)
    modemenu.add_command(label="Bright Mode", command=BrightMode)
    modemenu.add_command(label="Grey Mode", command=GreyMode)
    menubar.add_cascade(label='Modes', menu=modemenu)

    helpmenu = Menu(menubar, tearoff=0)

    def About():
        msg.showinfo('NoteBox - About',
                     '''The NoteBox is a piece of simple software that can be used in the place of Notepad. This is very importan, since Notepad is one of the best and most influential text editors as of current. To be said, NoteBox is way more intuitive, but I would like to bring along a way simpler version of Notepad with lesser functions but made in just a few days using Python 3.7.2. We hope ypu will enjoy this platform. Thank you!''')

    helpmenu.add_command(label='About NoteBox', command=About)
    menubar.add_cascade(label="Help", menu=helpmenu)

    window.config(menu=menubar)

    nb = CustomNotebook(window)
    # text, textcode, textoutput, savelocation = noteui(nb, filename)
    root = ttk.Frame(nb)
    nb.add(root, text='Textpad'.center(50))

    # chrome()
    # canvaa(nb)
    # nb.add(wids, text='Widgets'.center(50))
    # nb.add(wall, text='New Tab'.center(50))
    nb.pack(fill=BOTH, expand=1)

    if savelocation == 'untitled':
        nb.tab(root, text='NoteBox - untitled'.center(50))
    else:
        nb.tab(root, text=('Notebox - ' + savelocation.split('/')[-1] + ' - (' + savelocation + ')').center(50))

    frame_text = gooey.Frame(root)
    frame_text.pack(fill=BOTH, side=LEFT, expand=True)

    window.bind('<Control-e>', google)

    label = Label(frame_text, text='Editor', fg="red", font=('Trebuchet MS', 15))
    label.pack()

    text = NotePad(frame_text, True)
    xscroll = Scrollbar(frame_text, orient=HORIZONTAL)
    xscroll.pack(side=BOTTOM, fill='x')
    text.config(xscrollcommand=xscroll)
    # self.font = tkFont.Font(family=self.family, size=self.size)
    # text.config(font=text.font)
    xscroll.pack_forget()
    # , True
    # text.grid()
    # text.pack(fill=BOTH, side=RIGHT, expand=True)
    # text.place(x = 1, y = 0, height = 993, width = 1925)
    if filename != None:
        try:
            file = open(filename, 'r')
        except:
            file = open(filename, 'rb')
        text.insert(END, file.read())
        file.close()
        text.change_lexer(filename.split('.')[-1])
        text.config(font=text.font)

    text.focus()
    text.bind('<Control-f>', find)
    text.bind('<Control-n>', new)
    text.bind('<Control-o>', openit)
    text.bind('<Control-s>', savenow)
    text.bind('<Control-z>', undo)
    text.bind('<F5>', func2)
    text.bind('<Control-p>', toggle_show)
    text.bind('<Control-w>', word_wrap)
    text.bind('<Control-Shift-KeyPress-S>', saveas)
    text.bind('<Control-Shift-KeyPress-Z>', redo)

    # pack_forget()

    frame = gooey.Frame(root)
    frame.pack(fill=BOTH, side=RIGHT, expand=True)

    textoutput = NotePad(frame)
    textoutput.pack(fill=BOTH, expand=1)
    text.textoutput = textoutput
    frame_text.textoutput = textoutput
    root.textoutput = textoutput

    frame.pack_forget()

    frame_bottom = Frame(frame_text)
    frame_bottom.pack(side=BOTTOM)

    label_new = Label(frame_bottom, text='© 2019, Prannaya Gupta, Text Editor', font=('Helvetica', 5))
    label_new.pack()

    window.wait_visibility()

    # while True:
    # mixer.music.load(mDir1)
    # mixer.music.play()
    '''
    sleep(100)
    mixer.music.load(mDir5)
    mixer.music.play()
    sleep(100)
    mixer.music.load(mDir6)
    mixer.music.play()
    sleep(100)
    mixer.music.load(mDir4)
    mixer.music.play()'''

    window.mainloop()

    """
    for font in tkinter.font.families():
        exec(f'''
    def Font{''.join(font.split())}():
        global text
        text.config(font="{font}")
    fontmenu.add_command(label="{font}", command=Font{''.join(font.split())}())''', globals())"""


Thread(target=notebox()).start()
"""
class EmailTK(Frame):
    
    def __init__(self, master):
        from envelopes import GMailSMTP
        super().__init__(master)
        master.withdraw()
        self.email, self.psw = GetUserNamePassword(self, title='Login').result
        self.smtp = GMailSMTP(self.email, self.psw)
        master.deiconify()
        self.log = Frame(self)
        self.log.pack(fill=BOTH)
        Label(self.log, text='Send Emails').pack(side=LEFT)
        self.emails = Entry(self.log)
        self.emails.pack(side=LEFT)
        self.subf = Frame(self)
        Label(self.subf, text='Subject').grid(row=0)
        self.sub = Entry(self.subf)
        self.sub.grid(row=0, column=1)
        self.subf.pack(fill=BOTH)
        self.mainframe = Frame(self)
        Label(self.mainframe, text='Enter Message Below').pack(side=TOP)
        self.message = NotePad(self.mainframe, True)
        Button(self.mainframe, command=self.sendit).pack(side=BOTTOM)
        self.mainframe.pack(side=RIGHT, fill=BOTH)

    def sendit(self):
        from envelopes import Envelope
        envelope = Envelope(
            from_addr=self.email,
            to_addr=self.emails.get(),
            subject=self.sub.get(),
            text_body=self.message.get('1.0', END))
        self.smtp.send(envelope)

root = Tk()
EmailTK(root).pack()
root.mainloop()
"""
