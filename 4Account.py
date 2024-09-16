#Password in line 13
#This file is for the details of account holder
import pickle
import os


def convertTuple(idtup):
    std=''.join(idtup) #converting tuple to string
    return std


import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='<YOURPASSWORD>',database='email_subsystem') #mysql connection


f=open("idstoringfile.dat", "rb")
idname = pickle.load(f) #Loading mail id of current user
f.close()


cur=mycon.cursor()
cur.execute("SELECT first_name FROM user_details where mail_id='{}'".format(idname)) #retrieving name of current user
data=cur.fetchone()
name=convertTuple(data) #converting tuple to string
print('\nWelcome,',name,'\n')


while True:
    print('Select an operation:\n1)Messages\n2)Checklist\n3)Photos\n4)Games\n5)Edit Info\n6)Sign Out')

    ch=int(input('Enter your choice: '))
    if ch==1:
        os.system('41Messages.py')
        break
    elif ch==2:
        os.system('42Checklist.py')
        break
    elif ch==3:
        print('h')
        #os.system('Photos.py')
        break
    elif ch==4:
        os.system('44Games.py')
        break
    elif ch==5:
        os.system('45Editinfo.py')
        break
    elif ch==6:
        print()
        os.system('1Main.py')
        break
    else:
        print('Incorrect input, try again!')
  
        
