#password generator

import random
import string

def password_gen(length):
    character= string.ascii_letters + string.punctuation + string.hexdigits + string.digits
    password= ''.join(random.choice(character) for _ in range(length))
    return password

length = int(input("enter the length of password:"))
print("password:",password_gen(length))