#Take two numbers from the user, swap their values using a third variable, and print both before and after swapping.
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
print("before swapping the values are A:",a,"B:",b)
temp=a
a=b
b=temp
print("After swapping A: ",a,"B: ",b)