# password generator

import random
import string

length = int (input("enter password length :"))

character = string.ascii_letters + string.digits + string.punctuation
password = ""

for i in range(length):
    password = password + random.choice(character)


print("generated password :" , password)