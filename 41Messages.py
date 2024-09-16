#This file is for the details of account holder
import pickle
import os
from tabulate import tabulate #To show MAIL in tabular form


def f_comma(my_str, group=40, char='\n'):
    my_str = str(my_str)
    return char.join(my_str[i:i+group] for i in range(0, len(my_str), group))





import mysql.connector as mc
mycon=mc.connect(host='localhost', user='root',password='nafraJ20',database='email_subsystem') #mysql connection
cur=mycon.cursor() #mysql cursor


f=open("idstoringfile.dat", "rb")
idname = pickle.load(f) #Loading mail id of current user
f.close()


while True:
    print('\nSelect an operation:\n1)Send Mail\n2)Inbox\n3)Sent by you\n4)Exit to Main Menu')

    ch=int(input('Enter your choice: '))
    print()
    if ch==1:
        stat='Unread'
        rec=input('Enter Mail ID of recipient: ')
        sub=input('Enter subject of mail: ')
        m=input('Enter mail: ')
        mail=f_comma(m)
        print(mail)
        cur.execute("SELECT * FROM inbox") #contains all from checklist
        cur.fetchall()
        rc = cur.rowcount  #for knowing the current number of rows
        rc+=1
        rc='{0:03}'.format(rc) #changing format of number to 00x
        cur.execute('''Insert into inbox values("{}","{}","{}","{}","{}","{}")'''.format(rc,idname,rec,sub,mail,stat))
        mycon.commit()
        print('Mail sent successfully!\n')
        continue

    
    elif ch==2:
        k=0
        cur.execute("SELECT fmail_id,subject,mail FROM inbox where tmail_id='{}'".format(idname)) #contains all from checklist
        data=cur.fetchall()
        l=[] #empty list for tabulation purposes
        for i in data:
            k+=1
            (sender,subject,mail)=i #'i' is in tuple form, so we unpack the tuple using this statement
            r=[k,')',sender, subject, mail] #creating a new list where there is 'mail number),from, subject, mail'
            l.append(r) #appending the above list to the list in line
        print()
        print(tabulate(l, headers=['From','Subject', 'Mail']),'\n','\n') #tabulating list lst with headings From, subject and mail
    elif ch==3:
        k=0
        cur.execute("SELECT tmail_id,subject,mail FROM inbox where fmail_id='{}'".format(idname)) #contains all from checklist
        data=cur.fetchall()
        l=[] #empty list for tabulation purposes
        for i in data:
            k+=1
            (receiver,subject,mail)=i #'i' is in tuple form, so we unpack the tuple using this statement
            r=[k,')',receiver, subject, mail] #creating a new list where there is 'item number),Item, Current status'
            l.append(r) #appending the above list to the list in line
        print()
        print(tabulate(l, headers=['To','Subject', 'Mail']),'\n','\n') #tabulating list lst with headings Item and Status

        
    elif ch==4:
        print()
        os.system('4Account.py')
        break
    else:
        print('Incorrect input, try again!')
