import sqlite3
from datetime import datetime
import pprint
from tkinter import N
import bcrypt
connection = sqlite3.connect('dp_capstone.db')
cursor = connection.cursor()

class Users:
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
            if self.manager == 0:
                return user_menu()
            

def user_menu():
     u_input = input()
     print("Welcome!\n[1]Update your user information \n[2]View your competency assessment data\n")
     if u_input == '1':
         user_update()
     elif u_input == '2':
        view_reports() 

def user_update():
   user_input = input()
   pprint('Select what you need to edit\n[1]Email\n[2]Phone #\n[3]Name\n[4]Active\n[5]Manager\n[6]Date account was created\n[7]Hire Date\n')
   if user_input == '1':
      user_id = input('Comfirm User ID: ')
      email = input('New Email: ')
      cursor.execute("UPDATE Users SET email = ? WHERE user_id =?",(email,user_id))
      connection.commit()
      pprint(f"User {user_id}'s email is now {email}!")
   elif user_input == '2':
      id = input('Comfirm User ID: ')
      phone_num = input("New Phone Number: ")
      cursor.execute('UPDATE Users SET phone=? WHERE user_id=?',(phone_num,id))
      connection.commit()
      pprint(f"User {id}'s phone number is now {phone_num}!")
   elif user_input == '3':
      u_num = input('Comfirm User ID: ')
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

def view_reports():
     user_id = input('Comfirm User ID: ')
     rows = cursor.execute("Select first_name,last_name,score,Assessment FROM Competency_Assessment_Results WHERE user_id =?",(user_id, )).fetchall()
     columns = ['first_name','last_name','score','Assessment']
     pprint(f"{'First':<15} {'Last':<10} {'Score':<4} {'Assessment':<28}")
     for row in rows:
       pprint(f"{row[0] if row[0]!= None else '':15} {row[1] if row[1]!= None else '':<15} {row[2] if row[2]!= None else '':<4} {row[3] if row[3]!= None else '':<28}")

while True: user_menu()