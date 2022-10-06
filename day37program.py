a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter thrid number:"))
e=[]
e.append(a)
e.append(b)
e.append(c)
for i in range(0,3):
    for j in range(0,3):
        for k in range(0,3):
            
                if(i!=j&j!=k&k!=i):
                    print(e[i],e[j],e[k])
