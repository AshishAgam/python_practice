# random password generator
# A-Z
# a-z
# 0-9
# punctuators !@#$%^&*()_+<>?:"';,./\][{}|~`]

import random
import string

pass_len = 12

char_values = string.ascii_uppercase + string.ascii_lowercase + string.punctuation + string.digits

password = ""
for i in range(pass_len):
    password += random.choice(char_values)
    
print("Your random password is:", password)

# one line code for random password generator
# password = ''.join(random.choice(char_values) for i in range(pass_len))
# print(password)