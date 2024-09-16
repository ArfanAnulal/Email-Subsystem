input('Welcome to story creator')
from time import sleep
while True:
    a=input('Enter a name:')
    b=input('Enter any place:')
    c=input('Enter an item:')
    d=input('Enter a living thing, it can also be imaginary:')
    e=input('Enter something gross:')
    f=input('Enter something you have, it can also be a part of your body:')
    g=input('Enter a word an action ending with -ed:')
    h=input('Enter another living thing, it can also be imaginary:')
    i=input('Enter an action word:')
    print('Loading',end='');sleep(0.5)
    print('.',end='');sleep(0.5)
    print('.',end='');sleep(0.5)
    print('.',end='');sleep(0.5)
    print('.');sleep(0.5)
    print('Hello, my name is',a,'Today I went to',b,'and ate',c,'then a',d,'came and threw',e,'into my',f,'I got so angry that I',g,'the',d,'After all this, my',h,i,'me and I went back home');sleep(5)
    a=input('Do you want to play again?:')
    if a=='yes' or a=='Yes' or a=='YES':
        continue
    else:
        break
input()

