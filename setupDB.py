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

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","True or False: The Federal Trade Commission is NOT an example of a independent agency.",
                         "1. True", "2. False", "3. Null", "4. Null", "2. False"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","What is the process by which courts decide on the constitutionality of legislative enactments and actions of the executive branch",
                         "1. First Review", "2. Final Review", "3. Peer Review", "4. Judicial Review", "4. Juidicial Review"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","True or False: The Constitution is the supreme law of the land.",
                         "1. True", "2. False", "3. Null", "4. Null", "1. True"))

cursor.execute('''INSERT INTO QuizBowlDB
                          (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                            ("Law","What is NOT a type of Attoruney Fee?.",
                             "1. Fixed Fees", "2. Winners Fees", "3. Hourly Fees", "4. Contigency Fees", "2. Winners Fees"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","River City enacts an ordinance that prohibits all advertising on the sides of trucks. A court would likely review this ordinance under the principles of",
                         "1. equal protection.", "2. free exercise.", "3. interstate commerce.", "4. due process", "4. due process"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","A statute enacted by the Wyoming state legislature to regulate trucking affects interstate commerce. In evaluating this statute, the courts will weigh the burden that it imposes on interstate commerce against",
                         "1. the federal government's authority to regulate the matter.", "2. the purpose of interstate commerce.", "3. the state's interest in regulating the matter.", "4. 	the statute's impact on noneconomic activity.", "3. the state's interest in regulating the matter."))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","True or False: New administrative agencies are rarely created in response to a crisis.",
                         "1. True", "2. False", "3. Null", "4. Null", "2. False"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Law","Holly files an employment discrimination suit against Industrial Inc. under Title VII of the Civil Rights Act on a disparate-impact theory. To succeed, Holly must show in part that she was adversely affected by the employer's",
                         "1. Practice", "2. any of the choices", "3. business necessity", "4. 	bona fide occupational qualification.", "1. Practice"))

# DS 3850 Questions
cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What does GUI stand for?",
                         "1. Graphical User Interface", "2. General User Interface", "3. Graphical Universal Interface", "4. General Universal Interface", "1. Graphical User Interface"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What is the output of the following code: print(round (6.75))",
                         "1. 6", "2. 7", "3. 6.75", "4. 6.8", "2. 7"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","Which function brings up a interactive assitance menu in Python?",
                          "1. guide()", "2. assist()", "3. menu()", "4. help()", "4. help()"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","if x = 9, y = 'larry', z = True, what is the output of: Print(x == y)",
                          "1. False", "2. True", "3. Syntax Error", "4. No defined answer", "1. False"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","True or False: A While loop is a Definite loop, one that has a predetermined ending.",
                         "1. True", "2. False", "3. Null", "4. Null", "2. False"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What is the diffrence between a integer and a float?",
                          "1. Integers are positive numbers, floats are negative numbers", "2. Integers are decimal numbers, floats are whole numbers", "3. Integers are whole numbers, floats are decimal numbers", "4. Integers are negative numbers, floats are positive numbers", "3. Integers are whole numbers, floats are decimal numbers"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","Which of the following would provide the correct syntax for finding a random integer WITHOUT importing?",
                          "1. random()", "2. int(random)", "3. print(random)", "4. random.randint()", "4. random.randint()"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What number is the character 'g' in the following phrase? 'I had a good dinner.'",
                          "1. 4", "2. 9", "3. 6", "4. 5", "2. 9"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What is used to deliniate a dictonary?",
                          "1. Brackets ", "2. Parenthesis", "3. Braces", "4. Apostrophe", "3. Braces"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Coding","What keyword defines a new Function?",
                          "1. def", "2. function", "3. new", "4. define", "1. def"))

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

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","what is it called when we knowingly violate a rule of normalization to avoid problems in a table?",
                         "1. Ultra Normal Form", "2. Best Normal Form", "3. Perfect Normal Form", "4. Supreme Normal Form", "2. Best Normal Form"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","Box A has elements A,B,D, and Box B has elements A,C,D. What is the result of Box A Intersection Box B?",
                         "1. A,D", "2. A,,B,C,D", "3. A,B,D", "4. A,C,D", "1. A,D"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","What is NOT  a type of data from a database?",
                         "1. Soruce Data", "2. Meta Data", "3. Grey Data", "4. Overhead Data", "3. Grey Data"))

cursor.execute('''INSERT INTO QuizBowlDB 
                        (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                          ("Database Management","In a Database about a student profile, which of these could be a candidate key?",
                           "1. Student ID", "2. Student Name", "3. Both 1 & 2", "4. None of the 0ptions", "3. Both 1 & 2"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","True or False: Cardinality is the number of rows in one table associated with a single row in another table.",
                         "1. True", "2. False", "3. Null", "4. Null", "1. True"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","What type of Relation Algebra lists all of two tables with no duplicates?",
                         "1. Union", "2. Equijoin", "3. Divison", "4. Intersection", "1. Union"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","Rob has a viedo console that can play many games. However, Rob can only play one game at a time. what would describe Rob's relationship with playing games?.",
                         "1. One & simply One", "2. One & just One", "3. One & only One", "4. One and no One else", "3. One & only One"))

cursor.execute('''INSERT INTO QuizBowlDB
                       (Category, prompt, OptionA, OptionB, OptionC, OptionD, Answer) VALUES (?,?,?,?,?,?,?);''' ,
                        ("Database Management","Whenever there is a many to many relationship, what is the rquired entity to make??",
                         "1. Intersection entity", "2. Middleman entity", "3. Foreman entity", "4. Specalized entity", "1. Intersection entity"))


conn.commit()
conn.close()