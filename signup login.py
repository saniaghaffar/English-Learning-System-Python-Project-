# db=open("database.txt","w")
choice=input("Do you want to:\n 1_Sign-up \n 2_Log-in")
if choice=="1":
    username=input("Enter username:")
    password=input("Enter password:")
    password1 = input("Confirm password :")
    db=open("database.txt","r")
    d=[]
    f=[]
    for i in db:
        temp=i.split(",")
        a = temp[0]
        b=temp[1]
        d.append(a)
        f.append(b)

    if username in d:
        print("Sign up failed. Username already exist.")
    elif password!=password1:
        print("Confirmation failed")
    elif len(password)<=6:
         print("Password too short.Must contain 8 characters.")
    elif username in d:
        print("Username exists.")
    else:
        def Id():
            t=('''ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz.></?:;"'|\!1234567890@#$%^&*()-+=_''')
            r=""
            import random
            for i in range(5):
                c=random.choice(t)
                r+=c
            return r
        w8=Id()
        print("your identity is:",w8)
        print("\r",end="")

        db=open("database.txt","a")
        db.write(username+","+password+","+w8+"\n")
        print("Signing up successfully.")
if choice=="2":
     db = open("database.txt", "r")
     username=input("Enter username :")
     password=input("Enter password :")
     Password=str(password)
     if not len(username or password)<1:
         d = []
         f = []
         for i in db:
             temp = i.split(",")
             a = temp[0]
             b = temp[1]
             d.append(a)
             f.append(b)

         print(d)
         print(f)

         if username in d:
             index=d.index(username)
             print(index)
             s=f[index]
             print(type(f[index]))
             print(type(Password))
             print((f[index]))
             print((Password))
             print(s)
             if Password==f[index]:
                 print("Login successful")
             else:
                 print("Worng Password")
     else:
         print("Login error")








