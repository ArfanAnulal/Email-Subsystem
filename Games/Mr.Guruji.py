import random
from time import sleep
lst=['Yes','Surely','Of course','By all means','Absolutely','Indeed','Certainly','Definitely','Beyond a doubt','Affirmative','No','Never','Nope','Under no circumstances','Of course not','Probably','Maybe','Perhaps','Possibly','Conceivably']
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
                print('Sorry, I was just kidding. The real answer is No');sleep(3)
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
