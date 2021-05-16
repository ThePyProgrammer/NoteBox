#HTMLEditor
#insert video f"""<iframe width="560" height="315" src="{video_url}" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>"""

from tkinter import *
from widgets import *
from tkinter import ttk

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

<h1>My First Heading in Visual HyperText</h1>
<p>My first paragraph in Visual HyperText.</p>

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
        except: pass
        

    def setfile(self, filename):
        self.html.setfile(filename)
        self.text.delete("1.0", END)
        with open(filename) as file: self.text.insert("1.0", file.read())

    def seturl(self, url):
        self.html.seturl(url)
        self.text.delete("1.0", END)
        self.text.insert("1.0", urlopen(url).read().decode())

