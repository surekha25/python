# Python is case sensitive i.e. 'a' and 'A' are different

#environment = "PROD"
environment = input("Enter your environment: ")
change_ticket = False

environment = environment.casefold() # using this for non-case sensitive

if environment == "prod":
    change_ticket = True
    print("Please provide a change ticket")
elif environment == "Staging":
    print("welcome to staging environment")
else:
    print("Please login using your credentials")