#This file is for checklist
import pickle
import os
from tabulate import tabulate #To show checklist items in tabular form


def convertTuple(idtup):
    std=''.join(idtup) #converting tuple to string
    return std


import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem') #mysql connection
cur=mycon.cursor() #mysql cursor


#f=open("idstoringfile.dat", "rb")
f=open('test.dat','rb')
idname = pickle.load(f) #Loading mail id of current user
f.close()


while True: #while loop for selecting operation to perform with checklist
    print('\nSelect an operation:\n1)Add Item\n2)Check status\n3)Delete item\n4)Exit to Main menu')
    ch=int(input('Enter your choice: '))
    print() #gap for aesthetic purposes
    if ch==1:
        stat='Not Done' #default status of item in checklist
        item=input('\nEnter Item: ')
        cur.execute("SELECT * FROM checklist") #contains all from checklist
        cur.fetchall()
        rc = cur.rowcount  #for knowing the current number of rows
        rc+=1
        rc='{0:03}'.format(rc) #changing format of number to 00x
        cur.execute("Insert into checklist values('{}','{}','{}','{}')".format(rc,idname,item,stat))
        mycon.commit()
        print('Item added successfully!')
        continue


    elif ch==2:
        k=0 #Item number
        cur.execute("SELECT item,status FROM checklist where mail_id='{}'".format(idname)) #Selecting all from checklist where the mail id is of current user
        data=cur.fetchall()
        l=[] #empty list for tabulation purposes
        for i in data:
            k+=1
            (stuff,sta)=i #'i' is in tuple form, so we unpack the tuple using this statement
            r=[k,')',stuff, sta] #creating a new list where there is 'item number),Item, Current status'
            l.append(r) #appending the above list to the list in line
        print(tabulate(l, headers=['Item', 'Status'])) #tabulating list lst with headings Item and Status
        c=input('\nDo you want to change status? Y/N: ')
        if c=='Y' or c=='y':
            d='Done' #defaulr value of new status
            m=int(input('Enter the item number: '))
            p=data[m-1] #the variable data stores all from checklist where the mail id is of current user. we then use m-1 as list starts at index 0
            (item,stat)=p #unpacking the tuple 'p'
            cur.execute("update checklist set status='{}' where mail_id='{}' AND item='{}'".format(d,idname,item)) #changing status
            mycon.commit()
        else:
            continue

        
    elif ch==3:
        k=0 #Item number
        cur.execute("SELECT item,status FROM checklist where mail_id='{}'".format(idname)) #Selecting all from checklist where the mail id is of current user
        data=cur.fetchall()
        l=[] #empty list for tabulation purposes
        for i in data:
            k+=1
            (stuff,sta)=i #'i' is in tuple form, so we unpack the tuple using this statement
            r=[k,')',stuff, sta] #creating a new list where there is 'item number),Item, Current status'
            l.append(r) #appending the above list to the list in line
        print(tabulate(l, headers=['Item', 'Status'])) #tabulating list lst with headings Item and Status
        c=input('\nDo you want to delete an item? Y/N: ')
        if c=='Y' or c=='y':
            m=int(input('Enter the item number: '))
            p=data[m-1] #the variable data stores all from checklist where the mail id is of current user. we then use m-1 as list starts at index 0
            (item,stat)=p #unpacking the tuple 'p'
            cur.execute("delete from checklist where mail_id='{}' AND item='{}'".format(idname,item)) #deleting item
            mycon.commit()
        else:
            continue

            
    elif ch==4:
        os.system('4Account.py')
        break

    
    else:
        print('Incorrect input, try again!')
        continue
