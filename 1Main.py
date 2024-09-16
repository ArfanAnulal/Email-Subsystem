#This file for the main page
import os


print('Select an operation:\n1)Sign In\n2)Sign Up\n3)Exit')
while True:
    ch=int(input('Enter your choice: '))
    print()
    if ch==1:
        os.system('2Sign_In.py')
        break
    elif ch==2:
        os.system('3Sign_Up.py')
        break
    elif ch==3:
        break
    else:
        print('\nInvalid input, try again\n')
        continue
