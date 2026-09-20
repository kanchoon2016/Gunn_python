username = input("username: ")
password = input("password: ")

if username == "admin" and password == "secret123":
   print("access granted, welcome admin")

elif username == "admin" and password != "secret123":
   print("Access denied")

else:
   print("access denied, Unknown user")