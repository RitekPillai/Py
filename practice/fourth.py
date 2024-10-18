"""
#pracitcal 6a
f=open("text.txt","r")
data=f.read()
print(data)
f.close()

#6b
f=open("text.txt","r")
data=f.read()
print(data)

f=open("text.txt","a")
f.write(" ,World")
f.close()

f=open("text.txt","r")
print(f.read())
"""
#6c
# Write a Python program to read last n lines of a file. 
f=open("text.txt","r")

k=f.readline()
print(k[-1:])

f.close()