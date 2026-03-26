import random
name1=input("enter the player1:")
name2=input("enter the player2:")
d1=random.randint(1,25)
d2=random.randint(1,25)
s1=25
s2=25
print("___player 1___")
while True:
    g=int(input("enter the number"))
    s1=s1-1
    if(d1==g):
        print("ur guess is correct")
        break
    elif(d1>g):
        print("ur guess is less")
    else:
        print("ur guess is more")
    
    
print("___player 2___")
while True:
    g=int(input("enter the number"))
    s2=s2-1
    if(d2==g):
        print("ur guess is correct")
        break
    elif(d2>g):
        print("ur guess is less")
    else:
        print("ur guess is more")
if(s1==s2):
    print ("match is draw")
elif(s1>s2):
    print("winner is",name1)
else:
    print("winner is",name2)
    
    