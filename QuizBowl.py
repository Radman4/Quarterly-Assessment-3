import tkinter as tk
from tkinter import ttk, messagebox
import sqlite3
import random

# Hard-coded admin password
ADMIN_PASSWORD = "f40355"

class QuizApp(tk.Tk):
    """
    Main application class for the Quiz Bowl.
    Sets up the database connection, creates the questions table if needed,
    and initializes all the GUI frames.
    """
    def __init__(self):
        super().__init__()
        self.title("Quiz Bowl")
        self.geometry("600x400")
        self.conn = sqlite3.connect('QuizBowlDB.db')
        self.create_table()
        
        # Container to hold all frames
        self.container = tk.Frame(self)
        self.container.pack(side="top", fill="both", expand=True)
        
        # Dictionary to keep track of the frames
        self.frames = {}
        for F in (MainMenu, AdminLoginPage, AdminPanel, QuizCategorySelectionPage,
                  QuizPage, FinalScorePage, AddQuestionPage, EditQuestionPage, DeleteQuestionPage):
            frame = F(parent=self.container, app=self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        
        self.show_frame(MainMenu)
    
    def create_table(self):
        """
        Create the questions table (if it does not exist) with required columns.
        """
        try:
            cursor = self.conn.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS QuizBowlDB (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    category TEXT NOT NULL,
                    prompt TEXT NOT NULL,
                    optionA TEXT NOT NULL,
                    optionB TEXT NOT NULL,
                    optionC TEXT NOT NULL,
                    optionD TEXT NOT NULL,
                    answer TEXT NOT NULL
                )
            """)
            self.conn.commit()
        except Exception as e:
            messagebox.showerror("Database Error", "An error occurred while setting up the database: " + str(e))
    
    def show_frame(self, cont):
        """
        Raise the frame (page) passed in the parameter.
        """
        frame = self.frames[cont]
        frame.tkraise()
    
    def get_connection(self):
        """
        Provide the current database connection object.
        """
        return self.conn

# Main menu page with options for Admin or Quiz Taker
class MainMenu(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Welcome to Quiz Bowl!", font=("Helvetica", 16))
        label.pack(pady=20)
        
        admin_button = tk.Button(self, text="Admin", command=lambda: app.show_frame(AdminLoginPage))
        admin_button.pack(pady=10)
        
        quiz_button = tk.Button(self, text="Quiz Taker", command=lambda: app.show_frame(QuizCategorySelectionPage))
        quiz_button.pack(pady=10)

# Admin login page
class AdminLoginPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Admin Login", font=("Helvetica", 16))
        label.pack(pady=20)
        
        tk.Label(self, text="Enter Password:").pack(pady=5)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)
        
        login_button = tk.Button(self, text="Login", command=self.check_login)
        login_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: app.show_frame(MainMenu))
        back_button.pack(pady=5)
    
    def check_login(self):
        """
        Check entered password against the hard-coded ADMIN_PASSWORD.
        On success, load the Admin Panel.
        """
        if self.password_entry.get() == ADMIN_PASSWORD:
            self.password_entry.delete(0, tk.END)
            self.app.show_frame(AdminPanel)
        else:
            messagebox.showerror("Login Failed", "Incorrect password!")

# Admin panel offering add/edit/delete options
class AdminPanel(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Admin Panel", font=("Helvetica", 16))
        label.pack(pady=20)
        
        add_button = tk.Button(self, text="Add New Question", command=lambda: app.show_frame(AddQuestionPage))
        add_button.pack(pady=10)
        
        edit_button = tk.Button(self, text="Edit Existing Question", command=lambda: app.show_frame(EditQuestionPage))
        edit_button.pack(pady=10)
        
        delete_button = tk.Button(self, text="Delete a Question", command=lambda: app.show_frame(DeleteQuestionPage))
        delete_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: app.show_frame(MainMenu))
        back_button.pack(pady=10)

# Page for adding a new question
class AddQuestionPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Add New Question", font=("Helvetica", 16))
        label.pack(pady=10)
        
        # Create entry fields for all required question details.
        self.category_entry = tk.Entry(self)
        self.category_entry.pack(pady=5)
        self.category_entry.insert(0, "Category")
        
        self.prompt_entry = tk.Entry(self)
        self.prompt_entry.pack(pady=5)
        self.prompt_entry.insert(0, "Prompt/Question")
        
        self.optionA_entry = tk.Entry(self)
        self.optionA_entry.pack(pady=5)
        self.optionA_entry.insert(0, "Option 1")
        
        self.optionB_entry = tk.Entry(self)
        self.optionB_entry.pack(pady=5)
        self.optionB_entry.insert(0, "Option 2")
        
        self.optionC_entry = tk.Entry(self)
        self.optionC_entry.pack(pady=5)
        self.optionC_entry.insert(0, "Option 3")
        
        self.optionD_entry = tk.Entry(self)
        self.optionD_entry.pack(pady=5)
        self.optionD_entry.insert(0, "Option 4")
        
        self.answer_entry = tk.Entry(self)
        self.answer_entry.pack(pady=5)
        self.answer_entry.insert(0, "Correct Answer (must match one of the options)")
        
        submit_button = tk.Button(self, text="Add Question", command=self.add_question)
        submit_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Admin Panel", command=lambda: app.show_frame(AdminPanel))
        back_button.pack(pady=5)
    
    def add_question(self):
        """
        Add the new question to the database with proper error checking.
        """
        category = self.category_entry.get()
        prompt = self.prompt_entry.get()
        optionA = self.optionA_entry.get()
        optionB = self.optionB_entry.get()
        optionC = self.optionC_entry.get()
        optionD = self.optionD_entry.get()
        answer = self.answer_entry.get()
        
        # Validate that the answer is one of the options.
        if answer not in (optionA, optionB, optionC, optionD):
            messagebox.showerror("Error", "The answer must match one of the provided options.")
            return

        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""INSERT INTO QuizBowlDB (category, prompt, optionA, optionB, optionC, optionD, answer)
                              VALUES (?, ?, ?, ?, ?, ?, ?)""",
                           (category, prompt, optionA, optionB, optionC, optionD, answer))
            conn.commit()
            messagebox.showinfo("Success", "Question added successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", "Could not add question: " + str(e))

# Page for editing an existing question
class EditQuestionPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Edit Question", font=("Helvetica", 16))
        label.pack(pady=10)
        
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)
        self.id_entry.insert(0, "Enter Question ID to edit")
        
        load_button = tk.Button(self, text="Load Question", command=self.load_question)
        load_button.pack(pady=5)
        
        self.edit_frame = tk.Frame(self)
        self.edit_frame.pack(pady=5)
        
        back_button = tk.Button(self, text="Back to Admin Panel", command=lambda: app.show_frame(AdminPanel))
        back_button.pack(pady=5)
    
    def load_question(self):
        """
        Loads the question (if found) in editable entry fields.
        """
        qid = self.id_entry.get()
        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT category, prompt, optionA, optionB, optionC, optionD, answer FROM QuizBowlDB WHERE id = ?", (qid,))
            result = cursor.fetchone()
            if result:
                # Clear any previous widgets in edit_frame.
                for widget in self.edit_frame.winfo_children():
                    widget.destroy()
                self.edit_entries = {}
                labels = ["Category", "Prompt", "Option 1", "Option 2", "Option 3", "Option 4", "Answer"]
                for i, field in enumerate(result):
                    tk.Label(self.edit_frame, text=labels[i]).grid(row=i, column=0, padx=5, pady=5)
                    entry = tk.Entry(self.edit_frame, width=50)
                    entry.grid(row=i, column=1, padx=5, pady=5)
                    entry.insert(0, field)
                    # Using lower-case keys for convenience (note: key for "Option 1" becomes "option 1")
                    self.edit_entries[labels[i].lower()] = entry
                save_button = tk.Button(self.edit_frame, text="Save Changes", command=lambda: self.save_changes(qid))
                save_button.grid(row=len(result), column=0, columnspan=2, pady=10)
            else:
                messagebox.showerror("Error", "Question ID not found.")
        except Exception as e:
            messagebox.showerror("Database Error", "Error loading question: " + str(e))
    
    def save_changes(self, qid):
        """
        Commit edited question data to the database.
        """
        data = {}
        for field, entry in self.edit_entries.items():
            data[field] = entry.get()
        # Ensure the answer is one of the provided options.
        if data["answer"] not in (data["option 1"], data["option 2"], data["option 3"], data["option 4"]):
            messagebox.showerror("Error", "The answer must match one of the provided options.")
            return
        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("""
                UPDATE QuizBowlDB 
                SET category=?, prompt=?, optionA=?, optionB=?, optionC=?, optionD=?, answer=?
                WHERE id=?
            """, (data["category"], data["prompt"], data["option 1"], data["option 2"],
                  data["option 3"], data["option 4"], data["answer"], qid))
            conn.commit()
            messagebox.showinfo("Success", "Question updated successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", "Error saving question: " + str(e))

# Page for deleting an existing question based on its ID.
class DeleteQuestionPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Delete Question", font=("Helvetica", 16))
        label.pack(pady=10)
        
        self.id_entry = tk.Entry(self)
        self.id_entry.pack(pady=5)
        self.id_entry.insert(0, "Enter Question ID to delete")
        
        delete_button = tk.Button(self, text="Delete", command=self.delete_question)
        delete_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Admin Panel", command=lambda: app.show_frame(AdminPanel))
        back_button.pack(pady=5)
    
    def delete_question(self):
        """
        Delete a question by its ID from the database.
        """
        qid = self.id_entry.get()
        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("DELETE FROM QuizBowlDB WHERE id = ?", (qid,))
            if cursor.rowcount == 0:
                messagebox.showerror("Error", "Question ID not found.")
            else:
                conn.commit()
                messagebox.showinfo("Success", "Question deleted successfully!")
        except Exception as e:
            messagebox.showerror("Database Error", "Error deleting question: " + str(e))

# Page for quiz takers to select a category.
class QuizCategorySelectionPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        label = tk.Label(self, text="Select Quiz Category", font=("Helvetica", 16))
        label.pack(pady=10)
        
        self.category_var = tk.StringVar(self)
        self.category_combo = ttk.Combobox(self, textvariable=self.category_var)
        self.load_categories()
        self.category_combo.pack(pady=5)
        
        start_button = tk.Button(self, text="Start Quiz", command=self.start_quiz)
        start_button.pack(pady=10)
        
        back_button = tk.Button(self, text="Back to Main Menu", command=lambda: app.show_frame(MainMenu))
        back_button.pack(pady=5)
    
    def load_categories(self):
        """
        Load distinct categories from the questions database.
        """
        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT DISTINCT category FROM QuizBowlDB")
            categories = [row[0] for row in cursor.fetchall()]
            self.category_combo['values'] = categories
            if categories:
                self.category_combo.current(0)
        except Exception as e:
            messagebox.showerror("Database Error", "Error loading categories: " + str(e))

    def start_quiz(self):
        """
        Initialize the quiz based on selected category.
        """
        category = self.category_var.get()
        if category == "":
            messagebox.showerror("Error", "Please select a category.")
            return
        quiz_frame = self.app.frames[QuizPage]
        quiz_frame.start_quiz(category)
        self.app.show_frame(QuizPage)

# A simple Question class that holds question data and validates answers.
class Question:
    def __init__(self, prompt, options, answer):
        self.prompt = prompt
        self.options = options  # List of multiple-choice options
        self.answer = answer
    
    def is_correct(self, selected_option):
        """
        Compare the selected option against the answer.
        """
        return selected_option == self.answer

# The quiz interface shown to Quiz Takers.
class QuizPage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        self.question_objects = []  # List of Question objects
        self.score = 0
        self.current_index = 0
        
        # Visible score label
        self.score_label = tk.Label(self, text="Score: 0", font=("Helvetica", 14))
        self.score_label.pack(pady=5)
        
        # Label to display question prompt
        self.prompt_label = tk.Label(self, text="", wraplength=500, font=("Helvetica", 12))
        self.prompt_label.pack(pady=10)
        
        # Use a StringVar and radio buttons for multiple-choice options.
        self.selected_option = tk.StringVar()
        self.option_buttons = []
        for i in range(4):
            rbtn = tk.Radiobutton(self, text="", variable=self.selected_option,
                                  value="", font=("Helvetica", 12))
            rbtn.pack(anchor="w")
            self.option_buttons.append(rbtn)
        
        self.submit_button = tk.Button(self, text="Submit Answer", command=self.submit_answer)
        self.submit_button.pack(pady=10)
    
    def start_quiz(self, category):
        """
        Retrieve up to 10 QuizBowlDB (randomly chosen if more available) from the database
        for the selected category and reset the quiz state.
        """
        self.score = 0
        self.current_index = 0
        self.score_label.config(text="Score: 0")
        self.question_objects.clear()
        
        conn = self.app.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT prompt, optionA, optionB, optionC, optionD, answer FROM QuizBowlDB WHERE category = ?", (category,))
            rows = cursor.fetchall()
            if not rows:
                messagebox.showerror("Error", "No questions found for this category.")
                self.app.show_frame(QuizCategorySelectionPage)
                return
            # Randomly select 10 questions if necessary.
            if len(rows) > 10:
                rows = random.sample(rows, 10)
            for row in rows:
                prompt = row[0]
                options = list(row[1:5])
                answer = row[5]
                self.question_objects.append(Question(prompt, options, answer))
            self.display_question()
        except Exception as e:
            messagebox.showerror("Database Error", "Error retrieving questions: " + str(e))
    
    def display_question(self):
        """
        Display the current question and its options. If no questions remain, show the Final Score page.
        """
        if self.current_index < len(self.question_objects):
            q = self.question_objects[self.current_index]
            self.prompt_label.config(text=q.prompt)
            self.selected_option.set(None)
            for i, option in enumerate(q.options):
                self.option_buttons[i].config(text=option, value=option)
        else:
            final_frame = self.app.frames[FinalScorePage]
            final_frame.set_score(self.score, len(self.question_objects))
            self.app.show_frame(FinalScorePage)
    
    def submit_answer(self):
        """
        Check the user’s answer, update the score and provide immediate feedback,
        then load the next question.
        """
        selected = self.selected_option.get()
        if not selected:
            messagebox.showerror("Error", "Please select an option.")
            return
        current_question = self.question_objects[self.current_index]
        if current_question.is_correct(selected):
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect! The correct answer was: {current_question.answer}")
        self.score_label.config(text=f"Score: {self.score}")
        self.current_index += 1
        self.display_question()

# Final score page shown when the quiz is over.
class FinalScorePage(tk.Frame):
    def __init__(self, parent, app):
        super().__init__(parent)
        self.app = app
        
        self.score_label = tk.Label(self, text="", font=("Helvetica", 16))
        self.score_label.pack(pady=20)
        
        home_button = tk.Button(self, text="Return to Main Menu", command=lambda: app.show_frame(MainMenu))
        home_button.pack(pady=10)
    
    def set_score(self, score, total):
        """
        Update the score label with the final score.
        """
        self.score_label.config(text=f"Final Score: {score} out of {total}")

if __name__ == "__main__":
    app = QuizApp()
    app.mainloop()
