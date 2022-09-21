size=int(input("Enter the size of list:"))
l1=[]
for i in range(0,size):
    l=int(input())
    l1.append(l)
print()
list=l1[::-1]
for i in list:
    print(i,end=" ")
print()
s=l1[3::3]
for i in s:
    sum=i+3
    print(sum,end=" ")
print()
s1=l1[5::5]
for i in s1:
    sub=i-7
    print(sub)
s2=l1[3:8]
add=0
for i in s2:
    add+=i
print(add)


