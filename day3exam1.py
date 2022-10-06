n=int(input("enter the number"))
if(n==0):
    print(0)
if(n==1):
    print(1)
r=0
t=0
u=1
for i in range(1,n+1):
    r=u+t
    t=u
    u=r
print(r)
