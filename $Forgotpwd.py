#Password in line 15
from time import sleep
import os


def convertTuple(idtup):
    std=''.join(idtup)
    return std


lst=[]
d=0
m=0
import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='<YOURPASSWORD>',database='email_subsystem') #mysql connection
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

        d=1
        os.system('1Main.py')
        break
    else:
        print('\nMail ID does not exist, try again\n')
mycon.close()


if d!=1:
    import mysql.connector as mc
    mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem') #mysql connection
    cur=mycon.cursor()
    cur.execute("SELECT city_of_birth FROM user_details where mail_id='{}'".format(idname))
    data=cur.fetchall() #contains all mail id from user_details
    dat=convertTuple(data[0]).lower()



    s=0
    while True:
        ch=input('Enter your city of birth: ')
        ch=ch.lower()
        if dat==ch:
            passwd=input('Enter new password: ')
            cur.execute("update user_details set password='{}' where mail_id='{}'".format(passwd,idname))
            mycon.commit()
            print('Password changed successfully!');sleep(1)
            print()
            os.system('1Main.py')
            break
        elif dat!=ch and s<4:
            s+=1
            print('Incorrect, try again\n')
            continue
        elif s==4:
            print('\nYou have entered an incorrect answer 5 times')
            print('Redirecting',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.',end='');sleep(0.5)
            print('.\n');sleep(0.5)

            os.system('1Main.py')
            break










