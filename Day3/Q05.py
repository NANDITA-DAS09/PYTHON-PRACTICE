#Take two lists from the user (with the same items) and check if they are equal using ==.
b=[]
j=int(input("enter the len of  list:"))
for i in range(j):
    a=(input("enter the elements of b list:"))
    b.append(a)
x=[]
for i in range(j):
    a=(input("enter the elements of x list:"))
    x.append(a)
num=0
if b==x:
    num=1
if num==0:
    print (False)
if num!=0:
    print(True)
    

