"""
#practical4 b
l=[10,20,30,40,50,60]
l1=[]
for x,y in enumerate(l):
    if(x%2!=0):
        l1.append(y)

l=l1
print(l)
# 4c
l=[1,2,3,4,5]
l1=l
print("origianal list:" ,l)
print("copy list:",l1)


#practical 5a
import operator

d={"ritek":800,"abhishek":700,"pillai":100}

print("Original dictionary:")
print(d)
print("Acending Dictorinry by key")
sort_a=sorted(d.keys())
print(sort_a)
print("Decending Dictorinay by key")
sort_d=sorted(d.keys(),reverse=True)
print(sort_d)
print("Acending Dictorinay by values")
sort_av=sorted(d.items(),key=operator.itemgetter(1))
print(sort_av)
print("decending Dictorinary by values")
sort_dv=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print(sort_dv)


#practical 5b
dic1={1:100,2:200,3:300}
dic2={4:400,5:500,6:600}
dic3={7:700,8:800,9:900}
dic4={}
for i in dic1,dic2,dic3:
    dic4.update(i)
print(dic4)
"""
#pricatical 5c
dic1={1:200,2:300,3:500}
print(sum(dic1.values()))
"""
