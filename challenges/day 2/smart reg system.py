student_id = input ("enter your student_id")
email = input ("enter your email_id ")
password = input("enter your password ")
referral = input ("enter your referral code ")

status = "APPROVED"

if password [7:8] == "":
    status = "REJECTED"
elif not ('A' <= password[0] <='Z'):
    status = "REJECTED"
elif not (
    '0' in password or '1' in password or '2' in password or 
    '3' in password or '4' in password or '5' in password or
    '6' in password or '7' in password or '8' in password or 
    '9' in password
):
    status = "REJECTED"

elif student_id[0:3] != "CSE":
    status ="REJECTED"
elif student_id[3] != "-":
    status = "REJECTED"
elif not (
           '0' <= student_id[4] <= '9' and
           '0' <= student_id[5] <= '9' and
           '0' <= student_id [6] <= '9'
):
    status = "REJECTED"

elif "@" not in email or "." not in email :
    status = "REJECTED"
elif email[0] == "@" or email [-1] == "@":
    status = "REJECTED"
elif email [-4:]!= ".edu":
    status = "REJECTED"

elif referral[0:3] != "REF":
    status = "REJECTED"
elif not ('0'<= referral [3] <= '9' and '0' <= referral[4] <= '9'):
    status = "REJECTED"
elif referral[-1] != "@":
    status = "REJECTED"

print(status )