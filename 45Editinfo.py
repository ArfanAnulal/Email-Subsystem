#This file is for the details of account holder
import pickle
import os
from tabulate import tabulate #To show MAIL in tabular form
from time import sleep


import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem') #mysql connection
cur=mycon.cursor() #mysql cursor


f=open("idstoringfile.dat", "rb")
idname = pickle.load(f) #Loading mail id of current user
f.close()


while True:
    cur.execute("SELECT first_name,last_name,dob,gender,city_of_birth FROM user_details where mail_id='{}'".format(idname)) #contains all from checklist
    data=cur.fetchone()
    l=[] #empty list for tabulation purposes
    (first_name,last_name,dob,gender,city_of_birth)=data #'i' is in tuple form, so we unpack the tuple using this statement
    r=[first_name,last_name,dob,gender,city_of_birth] #creating a new list where there is 'item number),Item, Current status'
    l.append(r) #appending the above list to the list in line
    print()
    print(tabulate(l, headers=['First Name','Last Name', 'Date Of Birth','Gender','City of Birth']),'\n','\n') #tabulating list lst with headings Item and Status

    
    print('Select an operation:\n1)Change First Name\n2)Change Last Name\n3)Change Date Of Birth\n4)Change Gender\n5)Change City Of Birth\n6)Exit to Main Menu')
    ch=input('Enter your choice: ')
    print()
    if ch=='1':
        fname=input('Enter new First Name: ')
        cur.execute("update user_details set first_name='{}' where mail_id='{}'".format(fname,idname))
        mycon.commit()
        print('First Name changed to',fname,'successfully!');sleep(1)
        print()
    elif ch=='2':
        lname=input('Enter new Last Name: ')
        cur.execute("update user_details set Last_name='{}' where mail_id='{}'".format(lname,idname))
        mycon.commit()
        print('Last Name changed to',lname,'successfully!');sleep(1)
        print()
    elif ch=='3':
        dob=input('Enter new Date of Birth as YYYY-MM-DD: ')
        cur.execute("update user_details set DOB='{}' where mail_id='{}'".format(dob,idname))
        mycon.commit()
        print('Date of Birth changed to',dob,'successfully!');sleep(1)
        print()
    elif ch=='4':
        gender=input('Enter new gender as M/F: ')
        cur.execute("update user_details set gender='{}' where mail_id='{}'".format(gender,idname))
        mycon.commit()
        print('Gender changed to',gender,'successfully!');sleep(1)
        print()
    elif ch=='5':
        secques=input('Enter new city of birth: ')
        cur.execute("update user_details set city_of_birth='{}' where mail_id='{}'".format(secques,idname))
        mycon.commit()
        print('City of Birth changed to',secques,'successfully!');sleep(1)
        print()
    elif ch=='6':
        os.system('4Account.py')
        break
    else:
        print('Invalid input!, try again')
        continue

