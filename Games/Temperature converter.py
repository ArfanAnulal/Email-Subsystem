a=int(input('Enter the temperature:'))
b=int(input('''Do you want to 1-Convert farenheit to celsius
               2-Convert celsius to farenheit
               3-Convert farenheit to kelvin
               4-Convert kelvin to farenheit
               5-Convert celsius to kelvin
               6-Convert kelvin to celsius
               Enter your selection:'''))
if b==1:
    print((a-32)*5/9)
elif b==2:
    print((a*9)/5+32)
elif b==3:
    print(((a-32)*5)/9+273.15)
elif b==4:
    print(((a-273.15)*9)/5+32)
elif b==5:
    print(a+273.15)
elif b==6:
    print(a-273.15)
else:
    print('Invalid input,please run the program again')
    
input('Press Enter to exit')
