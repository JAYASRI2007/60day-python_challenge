name = input("enter your name:");
email = input("enter your email id: ");
mobile = input("enter your mobile number :")
age = int(input("enter your age :"))

status = "VALID"
if name == " "or name[-1]== " ":
    status = "INVALID"
elif name.count(" ") < 1:
    status = "INVALID"

if "@" not in email or "." not in email:
    status = "INVALID"
elif email[0] == "@":
    status = "INVALID"

if len(mobile) != 10:
    status = "INVALID"
elif mobile.isdigit() == False:
    status = "INVALID"
elif mobile[0] == "0":
    status = "INVALID"

if age < 18 or age > 60:
    status = "INVALID"

if status == "VALID":
    print("User Profile is VALID")
else:
    print("User Profile is INVALID")


