import os
def mad():
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


def guru():
    import random
    from time import sleep
    lst=['Yes','Surely','Of course','Absolutely','Indeed','Certainly','Definitely','Affirmative','No','Never','Nope','Under no circumstances','Of course not','Probably not','Maybe','Perhaps','Possibly','Conceivably']
    a=1
    pranklst=[1,2]
    print('Welcome to "Ask Mr.Guruji"');sleep(2)
    print('You can ask him any yes or no questions');sleep(2)
    print('All his answers will be 100% true, because he has magical powers');sleep(2)
    print("Don't beleive us? Check it out for yourselves");sleep(2)
    while a==1 or a==2:
        if a==2:
            input('Ask me another question child:')
            b=random.choice(lst)
            c=random.choice(pranklst)
            if c==2:
                if b=='No' or b=='Never' or b=='Nope' or b=='Under no circumstances' or b=='Of course not':
                    print('Yes');sleep(2)
                    print('Sorry, I was just kidding. The real answer is',b);sleep(3)
                else:
                    print(b);sleep(2.5)
            else:
                print(b);sleep(2.5)
        else:
            a=2
            input('Ask me a question child:')
            b=random.choice(lst)
            c=random.choice(pranklst)
            if c==2:
                if b=='No' or b=='Never' or b=='Nope' or b=='Under no circumstances' or b=='Of course not':
                    print('Yes');sleep(2)
                    print('Sorry, I was just kidding. The real answer is',b);sleep(3)
                else:
                    print(b);sleep(2.5)
            else:
                print(b);sleep(2.5)



def rock():
    print('Work in progress')


def odd():
    rules='''In Odd or Even the players prepare by deciding who will be assigned odd and who will be even.
    Then both players quickly and simultaneously thrust a fist into the center showing the number of their
    choice on their hand(from 0 to 6). The sum total of fingers displayed is either odd or even. If the result
    is odd, then the person who called odd wins the toss and if the result is even, the person who called even
    wins the toss. The player who won the toss can choose either batting or bowling. If the player chooses batting
    both players start thrusting a fist sumultaneously into the center and show the number of their choice(0 to 6)
    on their hand. These numbers must be added as the game progressess. This total sum is called runs. Once the person
    who is bowling shows the same number as the person batting the batsman gets out. When the batsman gets out the bowler
    becomes the next batsman and the game continues as before. Once both players have got out the player with most runs wins.'''
    print('Welcome to Odd or Even')
    yn=input('''Do you want a tutorial on how to play?
    Enter yes or no:''')
    if yn=='yes' or yn=='Yes' or yn=='YES' or yn=='y':
          print(rules)
          input('Press Enter To Continue')
    u=input('Choose Odd or Even:')
    import random
    L=[0,1,2,3,4,5,6]
    a=int(input('Enter any number from 0 to 6:'))
    if a not in L:
          input('Nice try, but that aint gonna slide!')
          exit()
    b=random.choice(L)
    print('My choice is',b)
    c=a+b
    if c%2==0:
          if u=='even' or u=='Even' or u=='EVEN':
             j='You have won the toss'
             print('You have won the toss')
          else:
              j='You have lost the toss'
              print('You have lost the toss')
    else:
        if u=='odd' or u=='Odd' or u=='ODD':
            j='You have won the toss'
            print('You have won the toss')
        else:
            j='You have lost the toss'
            print('You have lost the toss')
    if j=='You have won the toss':
          d=input('Choose batting or bowling:')
          if d=='batting' or d=='Batting' or d=='BATTING':
                w='bowling'
          else:
                w='batting'
          print('Your choice is',d,'so I am',w)
          print('Lets start!')
          if d=='batting' or d=='Batting' or d=='BATTING':
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=nn
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+nn
                
                print('I chose',pp)
                print('You are out')
                print('Your runs are',sum_1)
                input('Press enter to continue')
                print('Now you are',w,'and I am',d)
                print('Lets start!')
                sum_2=0
                vv=int(input('Enter the number:'))
                cc=random.choice(L)
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                sum_2+=cc
                if sum_2>sum_1 and vv!=cc:
                          print('I chose',cc)
                          print('My runs are are',sum_2)
                          print('Your runs are',sum_1)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+cc
                    if sum_2>sum_1:
                          print('I chose',cc)
                          print('My runs are are',sum_2)
                          print('Your runs are',sum_1)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',cc)
                print('I am Out')
                print('My runs are are',sum_2)
                print('Your runs are',sum_1)
                if sum_1>sum_2:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
          else:
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=cc
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+cc
                
                print('I chose',cc)
                print('I am Out')
                print('My runs are',sum_2)
                input('Press enter to continue')
                print('Now you are',w,'and I am',d)
                print('Lets start!')
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=nn
                if sum_1>sum_2 and nn!=pp:
                          print('I chose',pp)
                          print('My runs are',sum_2)
                          print('Your runs are',sum_1)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+nn
                    if sum_1>sum_2:
                          print('I chose',pp)
                          print('My runs are',sum_2)
                          print('Your runs are',sum_1)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                sum_1=sum_1-nn
                print('I chose',pp)
                print('You are out')
                print('Your runs are',sum_1)
                print('My runs are',sum_2)
                if sum_1>sum_2:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                
    else:
          M=['Batting','Bowling']
          d=random.choice(M)
          if d=='Batting':
                w='Bowling'
          else:
                w='Batting'
          print('My choice is',d,'so you are',w)
          print('Lets start!')
          if d=='Batting':
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=pp
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+pp
                sum_1=sum_1-pp
                print('I chose',pp)
                print('I am out')
                print('My runs are',sum_1)
                input('Press enter to continue')
                print('Now you are',d,'and I am',w)
                print('Lets start!')
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=vv
                if sum_2>sum_1 and vv!=cc:
                          print('I chose',cc)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+vv
                    if sum_2>sum_1:
                          print('I chose',cc)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',cc)
                print('You are Out')
                print('Your runs are',sum_2)
                print('My runs are',sum_1)
                if sum_1>sum_2:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
          else:
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=vv
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+vv
                
                print('I chose',cc)
                print('You are Out')
                print('Your runs are',sum_2)
                input('Press enter to continue')
                print('Now you are',d,'and I am',w)
                print('Lets start!')
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=pp
                if sum_1>sum_2 and nn!=pp:
                          print('I chose',pp)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+pp
                    if sum_1>sum_2:
                          print('I chose',pp)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                sum_1=sum_1-pp
                print('I chose',pp)
                print('I am out')
                print('My runs are',sum_1)
                print('Your runs are',sum_2)
                if sum_1>sum_2:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
    if yn!='yes' or yn!='Yes' or yn!='YES':
          input('Wrong input')
          exit()
    if yn=='no' or yn=='No' or yn=='NO':
     u=input('Choose Odd or Even:')
    import random
    L=[0,1,2,3,4,5,6]
    a=int(input('Enter any number from 0 to 6:'))
    if a not in L:
          input('Nice try, but that aint gonna slide!')
          exit()
    b=random.choice(L)
    print('My choice is',b)
    c=a+b
    if c%2==0:
          if u=='even' or u=='Even' or u=='EVEN':
             j='You have won the toss'
             print('You have won the toss')
          else:
              j='You have lost the toss'
              print('You have lost the toss')
    else:
        if u=='odd' or u=='Odd' or u=='ODD':
            j='You have won the toss'
            print('You have won the toss')
        else:
            j='You have lost the toss'
            print('You have lost the toss')
    if j=='You have won the toss':
          d=input('Choose batting or bowling:')
          if d=='batting' or d=='Batting' or d=='BATTING':
                w='bowling'
          else:
                w='batting'
          print('Your choice is',d,'so I am',w)
          print('Lets start!')
          if d=='batting' or d=='Batting' or d=='BATTING':
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=nn
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+nn
                sum_1=sum_1-nn
                print('I chose',pp)
                print('You are out')
                print('Your runs are',sum_1)
                input('Press enter to continue')
                print('Now you are',w,'and I am',d)
                print('Lets start!')
                sum_2=0
                vv=int(input('Enter the number:'))
                cc=random.choice(L)
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                sum_2+=cc
                if sum_2>sum_1 and vv!=cc:
                          print('I chose',cc)
                          print('My runs are are',sum_2)
                          print('Your runs are',sum_1)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+cc
                    if sum_2>sum_1:
                          print('I chose',cc)
                          print('My runs are are',sum_2)
                          print('Your runs are',sum_1)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',cc)
                print('I am Out')
                print('My runs are are',sum_2)
                print('Your runs are',sum_1)
                if sum_1>sum_2:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
          else:
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=cc
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+cc
                
                print('I chose',cc)
                print('I am Out')
                print('My runs are',sum_2)
                input('Press enter to continue')
                print('Now you are',w,'and I am',d)
                print('Lets start!')
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=nn
                if sum_1>sum_2 and nn!=pp:
                          print('I chose',pp)
                          print('My runs are',sum_2)
                          print('Your runs are',sum_1)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+nn
                    if sum_1>sum_2:
                          print('I chose',pp)
                          print('My runs are',sum_2)
                          print('Your runs are',sum_1)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',pp)
                print('You are out')
                print('Your runs are',sum_1)
                print('My runs are',sum_2)
                if sum_1>sum_2:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                
    else:
          M=['Batting','Bowling']
          d=random.choice(M)
          if d=='Batting':
                w='Bowling'
          else:
                w='Batting'
          print('My choice is',d,'so you are',w)
          print('Lets start!')
          if d=='Batting':
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=pp
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+pp
                
                print('I chose',pp)
                print('I am out')
                print('My runs are',sum_1)
                input('Press enter to continue')
                print('Now you are',d,'and I am',w)
                print('Lets start!')
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=vv
                if sum_2>sum_1 and vv!=cc:
                          print('I chose',cc)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+vv
                    if sum_2>sum_1:
                          print('I chose',cc)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('You win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',cc)
                print('You are Out')
                print('Your runs are',sum_2)
                print('My runs are',sum_1)
                if sum_1>sum_2:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
          else:
                sum_2=0
                vv=int(input('Enter the number:'))
                if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                cc=random.choice(L)
                sum_2+=vv
                while vv!=cc:
                    print('I choose',cc)
                    vv=int(input('Enter the number:'))
                    if vv not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    cc=random.choice(L)
                    sum_2=sum_2+vv
                
                print('I chose',cc)
                print('You are Out')
                print('Your runs are',sum_2)
                input('Press enter to continue')
                print('Now you are',d,'and I am',w)
                print('Lets start!')
                sum_1=0
                nn=int(input('Enter the number:'))
                if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                pp=random.choice(L)
                sum_1+=pp
                if sum_1>sum_2 and nn!=pp:
                          print('I chose',pp)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                while nn!=pp:
                    print('I choose',pp)
                    nn=int(input('Enter the number:'))
                    if nn not in L:
                      input('Nice try, but that aint gonna slide!')
                      exit()
                    pp=random.choice(L)
                    sum_1=sum_1+pp
                    if sum_1>sum_2:
                          print('I chose',pp)
                          print('My runs are are',sum_1)
                          print('Your runs are',sum_2)
                          print('I win')
                          input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                          exit()
                
                print('I chose',pp)
                print('I am out')
                print('My runs are',sum_1)
                print('Your runs are',sum_2)
                if sum_1>sum_2:
                      print('I win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                elif sum_1==sum_2:
                      print('It is a tie')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')
                else:
                      print('You win')
                      input('                        ᴬ ᵖʳᵒʲᵉᶜᵗ ᵇʸ ᴬʳᶠᵃⁿ ⱽ ᴬⁿᵘˡᵃˡ')




def pokemon():
    from time import sleep
    import webbrowser
    import random
    print('Welcome to "What type of pokemon are you?"');sleep(1)

    while True: #Game continue loop
      input('Enter your name?: ')
      input('Enter your year of birth?: ')
      input('Enter your favourite colour?: ')
      input('Enter your favourite number?: ')
      input('What is your primary hand?: ')
      input('Are you athletic?: ')
      input('Are you a vegetarian?: ')
      input('Are you impatient?: ')
      input('You walk down a dark alleyway and see a man get attacked, what do you do?: ')
      input('Do you prefer day or night?: ')
      gen1no=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 136, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 150, 151]
      gen1pok=["Bulbasaur","Ivysaur","Venusaur","Charmander","Charmeleon","Charizard","Squirtle","Wartortle","Blastoise","Caterpie","Metapod","Butterfree","Weedle","Kakuna","Beedrill","Pidgey","Pidgeotto","Pidgeot","Rattata","Raticate","Spearow","Fearow","Ekans","Arbok","Pikachu","Raichu","Sandshrew","Sandslash","Nidoran♀","Nidorina","Nidoqueen","Nidoran♂","Nidorino","Nidoking","Clefairy","Clefable","Vulpix","Ninetales","Jigglypuff","Wigglytuff","Zubat","Golbat","Oddish","Gloom","Vileplume","Paras","Parasect","Venonat","Venomoth","Diglett","Dugtrio","Meowth","Persian","Psyduck","Golduck","Mankey","Primeape","Growlithe","Arcanine","Poliwag","Poliwhirl","Poliwrath","Abra","Kadabra","Alakazam","Machop","Machoke","Machamp","Bellsprout","Weepinbell","Victreebel","Tentacool","Tentacruel","Geodude","Graveler","Golem","Ponyta","Rapidash","Slowpoke","Slowbro","Magnemite","Magneton","Farfetch'd","Doduo","Dodrio","Seel","Dewgong","Grimer","Muk","Shellder","Cloyster","Gastly","Haunter","Gengar","Onix","Drowzee","Hypno","Krabby","Kingler","Voltorb","Electrode","Exeggcute","Exeggutor","Cubone","Marowak","Hitmonlee","Hitmonchan","Lickitung","Koffing","Weezing","Rhyhorn","Rhydon","Chansey","Tangela","Kangaskhan","Horsea","Seadra","Goldeen","Seaking","Staryu","Starmie","Mr. Mime","Scyther","Jynx","Electabuzz","Magmar","Pinsir","Tauros","Magikarp","Gyarados","Lapras","Ditto","Eevee","Vaporeon","Jolteon","Flareon","Porygon","Omanyte","Omastar","Kabuto","Kabutops","Aerodactyl","Snorlax","Articuno","Zapdos","Moltres","Dratini","Dragonair","Dragonite","Mewtwo","Mew"]
      n=random.choice(gen1no)
      p=gen1pok[n-1]
      print("\nFinding the perfect pokemon for you",end='');sleep(0.5)
      print('.',end='');sleep(0.5)
      print('.',end='');sleep(0.5)
      print('.',end='');sleep(0.5)
      print('.');sleep(0.5)
      print("\nPokedex Number:",n);sleep(1)
      print("Pokemon:",p);sleep(1)
      yeno=str(input('Do you want to know more about this pokemon?:'))
      if yeno== 'Yes' or yeno=='yes' or yeno== 'YES' or yeno=='yES' or yeno=='y':
        decoy=1;sleep(0.5)   
        print('You will now be redirected to an external website');sleep(0.7)
        print('A project by GamerBro6q7');sleep(2.5)
        webbrowser.open('https://en.wikipedia.org/wiki/List_of_generation_I_Pok%C3%A9mon#Bulbasaur')
        break
      elif yeno== 'No' or yeno=='no' or yeno=='NO' or yeno=='nO' or yeno=='n':
          print('Thank you for playing!');sleep(0.7)
          break



    

    
while True:
    print('\nChoose a game:\n1)Madlib Generator\n2)Mr.Guruji\n3)Rock Paper Scissors\n4)Odd or Even\n5)What type of pokemon are you?\n6)Return to Main Menu')
    ch=int(input('Enter your choice: '))
    if ch==1:
        print()
        mad()
    elif ch==2:
        print()
        guru()
    elif ch==3:
        print()
        rock()
    elif ch==4:
        print()
        odd()
    elif ch==5:
        print()
        pokemon()
    elif ch==6:
        os.system('4Account.py')
        break
    else:
        print('Invalid input, try again!')
        continue
