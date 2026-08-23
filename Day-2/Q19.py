#Take the user's age and print whether they are a 'Child', 'Teenager', or 'Adult' using if-elif-else (below 13 = Child, 13-19 = Teenager, above 19 = Adult).
age=int(input("Enter your age:"))
if age<13:
    print("You are a Child.")
elif age>=13 and age<=19:
    print("You are a Teenager.")
else:
    print("You are an Adult.")