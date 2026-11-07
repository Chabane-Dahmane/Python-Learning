password = input("Enter your password: ")

if len(password) >= 8 :
    print("Password length: Valid")

else :
    print("Password length: inValid")

if any(i.isdigit() for i in password ) :
    print("Contains number: Yes")
else :
    print("Contains number: no")

if any(i.isupper() for i in password ) :
    print("Contains uppercase:Yes")
else :
    print("Contains uppercase:no")

if any(i.islower() for i in password ) :
    print("Contains lowercase:Yes")
else :
    print("Contains lowercase:  no")

a = len(password) >= 8
b = any(i.isdigit() for i in password)
c = any(i.isupper() for i in password)
d = any(i.islower() for i in password)

if a and b and c and d :
    print("Strong passworld")
else :
     print("weak passworld")