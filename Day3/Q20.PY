# Take a list of names from the user, check using if-else whether a name entered by the user exists in the list (using the 'in' keyword).
b=[]
a=int(input("enter the len of the list: "))

for i in range(a):
    d=input("Enter the names: ")
    b.append(d)
c=input("Enter the name you wanna find out:")
if c in b:
    print(c,"is present")
else:
    print("not present")
    