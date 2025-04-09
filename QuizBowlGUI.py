from tkinter import *
import tkinter as ttk
from tkinter import messagebox
import sqlite3

#login screen for the quiz bowl
root = Tk()
class LoginScreen:
    def __init__ (self, master):

        #frame for the login screen
        loginFrame = ttk.Frame(master, height=200, width=300)
        loginFrame.pack()
        #label for the username
        self.label1 = ttk.Label(loginFrame, text="Username:")
        self.label1.grid(column=0, row=0)
        #entry for the username
        self.username = ttk.Entry(loginFrame)
        self.username.grid(column=1, row=0)
        #label for the password
        self.label2 = ttk.Label(loginFrame, text="Password:")
        self.label2.grid(column=0, row=1)
        #entry for the password
        self.password = ttk.Entry(loginFrame, show="*")
        self.password.grid(column=1, row=1)
        #button to submit the login information
        self.btn1 = ttk.Button(loginFrame, text="Login as Admin", command=self.checkLogin)
        self.btn1.grid(column=0, row=2)
        #button to continue to quiz bowl
        self.btn2 = ttk.Button(loginFrame, text="Continue to Quiz Bowl", command=self.continueQuiz)
        self.btn2.grid(column=1, row=2)
        
    def checkLogin(self):
        if self.username.get() == "CornGuy" and self.password.get() == "f40355":
            messagebox.showinfo("Login", "Login Successful!")
            #opens the admin screen
            root.withdraw()
            admin_window = Toplevel(root)
            admin_window.title("Admin Screen")
            AdminScreen(admin_window)

        else:
            messagebox.showerror("Login", "Login Failed!")
    def continueQuiz(self):
        #opens the quiz screen
        root.withdraw()
        quiz_window = Toplevel(root)
        quiz_window.title("Quiz Bowl")
        quizStart(quiz_window)
class AdminScreen:
    def __init__(self, master):
        #frame for the admin screen
        self.adminFrame = ttk.Frame(self, height=200, width=300)
        self.adminFrame.pack()
        #entry for the category
        self.label2 = ttk.Label(self.adminFrame, text="Category:")
        self.label2.grid(column=0, row=1)
        self.category = ttk.Entry(self.adminFrame)
        self.category.grid(column=1, row=1)
        #add a question to the database
        self.label1 = ttk.Label(self.adminFrame, text="Question:")
        self.label1.grid(column=0, row=0)
        self.question = ttk.Entry(self.adminFrame)
        self.question.grid(column=1, row=0)
        #entry for the options
        self.label3 = ttk.Label(self.adminFrame, text="Options")
        self.label3.grid(column=0, row=2)
        self.options = ttk.Entry(self.adminFrame)
        self.options.grid(column=1, row=2)
        #entry for the answer
        self.label6 = ttk.Label(self.adminFrame, text="Answer:")
        self.label6.grid(column=0, row=5)
        self.answer = ttk.Entry(self.adminFrame)
        self.answer.grid(column=1, row=5)
        #button to submit the question
        self.btn1 = ttk.Button(self.adminFrame, text="Submit", command=self.submitQuestion)
        self.btn1.grid(column=0, row=6)
        #button to quit the admin screen
        self.btn2 = ttk.Button(self.adminFrame, text="Quit", command=self.quitAdmin)
        self.btn2.grid(column=1, row=6)
    def submitQuestion(self):
        #connect to the database
        conn = sqlite3.connect('QuizBowlDB.db')
        cursor = conn.cursor()
        #insert the question into the database
        cursor.execute('''INSERT INTO QuizBowlDB 
                        (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                         (self.category.get(),self.question.get(), self.options.get(), self.answer.get()))
        conn.commit()
        messagebox.showinfo("Submit", "Question Submitted!")
class quizStart:
    def __init__ (self, master):
        self.master = master
        self.master.geometry("300x200")
        #begins quiz questions at 0
        self.quizNum = 0
        #number of correct answers
        self.correct = 0
        #numer of questions
        self.numQuestions = 0
        #display buttons
        self.options=self.radioButtons()
        self.buttons()
        self.quizOptions()
        #integer for the question choice
        self.questionCheck = ttk.IntVar()
        self.questions = []

    def radioButtons(self):
        button = []
        for b in range(4):
            button.append(ttk.Radiobutton(self.master, text="", variable=self.questionCheck, value=b))
            button[b].grid(row=3, column=b)
        return button

    def quizOptions(self):
        #connect to the database
        conn = sqlite3.connect('QuizBowlDB.db')
        cursor = conn.cursor()
        #get the question from the database
        cursor.execute('''SELECT Category, Question, Options, Answer FROM QuizBowlDB''',)
        conn.commit()



   
    #check to see if question is correct
    def questionCheck(self, quizNum):
        if self.questionCheck.get() == [quizNum]:
            return True
    
    def checkAnswer(self):
        #check to see if the answer is correct
        if self.answer(self.quizNum):
            messagebox.showinfo("Correct", "Correct!")
            self.correct += 1
        else:
            messagebox.showinfo("Incorrect", "Incorrect!")
        #move on to the next question
        self.quizNum += 1
        #ends quiz if all questions are answered
        if self.quizNum==len(questions):
            messagebox.showinfo("Quiz Complete", f"You got {self.correct} out of {len(questions)} correct!")
            self.quitQuiz()
        else:
            self.quizQuestion()
            self.quizOptions()

    def quitQuiz(self):
        #closes the quiz window
        self.master.destroy()
        root.deiconify()
    
    def quizQuestion(self):
        #displays the question
        self.questionLabel = ttk.Label(self.master, text=questions[self.quizNum][1])
        self.questionLabel.grid(row=1, column=0, columnspan=4)
        #displays the options
        for i in range(4):
            self.options[i].config(text=questions[self.quizNum][2][i])
            self.options[i].grid(row=3, column=i)
        #displays the answer
        self.answer = questions[self.quizNum][3]
        #displays the category
        self.categoryLabel = ttk.Label(self.master, text=questions[self.quizNum][0])
        self.categoryLabel.grid(row=0, column=0, columnspan=4)

    def buttons(self):
        #button to submit the answer
        self.submit = ttk.Button(self.master, text="Submit", command=self.checkAnswer)
        self.submit.grid(row=5, column=0)
        #button to end quiz
        self.quit = ttk.Button(self.master, text="Quit", command=self.quitQuiz)
        self.quit.grid(row=5, column=1)
app = LoginScreen(root)
root.mainloop()