#Take 5 marks from the user, store them in a list, and print the highest mark using max() and lowest mark using min().
b=[]
for i in range(5):
    a=int(input("Enter the marks: "))
    b.append(a)
print(max(b))
print(min(b))

