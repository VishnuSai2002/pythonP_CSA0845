python=int(input("enter python marks:"))
cprogramming=float(input("enter cprogramming  marks:"))
mathematics=int(input("enter mathematics marks:"))
physics=int(input("enter physics marks:"))
total=python+cprogramming+mathematics+physics
print("total:",total)
aggregate=total/4
print("aggregate:",aggregate)
if python>=40 and cprogramming>=40 and mathematics>=40 and physics>=40:
    if aggregate==40:
        print("pass division")
    elif aggregate>=40 and aggregate<50:
        print("thrid division")
    elif aggregate>=50 and aggregate<60:
        print("second division")
    elif aggregate>=60 and aggregate<75:
        print("first division")
    elif aggregate>=75:
        print("distinction")
else:
    print("fail")
    
        

