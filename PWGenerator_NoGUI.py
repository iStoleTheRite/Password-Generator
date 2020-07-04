import random
import pyperclip as clip
from string import ascii_uppercase, ascii_lowercase, digits, punctuation

def print_and_copy_pw(pwLen=8):
    options = ascii_uppercase + ascii_lowercase + digits + punctuation
    length = pwLen
    generated = "".join(random.choice(options) for _ in range(length))
    clip.copy(generated)
    return (f"{generated} is your generated password. It has been copied to your clipboard.\n")

print("You may quit anytime by entering 0")
while True:
    pwLen = int(input("How long would you like your password to be? (Must be at least 6)\n> "))
    if pwLen == 0:
        break
    elif pwLen<6:
        print("Needs to be greater than 6 characters.")
        continue
    else:
        print(print_and_copy_pw(pwLen))
