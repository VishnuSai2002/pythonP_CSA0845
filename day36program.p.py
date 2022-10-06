def reverse(n):
    num = ""
    for i in n:
        num = i + num
    return num
  
n=input("enter the value")  
print("The reversed num(using loops) is : ", end="")
print(reverse(n))
