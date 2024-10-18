"""
practical 1a
name=input("Enter your name")
age=int(input("Enter your age"))
cy=int(input("Enter the current year"))
n=100-age
f=cy+n
print("you will be 100 year old in",f,"year")

1b
num=int(input("Enter the number:"))
if(num%2==0):
    print("the given number is even")
else:
    print("the given number is odd")

1c
num=int(input("Enter the number till to generate fibonacci series"))
n=0
n1=1
fibo=0

if(num<0):
    print("please enter the vaild number")
elif(num==1 or num==0):
    if(num==1):
        print("the given sequence is ",n,n1)
    else:
        print("the given sequence is 0")
else:
    print(n)
    print(n1)
    count=0
    while(count<num-2):
        fibo=n+n1
        print(fibo)
        n=n1
        n1=fibo
        count+= 1
1d
def reverse(num):
    rem=0
    rev=0
    while(num!=0):
        rem=num%10
        rev=(rev*10)+rem
        num=num//10
    return rev
n=int(input("Enter the number to reverse"))
r=reverse(n)
print("Reverse of ",n," is ",r)
    
1e
def armstrong(num):
    og=num
    rem=0
    rev=0
    sum1=0
    while(num!=0):
        rem=num%10
     
        sum1=rem*rem*rem+sum1
        num=num//10
    
    if(og==sum1):
        return 1
    else:
        return -1

n=int(input("Enter the number to check wheater it is armstrong or not"))
arm=armstrong(n)
if(arm==1):
    print("it is a armstrong")
else:
    print("it is not a armstrong")


def factorial(num):
    if(num<0):
        return "factorial is for -ve"
    elif num==0:
        return 1
        
    else:
        
        return num*factorial(num-1)

n=int(input("Enter the number "))
fact=factorial(n)
print("the factorial of the given number is",fact)

 normal method
def factorial(num):
    fact=1

    for i in range(num,0,-1):
        fact=fact*i
    return fact
n=int(input("Enter the number "))
fact=factorial(n)
print("the factorial of the given number is",fact)
"""
