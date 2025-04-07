import tkinter as ttk
from tkinter import messagebox
import sqlite3

class QuizStart:
    def __init__ (self, master):

        frame1 = ttk.Frame(master, height = 200, width=300)
        frame1.pack()
        #Label for the question
        self.label1 = ttk.Label(frame1, text="Sample Question:")
        self.label1.grid(column= 0, row= 0)
        self.name = ttk.Entry(frame1)
        self.name.grid(column= 1, row= 0)
        #Option A
        self.label2 = ttk.Label(frame1, text="Test A")
        self.label2.grid(column= 0, row = 1)
        self.bday = ttk.Entry(frame1)
        self.bday.grid(column= 1, row = 1)
        #option B
        self.label3 = ttk.Label(frame1, text="Test B")
        self.label3.grid(column= 0, row = 2)
        self.email = ttk.Entry(frame1)
        self.email.grid(column= 1, row = 2)
        #option C
        self.label4 = ttk.Label(frame1, text="Test C")
        self.label4.grid(column= 0, row = 3)
        self.phone = ttk.Entry(frame1)
        self.phone.grid(column= 1, row = 3)
        #option D
        self.label5 = ttk.Label(frame1, text="Test D")
        self.label5.grid(column= 0, row = 4)
        self.address = ttk.Entry(frame1)
        self.address.grid(column= 1, row = 4)
        #button to go to the next question
        self.btn1 = ttk.Button(frame1, text="Next Question")
        self.btn1.config(command=self.method1)
        self.btn1.grid()