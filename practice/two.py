"""
practical 2a
def vowel(char):
    if(char=='a' or char =='e' or char == 'i' or char=='o' or char == 'u'):
        return True
    elif(char=='A' or char =="E" or char =="I" or char == "O" or char =="U"):
        return True
    else:
        return False

char=input('Enter a charecter')
v=vowel(char)
if(v):
    print("it is vowel")
else:
    print("it is not a vowel")

2b method 1
def strlen(string):
    return len(string)

string=input("Enter the string")
l=strlen(string)
print(l)

method 2

string=input("Enter the string")
count=0
for i in string:
    count=count+1
print(count)
2b
l=[]
size=int(input("enter the length of the list you want to enter"))
print("Enter the elements")
for i in range(size):
    data=int(input())
    l.append(data)
print("the emelens of list is :")
print(l)
lenl=len(l)
print("the length of given list is :")
print(lenl)

2c

def histogram(string):
    for i in range(len(string)):
        print(string[i]*'*')
l=[]
size=int(input("Enter the lenght of the list"))
print("enter the elements of the list")
for i in  range(size):
    data=int(input())
    l.append(data)
histogram(l)

practical 3a
def pangram(string):
    a="abcdefghijklmnopqrstuvwxyz"
    a_count=0
    if(len(string)==0):
        print("string is emtyp")
        
    string=string.lower()
    for i in range(len(a)):
        if(a[i] in string):
            a_count+=1
        else:
            return False
    if(a_count==26):
        return True
    else:
        return False

string=input("Enter the string")
pang=pangram(string)
if(pang):
    print("it is a pangram")
else:
    print("it is not a pangram")

#practical 3b
l=[1,2,3,5,8,13,21,34,55,89]
for i in range(len(l)):
    if(l[i]<5):
        print(l[i])
"""
def copy(l1,l2):
    for i in range(len(l1)):
       for y in range(len(l2)):
            if(l1[i]==l2[y]):
                return True
            else:
                return False



l1=[1,2,3,4]
l2=[1,5,6,7]
c=copy(l1,l2)
if(c):
    print("same")
else:
    print("not")
