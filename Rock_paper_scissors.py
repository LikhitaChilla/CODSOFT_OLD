import random
def winner(ch,c,u):
    x=["r","p","s"]
    t=random.choice(x)
    print(f"you know my choice ...It's  {t} ")
    if t==ch:
        print("oops ! we have got same brain cells")
        return c,u
    elif t=="r":
        if ch=="p":
            print("You won dear")
            return c,u+1
        elif ch=="s":
            print("I won :)")
            return c+1,u
    elif t=="p":
        if ch=="s":
            print("You won dear ")
            return c,u+1
        elif ch=="r":
            print("I won :)")
            return c+1,u
    elif t=="s":
        if ch=="r":
            print("You won dear")
            return c,u+1
        elif ch=="p":
            print("I won :)")
            return c+1,u
    else:
        print("enter the correct choice ")  
        return c,u     
print("Hello I am a comuputer.Let's play enter your choice as r or p or s ")                     

c=0
u=0
r=2
while(r>0):
 for i in range(0,4):
    ch=input("enter your choice ")
    ch=ch.lower()
    c,u=winner(ch,c,u)
 if c>u:
    print(f"You got {u} and I got {c} I won :)")
 elif c<u:
    print(f" You got {u} anf I got {c} You won dear :)")
 elif c==u:
    print(f" We both got {u} It's a tie ....We have got same brain cells!!!")
 r=int(input("Are you willing to play again...\n if yes then enter 1 if not enter 0 "))
 if r==1:
     print("Let's kill it dear... Let's play again")
 elif r==0:
     print("Had a nice game with you","You are always welcome to play with me :)",sep="\n")     
                



