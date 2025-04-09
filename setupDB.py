import sqlite3
conn = sqlite3.connect('QuizBowlDB.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS QuizBowlDB (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Category TEXT NOT NULL,
    Question TEXT NOT NULL,
    Options TEXT NOT NULL,
    Answer TEXT NOT NULL
)''')
# Admin username : CornGuy password: f40355

# Law 2810 Questions
cursor.execute('''INSERT INTO QuizBowlDB 
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Law","Which is NOT a requirement for a Valid Contract?",
                         "A. Agreement, B. Ability, C. Consideration, D. Legality", "B"))

cursor.execute('''INSERT INTO QuizBowlDB 
                        (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Law","What is statue Congress enacts to create a administrative agency?",
                         "A. Debuting Legislation, B. Enabling Legislation, C. Creating Legislation, D. Enforcing Legislation", "B"))

# DS 3850 Questions
cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Coding","What does GUI stand for?",
                         "A. Graphical User Interface, B. General User Interface, C. Graphical Universal Interface, D. General Universal Interface", "A"))


# Finance 3210 Questions
cursor.execute('''INSERT INTO QuizBowlDB 
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Finance","Joan has $100 avalible for investment. She can choose to keep the $100, or invest it in a double or nothing game. Assuming Joan belives the risk is worth the same, what is she considered?",
                         "A. Risk-Adverse, B. Risk-Loving, C. Risk-Neutral, D. Risk-Dependant", "C"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Finance","True or False: The unsystematic risk component of the total portfolio risk can be reduced by adding negatively correlated stocks to the portfolio.",
                         "A. True, B. False, C. Null, D. Null", "A"))

# DS 3860 Questions
cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Database Management","Which type of Normal Form is the first to exclude partial dependencies?",
                         "A. 1NF, B. 4NF, C. 3NF, D.2NF", "D"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, Question, Options, Answer) VALUES (?,?,?,?);''' ,
                        ("Database Management","WestAir has 10 planes and 5 pilots. Each pilot can fly one or more planes.Each plane can only fly with one pilot. what type of relationship is this?",
                         "A. One to Many, B. Many to None, C. One & only One, D. Many to Many", "A"))
conn.commit()