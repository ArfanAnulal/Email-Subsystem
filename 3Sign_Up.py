#This page is for signing up
import os
import mysql.connector as mc

def convertTuple(idtup):
    std=''.join(idtup)
    return std


def check(idname):
    for i in idname:
        if i=='@':
            print('Do not enter the email service',end=', ')
            return 1
            break
        else:
            continue
    
    mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem')
    cur=mycon.cursor()        
    cur.execute("SELECT mail_id FROM user_details")
    data=cur.fetchall()
    for j in data:
        if convertTuple(j).lower()==idname.lower()+'@voidmail.com':
            return 2
            mycon.close()
            break
        else:
            continue
    return 0

  
while True:
    try:
        fname=input('Enter your first name: ')
        fname=fname.capitalize() #Capitalizing
        lname=input('Enter your last name: ')
        lname=lname.capitalize() #Capitalizing
        idname=input('Create your mail id(do not enter the mail service): ')#Collecting details from users
        s=check(idname) #Check if mail service was entered or if id exists
        if s==1:
            print('Try again\n')
            continue
        elif s==2:
            print('ID already exists, try again\n')
            continue
        else:
            idname=idname+'@voidmail.com'
            password=input('Enter your password: ')
            DOB=input('Enter your date of birth as YYYY-MM-DD: ')
            gender=input('Enter your gender M/F: ')
            gender=gender.upper()
            secques=input('Which city where you born in?: ')
            secques=secques.capitalize() #Capitalizing

            
            mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem')
            #if mycon.is_connected()==False:
            #    print('Connection Failed')
            #else:
            #    print('Connection Successful')


            cur=mycon.cursor()
            cur.execute("SELECT * FROM user_details")
            cur.fetchall()
            rc = cur.rowcount  #for knowing the current number of rows
            rc+=1
            rc='{0:03}'.format(rc)


            cur.execute("insert into user_details values('{}','{}','{}','{}','{}','{}','{}','{}')".format(rc,fname,lname,idname,password,DOB,gender,secques))
            mycon.commit()
            mycon.close()
            break
    except mc.Error as err:
        print("\nSomething went wrong: {}".format(err))
        print('Try again\n')
        continue


if s==0:
    input('\nYou have successfully signed up!\n')
    os.system('1Main.py')
