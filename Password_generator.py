import random
def password(n):
 v=0
 try:
  if n>len(l):
   v=n-len(l)
   for i in range(len(l)):
    f=l[i]
    u=str(random.choice(f))
    t.append(u)
   for i in range(v):
    f=random.choice(l)
    u=str(random.choice(f))
    t.append(u)
   return t
  if n<=len(l):
   f=l[i]
   u=str(random.choice(f))
   t.append(u)
  return t
 except:
     print("enter the correct value ")
l1=[chr(x) for x in range(ord('a'),ord('z')+1)]
l2=[chr(x) for x in range(ord('A'),ord('Z')+1)]
l3=[x for x in range(0,10)]
l4=['!','@','#','$','%','^','&','*']
l=[]
t=[]
l.append(l1)     
l.append(l2)     
l.append(l3)     
l.append(l4)
try:
 n=int(input("enter the length of the password "))
 z=input("Do you want a strong password anser strong or weak ").upper()
 if z!="STRONG" and z!="WEAK":
  raise ValueError
 t=password(n)
 d="".join(t)
 d=d.split()
 for i in range(len(d)):
   print(f"You have asked for a {z} password...")
   print(d[i],sep='',end='')
except:
 print("enter the valid option")   
       