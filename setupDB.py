import sqlite3
conn = sqlite3.connect('QuizBowlDB.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS QuizBowlDB (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Question TEXT NOT NULL,
    OptionA TEXT NOT NULL,
    OptionB TEXT NOT NULL,
    OptionC TEXT NOT NULL,
    OptionD TEXT NOT NULL,
    Answer TEXT NOT NULL
)''')

cursor.execute('''INSERT INTO QuizBowlDB 
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("1.) Which is NOT a requirement for a Valid Contract?",
                         "A. Agreement","B. Ability","C. Consideration","D. Legality", "B"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("2.) What does GUI stand for?",
                         "A. Graphical User Interface","B. General User Interface","C. Graphical Universal Interface","D. General Universal Interface", "A"))

cursor.execute('''INSERT INTO QuizBowlDB 
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("3.) Joan has $100 avalible for investment. She can choose to keep the $100, or invest it in a double or nothing game. Assuming Joan belives the risk is worth the same, what is she considered?",
                         "A. Risk-Adverse","B. Risk-Loving","C. Risk-Neutral","D. Risk-Dependant", "C"))

cursor.execute('''INSERT INTO QuizBowlDB 
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("4.) What is statue Congress enacts to create a administrative agency?",
                         "A. Debuting Legislation","B. Enabling Legislation","C. Creating Legislation","D. Enforcing Legislation", "B"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("5.) True or False: The unsystematic risk component of the total portfolio risk can be reduced by adding negatively correlated stocks to the portfolio.",
                         "A. True","B. False","C. Null","D. Null", "A"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("6.) Which type of Normal Form is the first to exclude partial dependencies?",
                         "A. 1NF","B. 4NF","C. 3NF","D.2NF", "D"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Question, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?);''' ,
                        ("7.) WestAir has 10 planes and 5 pilots. Each pilot can fly one or more planes.Each plane can only fly with one pilot. what type of relationship is this?",
                         "A. One to Many","B. Many to None","C. One & only One","D. Many to Many", "A"))
conn.commit()