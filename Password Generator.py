import random
characters=[chr(x) for x in range(33,127)]
def password_generator(n):
    if n<6:
        print("The password length must be greater than 6.")
    else:
        r = random.choices(characters,k=n)
        password = "".join(r)
        print("The password is: ",password)
pass_length = int(input("Enter the length of password: "))
password_generator(pass_length)