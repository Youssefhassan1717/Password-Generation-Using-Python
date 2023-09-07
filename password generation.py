#Author: Youssef Hassan
#Date: 6/9/2023

import random
import string

def generate_password(length=12):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = '!@#$%^&*()_+[]{}|;:,.<>?'

    all_characters = lowercase_letters + uppercase_letters + digits + special_characters

    if length < 12:
        length = 12
    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

if __name__ == "__main__":
    password_length = int(input("Enter the desired password length: "))
    generated_password = generate_password(password_length)
    print("Generated Password:", generated_password)
