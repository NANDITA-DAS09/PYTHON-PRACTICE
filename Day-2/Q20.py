#20. Take a username and password from the user and check using nested if-else whether both are correct (match them with fixed values you set in the code).
cu="Nandita09"
cp="009@008"
a=input("Enter the username:")
b=input("Enter the password:")
if a==cu:
    if b==cp:
     print("Login successful!")
    else: 
     print("Incorrect Password")
else:
    print("Incorrect Username")