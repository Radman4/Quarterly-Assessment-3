import sqlite3
conn = sqlite3.connect('QuizBowlDB.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS QuizBowlDB (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    Category TEXT NOT NULL,
    prompt TEXT NOT NULL,
    OptionA TEXT NOT NULL,
    OptionB TEXT NOT NULL,
    OptionC TEXT NOT NULL,
    OptionD TEXT NOT NULL,
    Answer TEXT NOT NULL
)''')
# Admin password: f40355

# Law 2810 Questions
cursor.execute('''INSERT INTO QuizBowlDB 
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","Which is NOT a requirement for a Valid Contract?",
                         "1. Agreement", "2. Ability", "3. Consideration", "4. Legality", "2. Ability"))

cursor.execute('''INSERT INTO QuizBowlDB 
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","What is statue Congress enacts to create a administrative agency?",
                         "1. Debuting Legislation", "2. Enabling Legislation", "3. Creating Legislation", "4. Enforcing Legislation", "2. Enabling Legislation"))

# DS 3850 Questions
cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What does GUI stand for?",
                         "1. Graphical User Interface", "2. General User Interface", "3. Graphical Universal Interface", "4. General Universal Interface", "1. Graphical User Interface"))


# Finance 3210 Questions
cursor.execute('''INSERT INTO QuizBowlDB 
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","Joan has $100 avalible for investment. She can choose to keep the $100, or invest it in a double or nothing game. Assuming Joan belives the risk is worth the same, what is she considered?",
                         "1. Risk-Adverse", "2. Risk-Loving", "3. Risk-Neutral", "4. Risk-Dependant", "3. Risk-Neutral"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","True or False: The unsystematic risk component of the total portfolio risk can be reduced by adding negatively correlated stocks to the portfolio.",
                         "1. True", "2. False", "3. Null", "4. Null", "1. True"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","Short Term Debt is known as (Blank) on the balance sheet.",
                         "1. Current Liabilities", "2. Accounts Payable", "3. Notes Payable", "4. Null", "3. Notes  Payable"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","what type of bond may be exchanged for common stock of the firm, at the holder’s option?",
                         "1. Convertible Bond", "2. Changeable Bond", "3. Income bond", "4. Putable Bond", "1. Convertible Bond"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","True or False: The Marginal Tax Rate is taxes divided by taxable income.",
                         "1. True", "2. False", "3. Null", "4. Null", "2. False"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","Which of the five types of ratios gives a idea of how efficiently a company is using its assets?",
                         "1. Profitability Ratios", "2. Liquidity Ratios", "3. Activity Ratios", "4. Solvency Ratios", "3. Activity Ratios"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance"," What is the present value (PV) of $100 due in 3 years, if I/YR = 4%?",
                         "1. 113.06", "2. 110.84", "3. 115.32", "4. 112.49", "4. 112.49"))   

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","what is the common equity raised by issuing new stock?", 
                         "1. external equity", "2. extra equity", "3. internal equity", "4. New Equity", "1. external equity"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","dividend per share / price of the stock per share is known as?",
                         "1. Dividend Yield", "2. Dividend Rate", "3. Dividend Payout", "4. Dividend Growth", "1. Dividend Yield"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Finance","True or False: The cost of debt is the return required by stockholders.",
                         "1. True", "2. False", "3. Null", "4. Null", "2. False"))

# DS 3860 Questions
cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","Which type of Normal Form is the first to exclude partial dependencies?",
                         "1. 1NF", "2. 4NF", "3. 3NF", "4.2NF", "4.2NF"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","WestAir has 10 planes and 5 pilots. Each pilot can fly one or more planes.Each plane can only fly with one pilot. what type of relationship is this?",
                         "1. One to Many", "2. Many to None", "3. One & only One", "4. Many to Many", "4 Many to Many"))
conn.commit()
conn.close()