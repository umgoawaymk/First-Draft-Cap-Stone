
from subprocess import call
import sqlite3
from datetime import datetime
import pprint
import bcrpyt
connection = sqlite3.connect('dp_capstone.db')
cursor = connection.cursor()
# with open ("query.txt","r")as infile:
#     queries = infile.read()
#     cursor.executescript(queries)
#     connection.commit()

    

class Manager:
    
   def __init__(self):
      self.user_id = None
      self.first = None
      self.first = None
      self.phone = None
      self.email = None
      self.__password = None
      self.active = None
      self.date_created = None
      self.hire_date = None
      self.manager = None
      self.salt = b'$2b$12$V62jpTY0AjTqpqoJn.WjW.'
   def __init__ (self,user_id,first,last,city,state,email,password,active,manager,date_created):
      self.id = user_id
      self.first = first
      self.last = last
      self.city = city
      self.state = state
      self.email = email
      self.password = bcrypt.hashpw(password.encode('utf-8'),self.salt)
      self.active = active
      self.manager = manager
      self.date = date_created
      def is_manager():
         if self.manager == 1:
               return manager_menu()
      def __init__(self):
         self.data
      def add_user(self,login,password):
         if login in self.data:
            raise AssertionError('User already exists.')
         if self.data[login] != password:
            return False
         return True
      def __init__(self):
         self.store = user()
      def ask_pass(self):
         user_id= input('User ID: ')
         password = input('Password: ')
         return user_id, password

   


           
            





def manager_menu():
     user_input = input()
     print("Welcome!\n[1] View all users\n[2]Search for a user by first or last name\n[3]View all users competency levels for a given competency\n[4]View a competency level report for an individual user\n[5]View a list of assessments for a given user\n[6]Add a user\n[7]Add a new competency\n[8]Add a new assessment to a competency\n[9]Add an assessment result for a user\n[10]Edit a users information\n[11]Edit a competency\n[12]Edit an assessment\n[13]Edit an assessment result\n[14]Delete and assessment result\n")
     if user_input == '1':
        view_all()
     elif user_input == '2':
        entry = input('Enter a search term First or Last name:')
        search_users(entry)
     elif user_input == '3':
       veiw_user_complevel()
     elif user_input == '4':
        single_user_report()
     elif user_input == '5':
        asse_for_user()
     elif user_input == '6':
        add_user()
     elif user_input == '7':
        add_comp()
     elif user_input == '8':
        add_asse_comp()
     elif user_input == '9':
        add_asse_result()
     elif user_input == '10':
        edit_user() 
     elif user_input == '11':
        edit_comp()
     elif user_input == '12':
        edit_asse()
     elif user_input == '13':
        edit_score()
     elif user_input == '14':
        delete_score() 
 

def view_all():
   rows = ("SELECT * FROM Users")
   columns = ['user_id','first_name','last_name','email','phone','password','active','manager','date_created','hire_date']
   print(f"{'user_id':<3} {'first_name':<15} {'last_name':<15} {'email':<28} {'phone':<11} {'password':<15} {'active':<3} {'manager':<3} {'date_created':<7} {'hire_date':<7}")
   for row in rows:
      pprint(f"{row[0] if row[0]!= None else '':<3} {row[1] if row[1]!= None else '':<15} {row[2] if row[2]!= None else '':<15} {row[3] if row[3]!= None else '':<28}{row[4] if row[4]!= None else '':<11}{row[5] if row[5]!= None else '':<15}{row[6] if row[6]!= None else '':<3}{row[7] if row[7]!= None else '':<3}{row[8] if row[8]!= None else '':<7}{row[9] if row[9]!= None else '':<7}")

def search_users():
    entry =f'%{entry}%'
    columns = ['user_id','first_name','last_name','email','phone','password','active','manager','date_created','hire_date']
    pprint(f"{'user_id':<3} {'first_name':<15} {'last_name':<15} {'email':<28} {'phone':<11} {'password':<15} {'active':<3} {'manager':<3} {'date_created':<9} {'hire_date':<9}")
    rows = cursor.execute("SELECT user_id,first_name,last_name,email,phone,password,active,manager,date_created,hire_date FROM Users WHERE first_name like ? OR WHERE last_name like ?",(entry,entry)).fetchall()
    for row in rows:
      pprint(f"{row[0] if row[0]!= None else '':<3} {row[1] if row[1]!= None else '':<15} {row[2] if row[2]!= None else '':<15} {row[3] if row[3]!= None else '':<28} {row[4] if row[4]!= None else '':<11} {row[5] if row[5]!= None else '':<15} {row[6] if row[6]!= None else '':<3} {row[7] if row[7]!= None else '':<3} {row[8] if row[8]!= None else '':<9} {row[9] if row[9]!= None else '':<9}")

def veiw_user_complevel():
    compentency = input.lower(('Enter the Competency you would like to see user results for: '))
    compentency = f"%{compentency}%"
    rows = cursor.execute('Select * FROM Compentency_Results WHERE Compentency =?',(compentency,)).fetchall()
    columns = ['Competency','First','Last','Level']
    pprint(f"{'Competency':<27} {'First':<20} {'Last':<20} {'Level':<3}")
    for row in rows:
        pprint(f"{row[0] if row[0]!= None else '':<27} {row[1] if row[1]!= None else '':<20} {row[2] if row[2]!= None else '':<20} {row[3] if row[3]!= None else '':<3}")


def single_user_report():
   name = input("Search the user by first or last name: ")
   name = f"%{name}%"
   rows= cursor.execute("Select * FROM Competency_Results WHERE First like? OR Last like?",(name,name)).fetchall()
   columns = ['Competency','First','Last','Level']
   pprint(f"{'Compentency':<17} {'First':<15} {'Last':<15} {'Level':<4}")
   for row in rows:
      pprint(f"{row[0] if row[0]!= None else '':<17} {row[1] if row[1]!= None else '':<15} {row[2] if row[2]!= None else '':<15} {row[3] if row[3]!= None else '':<4}")

def asse_for_user():
   name = input("Search the user by first or last name: ")
   name = f"%{name}%"
   rows = cursor.execute("Select first_name,last_name,score,Assessment FROM Competency_Assessment_Results WHERE first_name like? OR last_name LIKE?",(name,name)).fetchall()
   columns = ['first_name','last_name','score','Assessment']
   pprint(f"{'First':<15} {'Last':<10} {'Score':<4} {'Assessment':<28}")
   for row in rows:
     pprint(f"{row[0] if row[0]!= None else '':15} {row[1] if row[1]!= None else '':<15} {row[2] if row[2]!= None else '':<4} {row[3] if row[3]!= None else '':<28}")


def add_user():
    first = input('First name: ')
    last = input('Last name: ')
    email = input('Email: ')
    phone = input('Phone:')
    password = input('Password: ')
    active = input('Active? 1 = True, 0 = False: ')
    manager = input('Manager? 1 = True, 0 = False: ')
    date = datetime
    hire_date = input('Hire date: ')
    cursor.execute("INSERT INTO Users (first_name,last_name,email,phone,password,active,manager,date_created,hire_date)VALUES(?,?,?,?,?,?,?,?,?)",(first,last,email,phone,password,active,manager,date,hire_date))
    connection.commit()
    pprint('User added!')


def add_comp():
    competency = input('Competency: ')
    date = datetime
    cursor.execute("INSERT INTO Competencies (Competency,date_created)VALUES(?,?)",(competency,date))
    connection.commit()
    pprint('Competency added!')

def add_asse_comp():
    assessment = input('Assessment name: ')
    description = input('Assessment description: ')
    competency = input('Competency: ')
    date = datetime
    cursor.execute("INSERT INTO Assessments (Assessment,Description,Competency,date_created)VALUES(?,?,?,?)",(assessment,description,competency,date))
    connection.commit()
    pprint(f"{assessment} added to {competency}!")

def add_asse_result():
    assessment_id = input('Assessment ID: ')
    user_id = input('User ID: ')
    first = input('User First name: ')
    last = input('User Last name: ')
    score = input('Scores are measured and tracked on a scale from 0-4:\n0 - No competency - Needs Training and Direction\n1 - Basic Competency - Needs Ongoing Support\n2 - Intermediate Competency - Needs Occasional Support\n3 - Advanced Competency - Completes Task Independently\n4 - Expert Competency - Can Effectively pass on this knowledge and can initiate optimizations\nEnter score: ')
    date_taken = input('Enter the date assessment was taken: ')
    administrator = input('User ID of the person who administered the assessment: ')
    assessment = input('Assessment: ')
    cursor.execute('INSERT INTO Competency_Assessment_Results(assessment_id,user_id,first_name,last_name,score,date_taken,administrator,assessment)VALUES(?,?,?,?,?,?,?,?)',(assessment_id,user_id,first,last,score,date_taken,administrator,assessment))
    connection.commit()
    pprint('Score added!')

def edit_user():
   user_input = input()
   pprint('Select what you need to edit\n[1]Email\n[2]Phone #\n[3]Name\n[4]Active\n[5]Manager\n[6]Date account was created\n[7]Hire Date\n')
   if user_input == '1':
      user_id = input('User ID: ')
      email = input('New Email: ')
      cursor.execute("UPDATE Users SET email = ? WHERE user_id =?",(email,user_id))
      connection.commit()
      pprint(f"User {user_id}'s email is now {email}!")
   elif user_input == '2':
      id = input('User ID: ')
      phone_num = input("New Phone Number: ")
      cursor.execute('UPDATE Users SET phone=? WHERE user_id=?',(phone_num,id))
      connection.commit()
      pprint(f"User {id}'s phone number is now {phone_num}!")
   elif user_input == '3':
      u_num = input('User ID: ')
      pprint('Enter what you would like to update\n[F]irst Name\n[L]ast Name\n[B]oth First and Last\n')
      if user_input.lower() =='f':
         first = input("First Name: ")
         cursor.execute('UPDATE Users SET first_name=? WHERE user_id=?',(first,u_num))
         connection.commit()
         pprint(f"User {u_num}'s first name is now {first}!")
      elif user_input.lower() == 'l':
         last = input('Last Name: ')
         cursor.execute('UPDATE Users SET last_name = ? WHERE user_id=?',(last,u_num))
         connection.commit()
         pprint(f"User {u_num}'s last name is now {last}!")
      elif user_input.lower()=='b':
         first = input("First Name: ")
         last = input('Last Name: ')
         cursor.execute('UPDATE Users SET first_name=?, last_name = ? WHERE user_id =?',(first,last,u_num))
         connection.commit()
         pprint(f"User {u_num}'s name is now {first} {last}")

def edit_comp():
   pprint('To edit a compentency enter the current name of the competency.')
   competency = input('Competency: ')
   competency = f'%{competency}%'
   new_name = input(f'Enter the name of the Competency you would like replaced by {competency}: ')
   creation_date = input('Enter new Creation Date (MM-DD-YYYY): ')
   cursor.execute('UPDATE Competencies set Competency=? ,creation_date = ? where Competency=?',(new_name,creation_date,competency))
   connection.commit()
   cursor.execute('UPDATE Assessments set Competency = ? WHERE Competency=?',(new_name,competency))
   connection.commit()
   cursor.execute("UPDATE Compentency_Assessment_Results set Competency = ? WHERE Competency =?",(new_name,competency))
   connection.commit()
   pprint('Competency updated!')

def edit_asse():
   pprint('Enter the assessment ID of the assessment you would like to edit.')
   assessment_id = input('Assessment ID: ')
   pprint("Enter what you would like the assessment's name to be. ")
   new_asse = input('Assessment Name: ')
   desc = input('Enter Assessment Description: ')
   cursor.execute('UPDATE Assessments SET Assessment = ? , Description = ? WHERE assessment_id = ?',(new_asse,desc,assessment_id))
   connection.commit()
   pprint('Assessment updated!')

def edit_score():
   user_choice = input()
   pprint("What score would you like to edit?\n[C]ompetency_Assessment_Results for a invidual User\n[A]verage Score for a individual Assessment\n")
   if user_choice.lower() == 'c':
      user_id = input("Enter the ID of the user who's score you would like to update: ")
      assessment_id = input('Enter the Assessment ID that that user took: ')
      new_score = input('Enter the new score: ')
      cursor.execute('UPDATE Competency_Assessment_Results SET score = ? WHERE user_id = ? AND assessment_id = ? ',(new_score,user_id,assessment_id))
      connection.commit()
      pprint(f'Competency Assessment Result updated for User {user_id}!')
   elif user_choice.lower() == 'a':
      as_id = input('Enter the Assessment ID you are updating the average score for.\nAssessment ID:')
      new_ave = input (f'Enter the new average for Assessment #{as_id}:')
      cursor.execute('UPDATE Assessments SET average_score = ? WHERE assessment_id = ?',(new_ave,as_id))
      connection.commit()
      pprint('Average score updated!')

def delete_score():
   assessment = input('Enter the Assessment ID:')
   user_id = input("Enter the User's ID: ")
   cursor.execute("UPDATE Competency_Assessment_Results SET score= 'N/A' WHERE assessment_id =? AND user_id = ?",(assessment,user_id))
   connection.commit()
   pprint(f"User #{user_id}'s score is removed. ")