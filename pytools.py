import sys
import pyphp as php
from msvcrt import getch, getche
import re
import pyduktape
import sympy
import click
import os, glob
import jispy
import six, platform
from time import sleep as s
import subprocess
import smtplib 
from googlesearch import *
import webbrowser as wb
import requests, json
import win32com.client as wincl
import urllib.parse
from pyforest import *
from random import *
from sympy import *
from math import *
from turtle import *
from urllib.request import urlopen
import numpy as np
from bs4 import BeautifulSoup
import webbrowser as wb
import requests, json
import win32com.client as wincl
import pafy
import lxml
from tkinter import *
from lxml import etree
from google_currency import convert
from google_trans import Translator
import urllib
from fractions import Fraction
from decimal import Decimal
from array import *
from pprint import pprint
from bisect import bisect_right, bisect_left
from googlesearch import search_images as images
from googlesearch import search_news as news
from googlesearch import search_videos as videos
from googlesearch import search_shop as shop
from googlesearch import search_books as books
from googlesearch import search_apps as apps
from games import *
from munprog import actual_mun
from plotting import *
from import_run import *
from Docs import documentation
from CeusGuru import lesson as learn
from time import time as nowtime
from time import sleep 
from calendar import month
from winsound import Beep
from turtle import *
import webbrowser as wb
from stdout import stdoutIO
from google_trans import Translator
from google_currency import convert
#from cpp2python import *

def inp(prompt, type=str):
    return eval(f"{type}(input({prompt}))")

# as stuff
rand = randint
c = choice
choose = choice
shf = shuffle
Dec = Decimal
Frac = Fraction
jsonprint = pprint
br = bisect_right
bl = bisect_left
s = sleep
beep = Beep

real_path = rp = rd = real_dir = os.path.dirname(os.path.realpath(__file__))
# new
translator = Translator()
def globe():
    glob = dict(globals())
    glob.update(locals())
    return glob

mainjs = pyduktape.DuktapeContext()
def js(file):
    return mainjs.eval_js_file(file)

def jseval(code, glob=None):
    if glob != None: mainjs.set_globals(**glob)
    return mainjs.eval_js(code)


class Random:
    def randint(minval, maxval):
        '''
returns randint - similar to random.randint
        '''
        return list(np.random.randint(minval, maxval+1, 1))[0]

    def randints(minval, maxval, num):
        '''
returns multiple randints - similar to random.randint
        '''
        return list(np.random.randint(minval, maxval+1, num))

    def randnormdis(mean, std, num):
        return list(np.random.normal(mean, std, num))

class double(float): pass

class system1:
    def __init__(self):
        self.inp = sys.stdin
    class output:
        def println(self, text):
            print(text)
    out = output()

def input(prompt='', type=None):
    if type is None: return input(prompt)
    return inp(prompt, str(type))

class char:
    def __init__(self, value):
        if type(value) == int: self.string = chr(value)
        if type(value) == str: self.string = value

    def isLetter(self): return self.string.isalpha()
    def isDigit(self): return self.string.isdigit()
    def isWhitespace(self): return self.string.isspace()
    def isUpperCase(self): return self.string.isupper()
    def isLowerCase(self): return self.string.islower()
    def toUpperCase(self): return self.string.upper()
    def toLowerCase(self): return self.string.lower()
    def __str__(self): return self.string

class Scanner:
    def __init__(self, val=sys.stdin):
        if val != sys.stdin:
            raise ValueError('Invalid Input in Scanner Object')

    nextInt = lambda self: input('', int)
    nextByte = lambda self: input().encode()
    nextLine = lambda self: input()
    next = lambda self: input()
    nextBoolean = lambda self: bool(input())
    nextFloat = lambda self: input('', float)
    nextDouble = lambda self: double(input())
    nextEvaluate = lambda self: eval(input('>>> '))
    nextChar = lambda self: char(msvcrt.getche())
    def nextExecute(self):
        exec(execute(input('>>> ')))
        return 
    def nextCommand(self):
        os.system(input(os.getcwd()+'>'))
        return 

readLine = input

languages = {
    'afrikaans': 'af',
    'arabic': 'ar',
    'belarusian': 'be',
    'bulgarian': 'bg',
    'catalan': 'ca',
    'czech': 'cs',
    'welsh': 'cy',
    'danish': 'da',
    'german': 'de',
    'greek': 'el',
    'english': 'en',
    'esperanto': 'eo',
    'spanish': 'es',
    'estonian': 'et',
    'persian': 'fa',
    'finnish': 'fi',
    'french': 'fr',
    'irish': 'ga',
    'galician': 'gl',
    'hindi': 'hi',
    'croatian': 'hr',
    'hungarian': 'hu',
    'indonesian': 'id',
    'icelandic': 'is',
    'italian': 'it',
    'hebrew': 'iw',
    'japanese': 'ja',
    'korean': 'ko',
    'latin': 'la',
    'lithuanian': 'lt',
    'latvian': 'lv',
    'macedonian': 'mk',
    'malay': 'ms',
    'maltese': 'mt',
    'chinese (simplified)': 'zh-CN',
    'chinese (traditional)': 'zh-TW'
}

def translate(text=None, src=None, dest=None):
    if text == None:
        text = ''
        print('Enter Text:')
        while True:
            ui = input()
            if ui.lower() == 'end': break
            text += ui+'\n'

    if src == None or dest == None:
        print('\nPossible Languages are: \n\t-', '\n\t-'.join(list(languages.keys())))

    if src == None:
        if input('Would you like to use English as a source language? [y/n]: ').strip()[0] == 'y':
            src = 'en'
        else:
            src = languages[input('Enter source language: ').lower()]
    if dest == None:
        if input('Would you like to use English as a destination language? [y/n]: ').strip()[0] == 'y':
            src = 'en'
        else:
            src = languages[input('Enter destination language: ').lower()]
    return translator.translate(text, src, dest).text
    

class CurrencyError(Exception): pass
def currency(value=None, fro=None, to=None):
    if value == None: value = eval(input('Enter value: '))
    if fro == None: fro = input('Enter source currency: ')
    if to == None: fro = input('Enter destination currency: ')
    fro = fro.lower()
    to = to.lower()
    converted = json.loads(convert(fro, to, value))
    if converted["converted"]:
        return converted["amount"]
    else:
        raise CurrencyError('Inputted currency(s) are undefined.')


    


class gets:
    def __init__(self):
        self.input = input()+'\n'

    def __repr__(self):
        return self.input
    @staticmethod
    def chomp():
        return input()
    def to_i():
        return int(input())

class Console:
    @staticmethod
    def WriteLine(text, *args):
        if len(args): text = text.format(*args)
        print(text)

    @staticmethod
    def ReadLine(text=''):
        return input(text)

class jsmath:
    E = e
    LN2 = log(2)
    LN10 = log(10)
    LOG2E = log2(e)
    LOG10E = log10(e)
    PI = pi
    abs = lambda self, val: fabs(val)
    acos = lambda self, val: acos(val)
    asin = lambda self, val: asin(val)
    atan = lambda self, val: atan(val)
    atan2 = lambda self, val: atan2(val)
    ceil = lambda self, val: ceil(val)
    cos = lambda self, val: cos(val)
    atan2 = lambda self, *args: atan2(*args)
    cos = lambda self, val: cos(val)
    exp = lambda self, val: exp(val)
    floor = lambda self, val: floor(val)
    log = lambda self, val: log(val)
    max = lambda self, *args: max(*args)
    min = lambda self, *args: min(*args)
    pow = lambda self, x, y: pow(x, y)
    random = lambda self: random()
    round = lambda self, val: round(val)
    sin = lambda self, val: sin(val)
    tan = lambda self, val: tan(val)
    sqrt = lambda self, val: sqrt(val)

Math = jsmath()

prompt = lambda string: eval(textinput('JS Prompt', string))
def alert(string):
    messagebox.showinfo("JS Alert", string)

confirm = lambda string: bool(messagebox.askokcancel("JS Confirm", string) != None)

class Convert:
    @staticmethod
    def ToInt32(val):
        return int(val)
    def ToBoolean(val):
        return bool(val)
    def ToDouble(val):
        return double(val)
    def ToStr(val):
        return str(val)
    def ToList(val):
        return list(val)
    def ToFloat(val):
        return float(val)

class arr:
    def __init__(self, *args):
        self.list = args
    def __str__(self): return [str(i) for i in self.list]
    def __int__(self): return [int(i) for i in self.list]
    def __float__(self): return [float(i) for i in self.list]

def align(*args):
    rangen = sorted(args, key=lambda ds: len(list(ds)))
    s = []
    finaln = len(rangen[0])
    for i in range(finaln):
        for j in args:
            s += [j[i]]
    for i in rangen:
        s += [i[finaln:]]
    return s
    
class NoteError(Exception): pass
class mynote:
    def __init__(self, file=None, docstr=None):
        self.cnt = 0
        if file == docstr == None:
            docstr = ''
            name = input('Please enter the name of this note:\n\t')
            print('\t'+'_'*len(name))
            while True:
                ui = input()
                if ui.upper() == 'END': break
                docstr += ui + '\n'

        elif docstr == None:
            name = file[::-1][file.find('.')+1:][::-1]
            infile = open(file, 'r')
            docstr = infile.read()
            file.close()

        elif file == None:
             name = '<enter heading>'

        else: name = file[::-1][file.find('.')+1:][::-1]

        self.file = file
        self.note = docstr
        self.name = name
        self.final = '\n\n'.join([self.name, self.note])
        self.lines = docstr.split('\n')
        
    def __len__(self): return len(self.final)
    def __str__(self): return self.final
    
    def write(self, *args, sep='\n', end='\n', startline=None, move=True):
        docstr = (str(sep).join(str(arr(*args))) + str(end)).split('\n')
        if startline == None: startline = len(self.lines)+1
        starline -= 1
        if move and startline < self.cnt: self.cnt = startline
        notern = self.lines
        self.lines = self.lines[:startline] + docstr + self.lines[startline:]
        self.note = '\n'.join(self.lines)
        self.final = '\n\n'.join([self.name, self.note])
        
    def add(self):
        docstr = '\n'
        while True:
            ui = input()
            if ui.upper() == 'END': break
            docstr += ui + '\n'
        self.note += docstr
        self.final = '\n\n'.join([self.name, self.note])
        self.lines = docstr.split('\n')
        
    def append(self, *args, sep='\n', end='\n', move=True):
        docstr = (str(sep).join(str(arr(*args))) + str(end)).split('\n')
        if move: self.cnt = len(self.lines)
        self.lines = self.lines+docstr
        self.note = '\n'.join(self.lines)
        self.final = '\n\n'.join([self.name, self.note])

    def read(self): return self.final
    def cursor(self): return self.cnt+1
    def readline(self, index=None):
        if index == None:
            index = self.cnt
            self.cnt += 1
        return self.lines[index]
    def readlines(self): return self.lines
    def save(self, file=None):
        if file == self.file == None: raise NoteError('File is in standard form. It cannot be transferred into a file. Please give a filename instead. Thank you.')
        if file == None: file = self.file
        outfile = open(file, 'w+')
        outfile.write(self.note)
        outfile.close()

    def update(self, file=None):
        if self.file == file == None: raise NoteError('File is in standard form. It cannot be editted from a file. Please give a filename instead. Thank you.')
        if file == None: file = self.file
        name = file[::-1][file.find('.')+1:][::-1]
        infile = open(file, 'r')
        docstr = infile.read()
        file.close()

        self.file = file
        self.note = docstr
        self.name = name
        self.final = '\n\n'.join([self.name, self.note])
        self.lines = docstr.split('\n')

    def __iadd__(self, other):
        if type(other) == mynote: self.note += other.note
        else: self.note += str(other)
        self.final = '\n\n'.join([self.name, self.note])
        self.lines = docstr.split('\n')

    def __add__(self, other):
        if type(other) == mynote: return mynote(docstr=self.note+other.note)
        else: return mynote(docstr=self.note+str(other))

    def __radd__(self, other):
        if type(other) == mynote: return mynote(docstr=other.note+self.note)
        else: return mynote(docstr=str(other)+self.note)

    def __del__(self):
        if self.file == None: print(self.final, '\nPlease store this somewhere if you need it any other point.')
        else:
            outfile = open(file, 'w+')
            outfile.write(self.note)
            outfile.close()

    def rename(self, name):
        self.name = name
        self.final = '\n\n'.join([self.name, self.note])

    def new(self, value, **kwargs):
        if type(value) == mynote:
            self.file = other.file
            self.note = other.note
            self.name = other.name
            self.final = '\n\n'.join([self.name, self.note])
            self.lines = self.note.split('\n')
        else:
            sep = kwargs['sep'] if 'sep' in kwargs else '\n'
            end = kwargs['end'] if 'end' in kwargs else '\n'
            self.note = value
            self.final = '\n\n'.join([self.name, self.note])
            self.lines = value.split('\n')

class MementoError(Exception): pass
class mementoes:
    def __init__(self, *args):
        if len(args):
            self.mementos = args
        else:
            docstr = ''
            while True:
                ui = input()
                if ui.upper() == 'END': break
                docstr += ui + '\n'
            self.mementos = [docstr]
    def new(self, *args): self.mementos += args

    def __len__(self): return len(self.mementoes)

    def __getitem__(self, index):
        if type(index) != int: raise MementoError('Invalid Index. Not type int. Lol.')
        if index > len(self.mementoes): raise MementoError('Invalid Index. Too large. Lol.')
        if index < 1: raise MementoError('Invalid Index. Too small. Lol.')
        return self.mementoes[index-1]

    def __setitem__(self, index, memento):
        if type(index) != int: raise MementoError('Invalid Index. Not type int. Lol.')
        if index > len(self.mementoes): raise MementoError('Invalid Index. Too large. Lol.')
        if index < 1: raise MementoError('Invalid Index. Too small. Lol.')
        self.mementoes[index-1] = memento

    def __delitem__(self, index):
        if type(index) != int: raise MementoError('Invalid Index. Not type int. Lol.')
        if index > len(self.mementoes): raise MementoError('Invalid Index. Too large. Lol.')
        if index < 1: raise MementoError('Invalid Index. Too small. Lol.')
        del self.mementoes[index-1]
        
class document:
    @staticmethod
    def write(text):
        print(text)

def define(name, value):
    if type(value) == str: value = f"""\'{value}\'"""
    return name + f" = {value}"

def inheritant(name, cls):
    exec(f"class {name}({cls}): pass")

System = system1()

class print_funcs:
    '''
    This class is to show all the different functionalities available in our disposal. Take the following code.
        prints("Hello")
        echo "Hello"
        print "Hello"
        puts "Hello"
        print("Hello", end="")
        printf("Hello\n")
        Console.WriteLine("Hello")
        System.out.printIn("Hello")
        document.write("Hello")

    The output is
        "Hello"
        Hello
        HelloHello
        HelloHello
        Hello
        Hello
        Hello
    Hope this clears it up a bit.
    '''

class C:
    digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    whitespace = [' ', '\t', '\n', '\v', '\f', '\r']
    punctuation = """! " # $ % & ' ( ) * + , - . / : ; < = > ? @ [ \ ] ^ _ ` { | } ~""".split()
    lowercase = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    uppercase = 'A B C D E F G H I J K L M N O P Q R S T U V W X Y Z'.split()
    alphabetic = letters = lowercase + uppercase
    alphanumeric = digits+letters
    graphical = alphanumeric + punctuation
    printable = graphical + whitespace
    control = ['0o0'+'0'*abs(len(str(i))-2)+str(i) for i in range(38)]+ ['177']
    blank = whitespace[:2]
    
    @staticmethod
    def system(string):
        os.system(string)
    def strcpy(var1, var2):
        exec(f'{var1} = {var2}')
    def isxdigit(char):
        try:
            int(char, 16)
            return True
        except: return False
    def putchar(char):
        print(char[0])
    def toupper(char):
        return char.upper()
    def tolower(char):
        return char.lower()
    def isspace(char):
        return (char[0] in whitespace)
    def ispunct(char):
        return (char[0] in punctuation)
    def isprint(char):
        return (char[0] in printable)
    def islower(char):
        return (char[0] in lowercase)
    def isupper(char):
        return (char[0] in uppercase)
    def isgraph(char):
        return (char[0] in graphical)
    def isdigit(char):
        return (char[0] in digits)
    def iscntrl(char):
        return (char[0] in control)
    def isdigit(char):
        return (char[0] in digits)
    def isalpha(char):
        return (char[0] in letters)
    def isalnum(char):
        return (char[0] in alphanumeric)
    def atof(string):
        try: return float(string)
        except: raise TypeError('String object cannot be converted to a float')
    def atoi(string):
        try: return int(string)
        except: raise TypeError('String object cannot be converted to an int')
    def atol(string):
        try: return int(string)
        except: raise TypeError('String object cannot be converted to a long int')
    def atol(string):
        try: return int(string)
        except: raise TypeError('String object cannot be converted to a long int')
    def abs(integer):
        return abs(integer)
    def labs(integer):
        return abs(integer)
    def bsearch(key, base, nitems=None, size=32, compar=lambda i, j: i-j):
        if base[bl(base, key)] == key: return key
        return 
    def qsort(base, nitems=None, size=32, compar=lambda i:i):
        return sorted(base, key=compar)

    class div:
        def __init__(self, numer, denom):
            self.quot = numer//denom
            self.rem = numer%denom
    class ldiv(div):pass
    def sizeof(func):
        if func == int: return 32
    def rand():
        return randint(0, 10000000000000000000000000000000000000000000)
    
class double(float): pass
NULL = None

def open_web(filename):
    '''
    Open file on the web. Go to the directory using cd. Filename should be file.
    '''
    wb.open(f"{os.getcwd()}\\{filename}")
    return 
        
# Pyinfo
class Python:
    def __init__(self):
        self.python = '''--------------------------------------------------------------
What is Python?
Python is a popular programming language. It was created by Guido van Rossum, 

and released in 1991.

It is used for:
 -  web development (server-side), 
 -  software development, 
 -  mathematics,
 -  system scripting.

--------------------------------------------------------------
What can Python do?

 -  Python can be used on a server to create web applications.
 -  Python can be used alongside software to create workflows.
 -  Python can connect to database systems. It can also read and modify files.
 -  Python can be used to handle big data and perform complex mathematics.
 -  Python can be used for rapid prototyping, or for production-ready software development.

--------------------------------------------------------------
Why Python?

 -  Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
 -  Python has a simple syntax similar to the English language.
 -  Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
 -  Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
 -  Python can be treated in a procedural way, an object-orientated way or a functional way.

--------------------------------------------------------------
Python Syntax compared to other programming languages

 -  Python was designed for readability, and has some similarities to the English language with influence from mathematics.
 -  Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
 -  Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.
--------------------------------------------------------------'''
        [self.none1, self.what, self.capability, self.why, self.syntax, self.none2] = self.python.split('--------------------------------------------------------------')
        self.copyright = copyright
        self.credits = credits
        self.license = license
        self.help = help
        self.mathopers = '''
    |    a + b ==> a plus b
    |    c - d ==> c minus d
    |    e * f ==> e times f
    |    g / h ==> g exact divided by h
    |    g //h ==> g int divided by h
    |    g % h ==> g(mod h)
        '''

#Type Manipulation
strit = lambda lst: ''.join([str(i) for i in lst])
def reverse(x):
    return x[::-1] if type(x) == list else int(str(x)[::-1])
ispalindrome = lambda x: bool(reverse(x) == x)
flip = lambda i, lst: lst[:i]+lst[i:][::-1]
def equal(lst):
    k = i[0]
    for i in lst:
        if i != k: return False
    return True

#Important stuff:
dl = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
alphabet = [chr(i) for i in range(65, 91)]
alphstr = strit(alphabet)
puctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''


# Temperature
tempcon_fc = lambda farenheit: (5 / 9) * (fahrenheit - 32)
tempcon_cf = lambda celsius: ((9 / 95) * celsius) + 32
tempcon_ck = lambda celsius: celsius+273
tempcon_kc = lambda kelvin: kelvin-273
tempcon_kf = lambda kelvin: tempcon_cf(tempcon_kc(Kelvin))
tempcon_fk = lambda farenheit: tempcon_ck(tempcon_fc(farenheit))

#Mathematics
average = lambda lst: sum(lst)/len(lst)

cos_rule = lambda b, c, theta, rad=True: (b**2 + c**2 + 2*b*c*cos(theta))**0.5 if rad else (b**2 + c**2 + 2*b*c*cos(degrees(theta)))**0.5

class Matrixclass:
    def __init__(self, arg, undef=True):
        self.matr = list(arg)
        self.matrix = np.array(self.matr)

    def ch_matr(self, arg, undef=True):
        self.matr = arg if undef else list(arg)
        self.matrix = np.array(self.matr)

    def index_matrix(self, ind=1):
        self.matr = [i*[0] + [1]+(ind-1-i)*[0] for i in range(ind)]
        self.matrix = np.array(self.matr)

    def ch_val(self, row_ind, col_ind, val):
        self.matr[row_ind-1][col_ind-1] = val
        self.matrix = np.array(self.matr)

    def ch_row(self, row_ind, *args):
        self.matr[row_ind-1][:len(args)] = args
        self.matrix = np.array(self.matr)

    def ch_col(self, col_ind, *args):
        for i in range(len(args)):
            self.matr[i][col_ind-1] = args[i]
        self.matrix = np.array(self.matr)

    def ch_all(self, func):
        vectorized_func = np.vectorize(func)
        self.matrix = vectorized_func(self.matrix)
        self.matr = list(self.matrix)

    def add(self, undef=True, ret=False, *args):
        args = [self.matrix] + [np.array(i) for i in args] if undef else [self.matrix] + args
        val = np.add(*args)
        if ret:
            return val
        self.matrix = val
        self.matr = list(val)

    def subtract(self, arg, undef=True, ret=False):
        val = np.subtract(self.matrix, np.array(arg)) if undef else np.subtract(self.matrix, arg)
        if ret:
            return val
        self.matrix = val
        self.matr = list(self.matrix)

    def mult(self, undef=True, *args):
        args = [np.array(i) for i in args] if undef else args
        val = np.dot(self.matrix, *args)
        self.matrix = val
        self.matr = list(val)

    def initialise(self):
        self.row = len(self.matr)
        self.col = len(self.matr[0])
        self.shape = self.matrix.shape
        self.size = self.matrix.shape
        self.ndim = self.matrix.ndim
        self.minval = np.min(self.matrix)
        self.maxval = np.max(self.matrix)
        self.mean = np.mean(self.matrix)
        self.std = np.std(self.matrix)
        self.variance = np.var(self.matrix)
        self.det = np.linalg.det(self.matrix)
        self.isSingular = bool(self.det == 0)
        self.inv = None if self.isSingular and self.row != self.col else np.linalg.inv(self.matrix)

def Matrix(arg, undef=True, zero=False, index=False):
    if zero:
        # Given arg is a tuple denoting order of the zero matrix
        zeromatrix = Matrixclass([[0 for i in range(arg[1])] for i in range(arg[0])])
        return zeromatrix
    if index:
        # Given arg is the size of the square
        indexmatrix = Matrixclass([i*[0] + [1]+(arg-1-i)*[0] for i in range(arg)])
        indexmatrix.initialise()
        return indexmatrix
    mymatrix = Matrixclass(arg, undef)
    mymatrix.initialise()
    return mymatrix

class Vector:
    def __init__(self, *args):
        self.col = np.array([[i] for i in args])
        self.row = np.array(args)
        self.vec = args
        self.mag = sum([i**2 for i in args]) ** 0.5
        if len(args) == 2:
            self.theta = atan(args[1]/args[0])

    def add(self, undef=False, ret=True, *args):
        if ret: return Vector(tuple(np.add(self.row, *[np.array(i) if undef else i for i in args])))
        self.row = np.add(self.row, *[np.array(i) if undef else i for i in args])
        self.col = np.array([[i] for i in list(self.row)])
        self.mag = sum([i**2 for i in list(self.row)]) ** 0.5

    def __add__(self, other):
        lst = []
        selfbigger = bool(len(self.vec) > len(other.vec))
        for i in range(max(len(self.vec), len(other.vec))):
            try:
                lst.append(self.vec[i]+other.vec[i])
            except:
                lst.append(self.vec[i] if selfbigger else other.vec[i])
        return Vector(*lst)

class Stat:
    def __init__(self, *args):
        self.lst = args

        self.arr = np.array(args)
        
        self.mean = sum(self.lst)/len(self.lst)

        self.nums = sorted(list(set(self.lst)))
        self.frequency = dict([(i, self.lst.count(i)) for i in self.nums])
        
        maxy = None
        for i in self.nums:
            if self.lst.count(i) > self.lst.count(maxy): maxy = i
        self.mode = maxy

        self.median = self.lst[len(self.lst)//2] if len(self.lst)%2 else average(self.lst[len(self.lst)//2-1:len(self.lst)//2+1])

        self.std = np.std(self.arr)
    def __repr__(self):
        return self.arr

def freqStat(ref):
    if type(list(ref.keys())[0]) == str:
        keys = [average([int(j) for j in i.split("-")]) for i in list(ref.keys())]
    else:
        keys = [int(i) for i in list(ref.keys())]
    lst = []
    for i in range(len(keys)):
        lst += [keys[i] for j in range(list(ref.values())[i])]
    return Stat(*lst)
    

class Geo_Info:
    circum = lambda self, d: pi*d
    circarea = lambda self, r: r*r*pi

    traparea = lambda self, upper, lower, h: 0.5*(upper+lower) * h

    spherevol = lambda self, r: (4/3)*pi*(r**3)
    sphereSA = lambda self, r: 4*circarea(r)

    cylvol = lambda self, r, h: circarea(r)*h
    cylSA = lambda self, r, h: circum(r)*(r+h)

    pyrarea = lambda self, ba, h: (1/3) * ba * h

    regpolyarea = lambda self, n, s: (n*(s**2)) / (4 * (tan(pi/n)))


class Quadratics:
    def __init__(self, a):
        self.a = a

    def solveQuadraticabc(self, b, c):
        return (-b + ((b**2) - (4*self.a*c))**(1/2))/(2*self.a), (-b - ((b**2) - (4*self.a*c))**(1/2))/(2*self.a)

    def solveQuadraticahk(self, h, k):
        return solveQuadraticabc(-2*self.a*h, self.a*h**2+k)

class get_primes:
    def __init__(self, n):
        numbers = set(range(n, 1, -2)) if n % 2 else set(range(n-1, 1, -2))
        primes = []
        while numbers:
            p = numbers.pop()
            primes.append(p)
            numbers.difference_update(set(range(p, n+1, 2*p)))
        self.primes = primes


def primes(n):
    numbers = set(range(n, 1, -2)) if n % 2 else set(range(n-1, 1, -2))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(set(range(p, n+1, 2*p)))
    return primes

class Sheldon:
    primes = get_primes(10000000).primes
    def primeproperty(self, primelst=primes):
        rel = []
        for i in range(len(primelst)):
            prime = primelst[i]
            lstprime = [int(x) for x in str(prime)]
            multiply = 1
            for j in lstprime:
                multiply *= j
            if multiply == (i+1):
                rel.append(prime)
        self.primeprop = rel
        return rel

    def reverseproperty(self, primelst=primes):
        rel = []
        for i in primelst:
            if reverse(i) in primelst:
                if primelst.index(reverse(i)) + 1 == reverse(primelst.index(i)+1):
                    rel.append(i)
        self.reverseprop = rel
        return rel


class NUMTypes:
    def __init__(self, num):
        self.num = num
    isBinpalind = lambda self: ispalindrome(int(bin(self.num)[2:]))
    
    SheldonConjecture = Sheldon()
    primes = Sheldon().primes

class baseconv:
    # Bases: Bin, Dec, Oct, Hex
    # Max base: 36
    def ubconv(self, num, currbase, wantbase):
        num = num.upper()
        opp = num[::-1]
        decnum = 0
        for i in range(len(opp)):
            currnum = opp[i]
            if ord(currnum) in list(range(65, 91)):
                currnum = ord(currnum)-55
            decnum += int(currnum) * (currbase**i)
        wantnum = ''
        while len(decnum):
            decnum, rem = decnum//wantbase, decnum%wantbase
            rem = chr(rem+55) if rem > 9 else str(rem)
            wantnum = rem + wantnum
        return wantnum

    decbin = lambda self, decimal: ubconv(decimal, 10, 2)
    decoct = lambda self, decimal: ubconv(decimal, 10, 8)
    dechex = lambda self, decimal: ubconv(decimal, 10, 16)

    binoct = lambda self, binary: ubconv(binary, 2, 8)
    bindec = lambda self, binary: ubconv(binary, 2, 10)
    binhex = lambda self, binary: ubconv(binary, 2, 16)

    octbin = lambda self, octal: ubconv(octal, 8, 2)
    octdec = lambda self, octal: ubconv(octal, 8, 10)
    octhex = lambda self, octal: ubconv(octal, 8, 16)

    hexbin = lambda self, hexadecimal: ubconv(hexadecimal, 16, 2)
    hexoct = lambda self, hexadecimal: ubconv(hexadecimal, 16, 8)
    hexdec = lambda self, hexadecimal: ubconv(hexadecimal, 16, 10)


#Real World
def refractiveIndexi(ai, ar, nr):
    ni = round((nr * sin(radians(ar)) / sin(radians(ai))), 3)
    return ni

def day(d, m, y):
    if m == 1 or m == 2:
        m += 12
        y -= 1
    day = ((13*m+3)//5 + d + y + y//4 - y//100 + y//400) % 7
    dy = dl[day]
    return dy

def caesar(strlet, shift=3):
    string = strlet
    for i in range(len(string)):
        string = string[:i] + chr(ord(string[i])+shift) + string[i+1:] if string[i].upper() not in alphabet[-shift:] else string[:i] + chr(ord(string[i])-26+shift) + string[i+1:]
    return string

def vigenere(keystr, strlet):
    key, string = keystr.upper(), strlet.upper()
    if len(key) > len(string):
        key = key[:len(string)]
    elif len(key) < len(string):
        diffcomps = len(string)//len(key)
        diffparts = len(string) % len(key)
        key = diffcomps*key + key[:diffparts]
    res = ''
    for i in range(len(string)):
        res += alphabet[(alphstr.find(string[i]) + alphstr.find(key[i]))%26]
    for i in range(len(res)):
        if strlet[i].islower():
            res = res[:i] + res[i].lower() + res[i+1:]
    return res

def urldata(url):
    print(urlopen(url).info())
    return

def urlpage(url):
    print(BeautifulSoup(urlopen(url), 'lxml').prettify())
    return 



# Module Manipulation
def import_mod(module, nickname=False, *args):
    if args[0] == 'all':
        exec("from "+module+" import *")
        print("All Funcs Imported from", module)
    elif len(args):
        exec("from "+module+" import "+', '.join(args))
        print("Func"+('s' if len(args)>1 else 'tion'), ', '.join(args), "imported from", module)
    else:
        plus = 'as '+nickname if nickname else ''
        exec("import "+module+plus)
        print(module, "imported", plus)
    return

def ismodule(string):
    try:
        exec('import '+string)
        return True
    except:
        try:
            subprocess.call(['pip', 'install', string])
            return True
        except:
            return False


# Source Coded
def bubble_sort(lst):
    swapped = True
    for iPass in range(len(lst)):
        swapped = False
        for i in range(len(lst)-1-iPass):
            if lst[i] < lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
                swapped = True
        if not(swapped): return lst

def remove_html(string):
    res = ''
    start = 0
    for i in range(len(string)):
        if string[i] == '<': res += string[start:i]
        if string[i] == '>': start = i+1
    return res

#New Funcs
def puts(*args):
    '''
Similar to print, but can function like in Ruby too!
    '''
    print(*args)
    return 

def echo(*args):
    '''
Similar to print, but can function like in PHP too!
    '''
    print(*args)
    return 

def printf(statement):
    '''
The replica of the function in C!
    '''
    print(statement, end='')
    return 

const_ping = lambda num, typestr: 'constantpingyan.substituteadd('+str(num)+', '+typestr+')'

def xrange(*args):
    if len(args) == 1: return range(args[0]+1)
    if len(args) == 2: return range(*[args[i]+i for i in range(2)])
    if len(args) == 3: return range(args[0], args[1]+1, args[2])

rangelst = lambda *args: list(range(*args))
xrangelst = lambda *args: list(xrange(*args))
arange = np.arange
axrange = lambda *args: np.array(xrange(args))

evalinp = lambda obj: eval(input(obj))
def evalinput(*args):
    return eval(input(*args))

rawinput = raw_input = input

null = void = None
true = True
false = False
class string(str): pass
boolean = bool
Infinity = inf

def Function(*args):
    return eval('lambda '+', '.join(args[:-1])+': '+args[-1])

class char(str):
    def __init__(self, string):
        self.string = string[0]
    def __repr__(self):
        return self.string

class unicode(str): pass
unicode.__doc__ = 'A replica of the Python 2 function!'

class Array(np.ndarray):
    def __init__(self, arr):
        super().__init__(np.array(arr))
        self.arr = np.array(arr)

    def __round__(self, n):
        return np.around(self.arr, n)

    def __floor__(self):
        return np.ceil(self.arr)

    def __ceil__(self):
        return np.ceil(self.arr)

    def __trunc__(self):
        return np.trunc(self.arr)

    def __iadd__(self, other):
        self.array = np.add(self.array, other.array)

    def __isub__(self, other):
        self.array = np.add(self.array, -other.array)

    def __int__(self):
        return np.array([int(i) for i in self.lst])

    def __float__(self):
        return np.array([float(i) for i in self.lst])

    def __complex__(self):
        return np.array([complex(i) for i in self.lst])

    def __oct__(self):
        return np.array([int(oct(int(i))[2:]) for i in self.lst])

    def __hex__(self):
        return np.array([eval(hex(int(i))[2:]) for i in self.lst])

    def __str__(self):
        return np.array([str(i) for i in self.lst])

    perm = lambda self: np.random.permutation(self.array)
    shuffle = lambda self: np.random.shuffle(self.array)
    def choice(self, size=None, replace=False, p=None):
        if size == None: return np.random.choice(self.array, replace=replace) if p == None else np.random.choice(self.array, replace=replace, p=p)
        return np.random.choice(self.array, size=size, replace=replace) if p == None else np.random.choice(self.array, size=size, replace=replace, p=p)


def linecount(docstr):
    return len(docstr.split('\n'))

# INIT
python = Python()
Random = Random()
Primes = Sheldon().primes

# SG, Tech Stuff
speak = wincl.Dispatch("SAPI.SpVoice")
def say(string):
    speak.Speak(string)
    return 

class psi:
    @staticmethod
    def show():
        wb.open('https://blissair.com/psi-sg')
        return 

 
def YouAudio(url):  
    video = pafy.new(url) 
    bestaudio = video.getbestaudio() 
    bestaudio.download()
    say('Downloaded '+video.title+' as an audio file')
    return video

def YouVideo(url):  
    video = pafy.new(url) 
    best = video.getbest()
    best.download()
    say('Downloaded '+video.title+' as a video file')
    return video


def weather():
    def weather_data(query):
        res=requests.get('http://api.openweathermap.org/data/2.5/weather?'+query+'&APPID=b35975e18dc93725acb092f7272cc6b8&units=metric')
        return res.json()
    def print_weather(result,city):
        print("\n{}'s temperature: {}°C ".format(city,result['main']['temp']))
        print("Wind speed: {} m/s".format(result['wind']['speed']))
        print("Description: {}".format(result['weather'][0]['description']))
        print("Weather: {}".format(result['weather'][0]['main']), '\n')
    city=input('Enter the city:\n')
    print()
    query='q='+city
    w_data=weather_data(query)
    print_weather(w_data, city)
    print()
    return w_data

speak = wincl.Dispatch("SAPI.SpVoice")
def say(string):
    speak.Speak(string)
    return 
say.__doc__ = 'Insert String to hear the computer to say it. Only works on Windows.'

# Pyshell funcs
def install(lib):
    '''
write your packages after this
    '''
    subprocess.call(['pip', 'install', *lib.split(' ')])

install.__doc__ = "Install a package with this functionality"


def quorask(string):
    wb.open('https://www.quora.com/search?q='+urllib.parse.quote_plus(string))
    return 

def ecosearch(string):
    wb.open('https://www.ecosia.org/search?q='+urllib.parse.quote_plus(string))
    return 
def Query():
    print('Disclaimer: we will open the search tab for the Quora and Ecosia searches')
    print('Press enter in query to exit...')
    query_types = {
        'Google': 'search(\'',
        'Images': 'search_images(\'',
        'News': 'search_news(\'',
        'Videos': 'search_videos(\'',
        'Shop': 'search_shop(\'',
        'Books': 'search_books(\'',
        'Apps': 'search_apps(\'',
        'Lucky': 'lucky(\'',
        'Hits': 'hits(\'',
        'Quora': 'quorask(\'',
        'Ecosia': 'ecosearch(\''
    }
    print('Search Areas:', [*query_types])
    while True:
        ui = input('\nEnter Query >>')
        if not len(ui): return 
        searchtype = input('Enter Search Area: ')
        if not len(searchtype): searchtype = 'Google'
        search = query_types[searchtype]
        if searchtype in ['Ecosia', 'Quora']:
            print('We will open this in a new tab...')
            exec(search+ui+'\')')
            continue
        searches = eval(search+ui+'\')')
        print('In order, the top 10 search results on the Google Category', searchtype+':')
        temp = []
        for i in searches:
            print(i)
            temp.append(i)
        num = eval(input('Which link would you like to access? In 1-10: '))
        wb.open(temp[num-1])


def findnewfor(code):
    start = code.find('for(')
    end = code.find('):')
    string = code[start+4:end]
    restr = code[:start]
    if ';' in string:
        [init, cond, change] = string.split(";")
        init, cond, change = init.strip(), cond.strip(), change.strip()
        
        # set up of init
        [var, val] = re.split('[ ]*=[ ]*', init)
        restr += var + " = " + val + " - 1" + "\n" + code[:start] + 'while (' + cond + " - 1" + '): ' + "\n" + code[:start] + "\t"
        if change.endswith("++"): restr += change[:-2].strip() + " += 1"
        elif change.endswith("--"): restr += change[:-2].strip() + " -= 1"
        else: restr += change
        return restr + "\n" + code[:start] + "\t" + code[end+2:].strip()
    if ';' in string:
        [init, maxn, change] = string[string.find('('):string.find(')')].split(';')
        x, val = init.split('=')
        x = str(filter(lambda y: y != ' ', list(x)))
        val = str(filter(lambda y: y != ' ', list(val)))
        res = 'for '+x+' in range('+val+', '
        maxn = maxn.replace('<', '', maxn.count('<'))
        maxn = maxn.replace('>', '', maxn.count('>'))
        maxn = maxn.replace('=', '', maxn.count('='))
        maxn = maxn.replace(x, '')
        maxn.replace(' ', '')
        res += maxn
        change = change.replace(x, '').replace(' ', '')
        if change == '++': return res+'):'
        if change == '--': return res+', -1):'
    elif ':' in string:
        [name, lst] = string[string.find('(')+1:string.find(')')].split(':')
        name = ''.join(list(filter(lambda y: y != ' ', list(name))))
        lst = "".join(list(filter(lambda y: y != ' ', list(lst))))
        return 'for '+name+' in '+lst+':'


def run(string): exec(execute(string))

def foreachfind(string):
    start = string.find('foreach(')
    end = string.find('):')
    if " as " in string: [lst, name] = re.split("[ ]+as[ ]+", string[start+8:end])
    else: [name, lst] = re.split("[ ]*:[ ]*", string[start+8:end])
    return string[:start]+'for '+name+' in '+lst+':'+string[end+2:]

def cd(directory):
    try:
        os.chdir(directory)
        print('Current Working Directory:', os.getcwd())
    except:
        print('Cannot Change Directory')
    finally:
        return 

def mkdir(directory):
    try:
        os.mkdir(directory)
        print('Made Directory:', os.getcwd()+'\\'+directory)
    except:
        print('Cannot Make Directory')
    finally:
        return 

def printerr(text, err):
    say('Hey. Wimpy back here again.')
    print(text)
    say(text)
    print('Error:', err)
    say('Error: '+str(err))
    return

def dot(var1, var2):
    if type(var1) == type(var2) == np.ndarray: return np.dot(var1, var2)
    return var1 * var2

def flatten(arr):
    if type(arr) == np.ndarray: return arr.flatten()

def transpose(arr):
    if type(arr) == np.ndarray: return arr.T

def absdet(var):
    if type(var) == np.ndarray:
        if var.ndim > 1: return np.linalg.det(var)
        elif var.ndim == 1: return np.sqrt(dot(var, var))
    return abs(var)

def inv(var):
    if type(var) == np.ndarray: return np.linalg.inv(var)


def pinv(var):
    if type(var) == np.ndarray: return np.linalg.inv(var)

def zeros(m, n=-1):
    if n < 0: n = m
    return np.array([[0 for i in range(n)] for j in range(m)])

def ones(m, n=-1):
    if n < 0: n = m
    return np.array([[1 for i in range(n)] for j in range(m)])

def reshape(arr, m, n=1):
    if type(var) == np.ndarray: return arr.reshape(m, n)

def pwmult(arr1, arr2):
    if type(arr1) == np.ndarray and type(arr2) == np.ndarray:
        [r1, c1] = (len(arr1.shape) == 1)*[1] + list(arr1.shape)
        [r2, c2] = (len(arr2.shape) == 1)*[1] + list(arr2.shape)
        maxr = max(r1, r2)
        maxc = max(c1, c2)
        arr1 = np.array([i for i in arr1] + [[0]]*(maxr-r1))
        a1 = [i for i in arr1] if maxc == c1 else [i for i in arr1]+[0 for i in range(maxc-c1)]
        arr2 = np.array([i for i in arr2] + [[0]]*(maxr-r2))
        a2 = [i for i in arr2] if maxc == c2 else [i for i in arr2]+[0 for i in range(maxc-c2)]
        return np.array([[a1[i][j]*a2[i][j] for j in range(maxc)] for i in range(maxr)]) if maxr > 1 else  np.array([a1[i]*a2[i] for i in range(maxc)])


def pwdiv(arr1, arr2):
    if type(arr1) == np.ndarray and type(arr2) == np.ndarray:
        [r1, c1] = (len(arr1.shape) == 1)*[1] + list(arr1.shape)
        [r2, c2] = (len(arr2.shape) == 1)*[1] + list(arr2.shape)
        if r1 == r2 and c1 == c2:
            return np.array([[arr1[i][j]/arr2[i][j] for j in range(c1)] for i in range(r1)])
        elif r1 == r2 and c2 == 1:
            return np.array([[arr1[i][j]/arr2[i][0] for j in range(c1)] for i in range(r1)])
        elif c1 == c2 and r2 == 1:
            return np.array([[arr1[i][j]/arr2[0][j] for j in range(c1)] for i in range(r1)])
           


def code(string):
    print(execute(string))
    

def execute(*args):
    code = args[0]
    codec = code.split('\n')
    opened = 0
    for i in range(len(codec)):
        codec[i].replace(";", "\n"+re.search("\s*", codec[i]).group())
        codec[i] = codec[i].replace('#include <iostream>', 'from pyforest import *')
        codec[i] = codec[i].replace('using namespace std', 'from builtins import *')
        codec[i] = codec[i].replace('this', 'self')
        for t in ['void', 'int', 'double', 'float', 'String', 'str', 'string', 'Integer', "integer", "long", "short", "Double", "Float", "char", "Character", 'func', 'function', 'fun', 'fn', "Function"]:
            while re.search(t+"[ ]+\w+[ ]*\(", codec[i]):
                match = re.search(t+"[ ]+\w+[ ]*\(", codec[i])
                codec[i].replace(match.group, match.group().replace(t, "def"))
            while re.search(t+"[ ]+\w+[ ]*=|[ ]+\[.*\][ ]*=|[ ]+\(.*\)[ ]*=", codec[i]):
                match = re.search(t+"[ ]+\w+[ ]*=|[ ]+\[.*\][ ]*=|[ ]+\(.*\)[ ]*=", codec[i])
                codec[i] = codec[i].replace(match.group(),match.group().replace(t+" ", ""))

        for pre in ['public', 'pub', 'protected', 'open', 'private', 'new', 'final', 'const', 'let', 'val', 'var']:
            codec[i] = codec[i].replace(pre+' ', '')

        if re.search("catch\((\w+)[ ]+(\w+)\)", codec[i]):
            match = re.search("catch\(\w+[ ]+\w+\)", codec[i])
            codec[i] = codec[i].replace(match.group(), "except "+match.group(1)+" as "+match.group(2))
            
        codec[i] = codec[i].replace('throw ', 'raise ')
        codec[i] = codec[i].replace('fmt', 'f')
        codec[i] = codec[i].replace('!(', 'not(')

        for ma in ['import', 'mod', 'module', 'package', 'library', 'requires']: #module accessors
            while re.search(ma+"[ ]+([\w., ]+)", codec[i]):
                match = re.search(ma+"[ ]+([\w., *]+)", codec[i])
                imports = [i.strip() for i in match.group(1).split(',')]
                string = ''
                for imp in imports:
                    string += codec[i][:match.start()]
                    if " as " in imp:
                        lib, name = map(lambda x: x.strip(), imp.split(" as "))
                        string += "import "+lib+" as "+name

                    elif "." in imp:
                        sub, sup = map(lambda x: x[::-1], imp[::-1].split(".", 1))
                        string += "from "+sup+" import "+sub

                    else: string += "import "+imp

                    string += "\n"

                codec[i] = string+codec[i][match.end():]

        
        codec[i] = codec[i].replace(' mod ', ' % ')
        codec[i] = codec[i].replace('::', '.')
        codec[i] = codec[i].replace('elsif', 'elif')
        codec[i] = codec[i].replace('elseif', 'elif')
        codec[i] = codec[i].replace('else if', 'elif')
        codec[i] = codec[i].replace('unless', 'if not')
        codec[i] = codec[i].replace('use ', 'imp ')
        codec[i] = codec[i].replace('∈', ' in ')

        codec[i] = codec[i].replace('<?php', 'pyphp.executer.execute_php(\"\"\"<?php')
        codec[i] = codec[i].replace('?>', '?>\"\"\")')
        
        if '<?php' in codec[i] and '?>' in codec[i]:
            stripped = 0
            while codec[i][stripped].isspace(): stripped += 1
            codec[i] = codec[i][:stripped] + f"pyphp.executer.execute_php({codec[i].strip()})"
        if 'static ' in codec[i]:
            stripped = 0
            while codec[i][stripped].isspace(): stripped += 1
            codec[i] = codec[i][:stripped] + '@staticmethod\n' + codec[i].replace('static ', '')
        if codec[i].strip().startswith('#include <'): codec[i] = codec[i].replace('#include <', 'imp ').replace('>', '')
        if '{' in codec[i]:
            if re.search("if(.)+{", codec[i]) or re.search("for(.)+{", codec[i]) or re.search("while(.)+{", codec[i]) or re.search("def (.)+{", codec[i]) or re.search("(.)+elif (.)+{", codec[i]) or re.search("else(.)+{", codec[i]) or re.search("try(.)+{", codec[i]) or re.search("except (.)+{", codec[i]):
                codec[i] = codec[i].replace('{', ':')
            else: opened += 1
        if codec[i].strip().startswith('} '):
            if not opened: codec[i] = codec[i].replace('} ', '')
            else: opened -= 1
        if codec[i].strip().startswith('}'):
            if not opened: codec[i] = codec[i].replace('}', '')
            else: opened -= 1
        if codec[i].strip().endswith('}'):
            if opened: opened -= 1
            else: codec[i] = codec[i].replace('}', '')
        if codec[i].strip().startswith('{'):
            codec[i-1] += ':'
            codec[i] = codec[i].replace('{', '')
        if '///' in codec[i]: codec[i] = codec[i][:codec[i].find('///')]
        if '#' in codec[i]: codec[i] = codec[i][:codec[i].find('#')]
        if ' /* ' in codec[i]: codec[i] = codec[i].replace('/*', "'''")
        if ' */ ' in codec[i]: codec[i] = codec[i].replace('*/', "'''")
        if '=begin' in codec[i]: codec[i] = codec[i].replace('=begin', "'''")
        if '=end' in codec[i]: codec[i] = codec[i].replace('=end', "'''")
        if '#[' in codec[i]: codec[i] = codec[i].replace('#[', "'''")
        if ']#' in codec[i]: codec[i] = codec[i].replace(']#', "'''")
        if 'prints(' in codec[i]: codec[i] = codec[i].replace('prints(', "print('").replace(")", "')")
        if 'puts ' in codec[i]: codec[i] = codec[i].replace('puts ', 'puts(') + ')'
        if 'echo ' in codec[i]: codec[i] = codec[i].replace('echo ', 'echo(') + ')'
        if 'print ' in codec[i]:
            string = codec[i].replace('print ', 'printf(')
            if ';' in string: codec[i] = string[:string.find(";")] + ")" + string[string.find(";"):]
            else: codec[i] = string + ")"
        if '&&' in codec[i]: codec[i] = codec[i].replace('&&', ' and ')
        if '||' in codec[i]: codec[i] = codec[i].replace('||', ' or ')
        if '===' in codec[i]: codec[i] = codec[i].replace('===', '==')
        if 'define(' in codec[i]: codec[i] = f'exec({eval(codec[i])})'
        if '<>' in codec[i]: codec[i] = codec[i].replace('<>', '!=')
        if codec[i].strip().startswith('!'): codec[i] = codec[i].replace("!", "os.system('") + "')"
        if codec[i].strip().startswith('cd '):
            new = codec[i].strip()[3:]
            codec[i] = f"cd('{new}')"
        if codec[i].strip().startswith('mkdir '):
            new = codec[i].strip()[6:]
            codec[i] = f"mkdir('{new}')"

        if codec[i].strip().startswith('js '):
            new = codec[i].strip()[3:]
            codec[i] = f"js('{new}')"
            
        if 'pip install ' in codec[i]:
            codec[i] = f"os.system('{codec[i]}')"
        if 'imp(' in codec[i]:
            codec[i] = codec[i].replace('imp(', "imp('").replace(")", "')")
            codec[i] = eval(codec[i])
            continue
        if 'imp ' in codec[i]:
            codec[i] = codec[i].replace('imp ', "imp('") + "')"
            codec[i] = eval(codec[i])
            continue
        if 'for(' in codec[i]:
            codec[i] = findnewfor(codec[i])
            continue
        if 'foreach(' in codec[i]:
            codec[i] = foreachfind(codec[i])
            continue
        codec[i] = codec[i].replace('^', '**')
        codec[i] = codec[i].replace('.**', '**')
        codec[i] = codec[i].replace('.+', '+')
        codec[i] = codec[i].replace('.-', '-')
        if '++' in codec[i]: codec[i] = codec[i].replace('++', "+= 1")
        if '--' in codec[i]: codec[i] = codec[i].replace('--', "-= 1")
        if codec[i] == 'query': codec[i] = 'Query()'
        if codec[i] == 'jupyter': codec[i] = 'Jupyter()'
        if codec[i].strip() in ['netstat', 'python', 'ipython', 'py', 'start python', 'assoc', 'systeminfo', 'shutdown /s', 'notepad', 'shutdown /i', 'dir', 'tree']: codec[i] = "os.system('"+codec[i]+"')"
        if 'shutdown --nqa' in codec[i]: os.system('shutdown /s')
        if 'shutdown --ask' in codec[i]: os.system('shutdown /i')
        if codec[i].strip().startswith('py '): codec[i] = "os.system('"+codec[i]+"')"
        if codec[i].strip().startswith('prompt '): codec[i] = "os.system('"+codec[i]+"')"
        if codec[i].strip().startswith('erase '): codec[i] = "os.system('"+codec[i]+"')" if '/p' in codec[i] else "os.system('"+codec[i]+"/p')"
        if codec[i] in ['jupyter notebook', 'jupyter lab']: codec[i] = "jupyterisate('"+codec[i]+"')"
        if codec[i] == 'cmd': codec[i] = 'CommandPrompt()'
        if codec[i] == 'py2': codec[i] = 'Python2()'
        if codec[i] == 'weather': codec[i] = f'Weather = {codec[i]}()'
        if codec[i].strip() == 'print':
            codec[i].replace('print', 'print()')
        while re.search(r"[A-Za-z0-9_]+\.\.\.[A-Za-z0-9_]+", codec[i]):
            match = re.search(r"[A-Za-z0-9_]+\.\.\.[A-Za-z0-9_]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+3:]
            end = codec[i][match.end():]
            codec[i] = start+f"xrange({name1}, {name2})"+end
            
        while re.search(r"[A-Za-z0-9_]+\.\.[A-Za-z0-9_]+", codec[i]):
            match = re.search(r"[A-Za-z0-9_]+\.\.[A-Za-z0-9_]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+2:]
            end = codec[i][match.end():]
            codec[i] = start+f"range({name1}, {name2})"+end
            
        while re.search(r"[A-Za-z0-9_]+\.\.<[A-Za-z0-9_]+", codec[i]):
            match = re.search(r"[A-Za-z0-9_]+\.\.<[A-Za-z0-9_]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+2:]
            end = codec[i][match.end():]
            codec[i] = start+f"range({name1}, {name2})"+end

        while re.search(r"[^ ]+ \. [^ ]+", codec[i]):
            match = re.search(r"[^ ]+ \. [^ ]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+2:]
            end = codec[i][match.end():]
            try:
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name1)-1, -1, -1):
                    s = name1[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        start += name1[:ind+1]
                        name1 = name1[ind+1:]
                        break
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name2)):
                    s = name2[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        end = name2[ind:] + end
                        name2 = name2[:ind]
                        break

                value1 = eval(execute(name1))
                value2 = eval(execute(name2))
                codec[i] = start+f"dot({name1}, {name2})"+end
            except:
               if re.match("[A-Za-z0-9_]+", name1) and re.match("[A-Za-z0-9_]+", name2):
                    codec[i] = start+f"dot({name1}, {name2})"+end

        while re.search(r"[^ ]+ \.\* [^ ]+", codec[i]):
            match = re.search(r"[^ ]+ \.\* [^ ]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+3:]
            end = codec[i][match.end():]
            try:
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name1)-1, -1, -1):
                    s = name1[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        start += name1[:ind+1]
                        name1 = name1[ind+1:]
                        break
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name2)):
                    s = name2[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        end = name2[ind:] + end
                        name2 = name2[:ind]
                        break

                value1 = eval(execute(name1))
                value2 = eval(execute(name2))
                codec[i] = start+f"pwmult({name1}, {name2})"+end
            except:
               if re.match("[A-Za-z0-9_]+", name1) and re.match("[A-Za-z0-9_]+", name2):
                    codec[i] = start+f"pwmult({name1}, {name2})"+end


        while re.search(r"[^ ]+ \./ [^ ]+", codec[i]):
            match = re.search(r"[^ ]+ \./ [^ ]+", codec[i])
            start = codec[i][:match.start()]
            name1 = match.group()[:match.group().find('.')]
            name2 = match.group()[match.group().find('.')+3:]
            end = codec[i][match.end():]
            try:
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name1)-1, -1, -1):
                    s = name1[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        start += name1[:ind+1]
                        name1 = name1[ind+1:]
                        break
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name2)):
                    s = name2[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        end = name2[ind:] + end
                        name2 = name2[:ind]
                        break

                value1 = eval(execute(name1))
                value2 = eval(execute(name2))
                codec[i] = start+f"pwdiv({name1}, {name2})"+end
            except:
               if re.match("[A-Za-z0-9_]+", name1) and re.match("[A-Za-z0-9_]+", name2):
                    codec[i] = start+f"pwdiv({name1}, {name2})"+end

        while re.search(r".+\(:\)", codec[i]):
            match = re.search(r".+\(:\)", codec[i])
            start = codec[i][:match.start()]
            end = codec[i][match.end():]
            name = match.group()[:-3]
            #try:
            square = []
            parentheses = []
            curly = []
            for ind in range(len(name)-1, -1, -1):
                s = name[ind]
                
                try:
                    if s == "=" and len(square) == len(parentheses) == len(curly) == 0:
                        said = ind+(len(name[ind+1:]) - len(name[ind+1:].lstrip()))
                        start += name[:said+1]
                        name = name[said+1:]
                        break
                    if s == ']': square.append(1)
                    if s == ')': parentheses.append(1)
                    if s == '}': curly.append(1)
                    if s == '[': square.pop()
                    if s == '(': parentheses.pop()
                    if s == '{': curly.pop()
                except:
                    start += name[:ind+1]
                    name = name[ind+1:]
                    break
            #value = eval(execute(name))
            codec[i] = start+f"flatten("+name+")"+end
            """except:
                if re.match("[A-Za-z0-9_]+", name):
                    codec[i] = start+f"flatten({name})"+end"""

        while re.search(r"[|].+[|]", codec[i]):
            match = re.search(r"[|].+[|]", codec[i])
            start = codec[i][:match.start()]
            end = codec[i][match.end():]
            name = match.group()[1: -1]
            codec[i] = start+f"absdet({name})"+end

            """
            try:
                value = eval(execute(name))
                codec[i] = start+f"absdet({name})"+end
            except:
                if re.match("[A-Za-z0-9_]+", name):
                    codec[i] = start+f"absdet({name})"+end"""

        while re.search(r"[\[].+[;].+[\]]", codec[i]):
            match = re.search(r"[\[].+[;].+[\]]", codec[i])
            start = codec[i][:match.start()]
            end = codec[i][match.end():]
            string = match.group().replace('  ', ' ').replace(', ', ',').replace('; ', ':').replace(' ', ',')
            #tbd///////

        while re.search(r".+'", codec[i]):
            match = re.search(r".+'", codec[i])
            start = codec[i][:match.start()]
            end = codec[i][match.end():]
            name = match.group()[:match.group().find('\'')]
            try:
                square = []
                parentheses = []
                curly = []
                for ind in range(len(name)-1, -1, -1):
                    s = name[ind]
                    try:
                        if s == ']': square.append(1)
                        if s == ')': parentheses.append(1)
                        if s == '}': curly.append(1)
                        if s == '[': square.pop()
                        if s == '(': parentheses.pop()
                        if s == '{': curly.pop()
                    except:
                        start += name[:ind+1]
                        name = name[ind+1:]
                        break
                
                value = eval(execute(name))
                codec[i] = start+f"transpose({name})"+end
            except:
                if re.match("[A-Za-z0-9_]+", name):
                    codec[i] = start+f"transpose({name})"+end
        if ')(' in codec[i]: codec[i]= codec[i].replace(')(', ')*(')
            
        if codec[i].strip() in ['cwd','getcwd']:
            stripped = 0
            while codec[i][stripped].isspace(): stripped += 1
            codec[i] = codec[i][:stripped] + "print(os.getcwd())"
        
    return '\n'.join(codec)

def evaluate(codec):
    codec = [codec]
    for i in range(len(codec)):
        if '///' in codec[i]: codec[i] = codec[i][:codec[i].find('///')]
        if ' /* ' in codec[i]: codec[i] = codec[i].replace('/*', "'''")
        if ' */ ' in codec[i]: codec[i] = codec[i].replace('/*', "'''")
        if '=begin' in codec[i]: codec[i] = codec[i].replace('=begin', "'''")
        if '=end' in codec[i]: codec[i] = codec[i].replace('=end', "'''")
        if 'prints(' in codec[i]: codec[i] = codec[i].replace('prints(', "print('").replace(")", "')")
        if 'puts ' in codec[i]: codec[i] = codec[i].replace('puts ', 'puts(') + ')'
        if 'echo ' in codec[i]: codec[i] = codec[i].replace('echo ', 'echo(') + ')'
        if 'print ' in codec[i]: codec[i] = codec[i].replace('print ', 'printf(')+ ')'
        if '&&' in codec[i]: codec[i] = codec[i].replace('&&', ' and ')
        if '||' in codec[i]: codec[i] = codec[i].replace('||', ' or ')
        if '===' in codec[i]: codec[i] = codec[i].replace('===', '==')
        if 'define(' in codec[i]: codec[i] = f'exec({eval(codec[i])})'
        if '<>' in codec[i]: codec[i] = codec[i].replace('<>', '!=')
        if 'elsif' in codec[i]: codec[i].replace('elsif', 'elif')
        if 'elseif' in codec[i]: codec[i].replace('elseif', 'elif')
        if 'else if' in codec[i]: codec[i].replace('else if', 'elif')
        if str(filter(lambda x: x not in [' ', '\t', '\n'], list(codec[i])))[0] == '!': codec[i] = codec[i].replace("!", "os.system('") + "')"
        if codec[i].strip().startswith('cd '):
            new = codec[i].strip()[3:]
            codec[i] = f"cd('{new}')"
        if codec[i].strip().startswith('mkdir '):
            new = codec[i].strip()[6:]
            codec[i] = f"mkdir('{new}')"

        if codec[i].strip().startswith('js '):
            new = codec[i].strip()[3:]
            codec[i] = f"js('{new}')"
        if 'pip install ' in codec[i]:
            codec[i] = codec[i].replace('pip install ', "install('") + "')"
        if 'function ' in codec[i]: codec[i] = codec[i].replace('function ', "def ")
        if 'imp(' in codec[i]:
            codec[i] = codec[i].replace('imp(', "imp('").replace(")", "')")
            codec[i] = eval(codec[i])
            continue
        if 'imp ' in codec[i]:
            codec[i] = codec[i].replace('imp ', "imp('") + "')"
            codec[i] = eval(codec[i])
            continue
        if ')(' in codec[i]: codec[i]= codec[i].replace(')(', ')*(')
        if 'for(' in codec[i]:
            codec[i] = findnewfor(codec[i])
            continue
        if 'foreach(' in codec[i]:
            codec[i] = foreachfind(codec[i])
            continue
        if '^' in codec[i]:
            codec[i] = codec[i].replace('^', '**')
        if '++' in codec[i]: codec[i] = codec[i].replace('++', "+= 1")
        if '--' in codec[i]: codec[i] = codec[i].replace('--', "-= 1")
        if codec[i] == 'query': codec[i] = 'Query()'
        if codec[i] == 'jupyter': codec[i] = 'Jupyter()'
        if codec[i].strip() in ['explorer', 'control panel', 'netstat', 'python', 'ipython', 'py', 'start python', 'assoc', 'systeminfo', 'shutdown /s', 'notepad', 'shutdown /i', 'dir', 'tree']: codec[i] = "os.system('"+codec[i]+"')"
        if 'shutdown --nqa' in codec[i]: os.system('shutdown /s')
        if 'shutdown --ask' in codec[i]: os.system('shutdown /i')
        if codec[i].strip().startswith('py '): codec[i] = "os.system('"+codec[i]+"')"
        if codec[i].strip().startswith('erase '): codec[i] = "os.system('"+codec[i]+"')" if '/p' in codec[i] else "os.system('"+codec[i]+"/p')"
        if codec[i].strip().startswith('prompt '): codec[i] = "os.system('"+codec[i]+"')"
        if codec[i] in ['jupyter notebook', 'jupyter lab']: codec[i] = "jupyterisate('"+codec[i]+"')"
        if codec[i] == 'cmd': codec[i] = 'CommandPrompt()'
        if codec[i] == 'py2': codec[i] = 'Python2()'
        if codec[i] == 'weather': codec[i] = f'Weather = {codec[i]}()'
        if codec[i] == 'cwd': codec[i] = "print(os.getcwd())"
    return codec[0]


def camera():
    cd = os.getcwd()
    os.chdir(rd)
    os.system('python camera.py')
    os.chdir(cd)
    return 

def Python2():
    pyfile = open('Python2.py', 'w+')
    while True:
        ui = input('python2 | ')
        if ui in ['exit()', 'quit()']:
            break
        pyfile.write(ui+'\n')
    pyfile.close()
    install('2to3')
    os.system('2to3 -w Python2.py')
    os.system('python Python2.py')
    del pyfile
    return 
        

def jupyterisate(type_of):
    try:
        os.system(type_of)
    except KeyboardInterrupt:
        return 


def CommandPrompt():
    while True:
        ui = input('\n'+os.getcwd()+'>')
        if ui in ['exit()', 'quit()']: return 
        if ui.strip()[:3] == 'cd ':
            os.chdir(ui.strip()[3:])
            print('Current Working Directory:', os.getcwd())
            continue
        if ui.strip()[:6] == 'mkdir ':
            os.mkdir(ui.strip()[6:])
            print('Made Directory:', os.getcwd()+'\\'+ui.strip()[6:])
            continue
        try:
            os.system(ui)
        except Exception as e:
            print(e)

def escape():
    os.system('cmd')
    return 

def Jupyter():
    print("\nEnter within the '| ' section while coding and press Ctrl-C to execute the code. To exit the Notebook, just enter exit()\n")
    code =''''''
    while True:
        try:
            try:
                rewrite = ''''''
                uinp = input('\nJupyter | ')+'\n'
                while True:
                    if 'exit()' in uinp: return code
                    rewrite += uinp
                    uinp = input('        | ')+'\n'
            except KeyboardInterrupt:
                try:
                    exec(execute(rewrite))
                    code += rewrite

                except Exception as e:
                    print(e)
                
        except EOFError:
            return code

def pyexec(source):
    exec(execute(source))

def pyeval(source):
    return eval(evaluate(source))
cnt = -1
def pythonshellreact(ans=False, codes='', no=False):
    final_code = ''
    libraries = [] #["from games import *", "from munprog import*", "from plotting import *", "from CeusGuru import lesson as learn", "from pyforest import *", "from mensuration import *"]
    #"from Docs import documentation"
    for library in libraries: exec(execute(library))
    if not no:
        codec = str(filter(lambda x: x not in [' ', '\t', '\n'], list(codes)))
        if len(codec) and len(codes):
            try:
                print('\STARTING_EXECUTION', end ='')
                exec(execute(codes))
                final_code += codes + '\n'
                print('\n\ENDING_EXECUTION')
            except Exception as e:
                print('There was an Error:', e)
                print('\n\ENDING_EXECUTION')
                pythonshellreact(no=True)
    else:
        print('\n\n')
    global cnt
    ans = ans if ans else bool(ans)
    constlst = []
    while True:
        try:
            ui = input('\n>>>  | ')
            if 'constlst.append' in ui:
                cnt += 1
                for library in libraries: exec(execute(library))
                exec(execute(ui))
                print('this constant has been added\nIt is uploadable by typing constlst[', cnt, ']', sep='')
                continue
            if ui.upper() == '\START':
                docstr = ''''''
                while True:
                    ui = input('code | ')
                    if ui.upper() == '\END': break
                    docstr += ui + '\n'
                '''
for i in range(3):
    s(1)
    print('.', end="")
                '''
                print('\n')
                for library in libraries: exec(execute(library))
                exec(execute(docstr))
                print('\n')
                continue
            if ui == 'query':
                Query()
            if ui == 'cmd':
                CommandPrompt()
                continue
            if ui in ['python', 'ipython', 'py']:
                os.system(ui)
                continue
            if ui in ['jupyter notebook', 'jupyter lab']:
                jupyterisate(ui)
                continue
            if ui in ['quit()', 'exit()']:
                print("It's sad to see you go, but we wish you a happy journey in Python!")
                os.system('cmd')
                break
            if ui == 'jupyter':
                exec('JupyterNB = Jupyter()')
                continue
            if ui in ['restart', 'pqrs']:
                os.system('pqrs')

            if ui == 'py2':
                Python2()
                continue
            if ui in ['this', 'antigravity']:
                exec('import '+ui)
                continue

            try:
                while True:
                    try:
                        for library in libraries: exec(execute(library))
                        found = eval(evaluate(ui))
                        break
                    except NameError as e:
                        if str(e).startswith("name '") and str(e).endswith("' is not defined"):    #name 'pip' is not defined
                            name = str(e)[6:-16]
                            say(f"Hey. Wimpy back here again. Name '{name}' was not defined. Generating it as a algebraic quantity.")
                            exec(execute(f"{name} = sympy.Symbol('{name}')"))
                        else: raise NameError(e)
            except:
                for library in libraries: exec(execute(library))
                exec(execute(ui))
            else:
                if found is None:
                    continue
                try:
                    uinow = str(found)
                except:
                    print(found)
                    ans, prevans = found, ans 
                else:
                    if 'constantpingyan.substituteadd' in uinow:
                        uinow, uitype = uinow[30:-6], uinow[-4:-1]
                        if uitype == 'num':
                            uinow = float(uinow) if '.' in uinow else int(uinow)
                        constlst.append(uinow)
                        cnt += 1
                        print('this constant has been pinged\nIt is uploadable by typing constlst[', cnt, ']', sep='')
                        say('this constant has been pinged\nIt is uploadable by typing constlst['+cnt+']')
                    
                    else:
                        print(found)
                        ans, prevans = found, ans
        except ZeroDivisionError as e:
            try: printerr('Oh no! You divided a number by zero! You can\'t do that, please note that!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! You divided a number by zero! You can\'t do that, please note that!\nError:', e)

        except (ImportError, ModuleNotFoundError) as e:
            try: printerr('Oh no! It seems this import failed! Nevertheless, do persist!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! It seems this import failed! Nevertheless, do persist!\nError:', e)
        
        except SyntaxError as e:
            try: printerr('It seems there is an error in your syntax. You should try and make it right!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('It seems there is an error in your syntax. You should try and make it right!\nError:', e)

        except IndexError as e:
            try: printerr('It seems a data structure has been indexed with an out-of-range number. Don\'t do that!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('It seems a data structure has been indexed with an out-of-range number. Don\'t do that!\nError:', e)
        
        except NameError as e:
            try: printerr('Hey, that variable is unknown! Please do define variables before using them!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Hey, that variable is unknown! Please do define variables before using them!\nError:', e)
           
        except ValueError as e:
            try: printerr('It seems the value inputted in the function is invalid, not because of type! Correct it!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('It seems the value inputted in the function is invalid, not because of type! Correct it!\nError:', e)

        except TypeError as e:
            try: printerr('It seems a function has been called with a wrong-type variable! Please correct it!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('It seems a function has been called with a wrong-type variable! Please correct it!\nError:', e)

        except RuntimeError as e:
            try: printerr('Oops! It seems your code took too long. Maybe you could try shortening it!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oops! It seems your code took too long. Maybe you could try shortening it!\nError:', e)
            
        except FileNotFoundError as e:
            try: printerr('Oh no! This file does not seem to exist! It\'s ok, try again later!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! This file does not seem to exist! It\'s ok, try again later!\nError:', e)

        except AttributeError as e:
            try: printerr('Your attribute assignment/reference seems to fail! Retry!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Your attribute assignment/reference seems to fail! Retry!\nError:', e)
             
        except RecursionError as e:
            try: printerr("Looks like you became too recursive, eh? Sorry, my puns are bad. Also, you can't really chat with me. So that's kinda sad.", e)
            except KeyboardInterrupt: pass
            except EOFError: print("Looks like you became too recursive, eh? Sorry, my puns are bad. Also, you can't really chat with me. So that's kinda sad.\nError:", e)

        except ReferenceError as e:
            try: printerr('Oops a weak reference proxy was obviously used to access an attribute of the referent. Hmm.', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oops a weak reference proxy was obviously used to access an attribute of the referent. Hmm.\nError:', e)
            
        except FloatingPointError as e:
            try: printerr('Oh no! It seems a floating point operation of yours has failed!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! It seems a floating point operation of yours has failed!\nError:', e)

        except KeyError as e:
            try: printerr('It seems this key was not found in the dictionary!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('It seems this key was not found in the dictionary!\nError:', e)

        except MemoryError as e:
            try: printerr('Oh no! The operation you ran has run out of memeory!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! The operation you ran has run out of memeory!\nError:', e)
            
        except OverflowError as e:
            try: printerr('Oh no! This arithmetic operation is too large to be represented.', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh no! This arithmetic operation is too large to be represented.\nError:', e)
            
        except (IndentationError, TabError) as e:
            try: printerr('Oh, your indent is incorrect! You should correct it!', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Oh, your indent is incorrect! You should correct it!\nError:', e)

        except UnboundLocalError as e:
            try: printerr('Well, it seems your value is incorrect.', e)
            except KeyboardInterrupt: pass
            except EOFError: print('Well, it seems your value is incorrect.\nError:', e)

        except AssertionError as e:
            try: printerr("There was an Assertion Error", e)
            except KeyboardInterrupt: pass
            except EOFError: print('There was an Assertion Error\nError:', e)

        except SystemError as e:
            try: printerr('T H E R E  H A S  B E E N  A N  E R R O R  I N  T H E  S Y S T E M', e)
            except KeyboardInterrupt: pass
            except EOFError: print('T H E R E  H A S  B E E N  A N  E R R O R  I N  T H E  S Y S T E M\nError:', e)

        except UnicodeError as e:
            try: printerr("There's a unicode on the other side of the firlf! Let's go touch it's big horn. Oh wait, a Unicode Error.", e)
            except KeyboardInterrupt: pass
            except EOFError: print("There's a unicode on the other side of the firlf! Let's go touch it's big horn. Oh wait, a Unicode Error.\nError:", e)
            
        except KeyboardInterrupt:
            print("It's sad to see you go, but we wish you a happy journey in Python!\n\n\n")
            try: say("Hey. Wimpy back here again. It's sad to see you go, but we wish you a happy journey in Python!")
            except: pass
            break

        except Exception as e:
            print('Error:', e)
    return 

'''
cardValue = 11
if cardValue == 11 {
   print("Jack")
} else if cardValue == 12 { 
   print("Queen")
} else {
   print("Not found") 
}
'''

def exec(source, globals=None, locals=None):
    __import__("builtins", globals, locals).exec(execute(source), globals, locals)
