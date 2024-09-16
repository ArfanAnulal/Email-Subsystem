#This file is the sign up page
import pickle
f=open("idstoringfile.dat", "wb")
import os
from time import sleep


def convertTuple(idtup):
    std=''.join(idtup)
    return std

def forgotpwd():
    os.system('$Forgotpwd.py')
    

m=0 #variable for checking if inputted mail id exists in line 33


import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem') #mysql connection
#if mycon.is_connected()==False:
#    print('Connection Failed')
#else:
#    print('Connection Successful')


cur=mycon.cursor()
cur.execute("SELECT mail_id FROM user_details")
data=cur.fetchall() #contains all mail id from user_details
k=0 #variable for checking if non-existing mail has been entered 5 times


while True: #while loop for entering mail id
    idname=input('Enter your Mail ID: ')
    for i in data: #for loop to iterate through all items in tuple 'data'
        stringid=convertTuple(i) #convert tuple to string
        if stringid==idname:#check if user entered mail id exists in database
            m+=1
            break
        elif stringid!=idname and k<15: #if user entered id does not exist go to next iteration of loop while adding +1 to the variable k in line 36
            k+=1
            continue
        elif k==15: #if user enters non-existent mail for 5 times for loop breaks
            break
    if m==1: #to check if mail id was found and to terminate while loop
        break
    elif k==15: #if user enters non-existent mail for 5 times while loop breaks and redirect to main menu
        print('\nYou have entered a non-existing mail id 5 times\nTry creating a new mail id')
        print('\nRedirecting',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.\n');sleep(0.5)
        
        os.system('1Main.py')
        break
    else:
        print('\nMail ID does not exist, try again\n')

        
t=0 #variable for checking number of times wrong password was entered from line 72
while True:
    password=input('Enter your password: ')
    cur.execute("SELECT password FROM user_details where mail_id='{}'".format(idname))
    data=cur.fetchone()
    stringpassword=convertTuple(data) #convert tuple to string
    if password==stringpassword:
        print('Redirecting',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.',end='');sleep(0.5)
        print('.');sleep(0.5)
        pickle.dump(stringid, f)
        f.close()
        os.system('4Account.py')
        break
    elif password!=stringpassword and t<4:
        t+=1
        print('Incorrect password\n')
        continue
    elif t==4:
        mp=input('Do you want to change your password? Y/N: ')
        if mp.upper()=='YES' or mp.upper()=='Y':
            forgotpwd()
            break
        else:
            print('\nYou have entered an incorrect password 5 times')
            print('Redirecting',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.\n');sleep(0.5)
            
            os.system('1Main.py')
            break
