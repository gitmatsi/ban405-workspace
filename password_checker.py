# Assignment 1 — Password Strength Checker

# Characters that count as special characters
from multiprocessing.resource_sharer import stop
import sys
special_characters = "!@#$%&*?"

# Passwords that are too common to be safe (all in lowercase)
common_passwords = ["password", "password1", "password123", "password123!", "passord",
                    "passord123", "123456", "12345678", "qwerty", "qwerty123", "iloveyou", "admin"]

# The password your program should check. To try a different test password,
# move the "#" from that line to the active one.
password = input("Choose a password (or press Enter to quit): ")
if password == "":
    print("No password chosen. Passwords checked: 1")
    sys.exit()

#password = "hello"
#password = "Ban405!"
#password = "sunshine"
#password = "abcdefghij1"
#password = "abcdefghijk1"
#password = "Ban405rock!"
#password = "Blåbær!2"
#password = "correct horse battery"
#password = "Password123!"
#password = "PASSWORD123!"

# Write your code below

digit_count = 0
upper_count = 0
lower_count = 0
special_count = 0

for char in password:
    if char.isdigit():
        digit_count += 1

for char in password:
    if char.isupper():
        upper_count += 1

for char in password:
    if char.islower():
        lower_count += 1

for char in password:
    if char in special_characters:
        special_count += 1

print(f"Digits: {digit_count}")
print(f"Uppercase letters: {upper_count}")
print(f"Lowercase letters: {lower_count}")
print(f"Special characters: {special_count}")
print(f"Length: {len(password)}")

if len(password) >= 8:
    len_status = "OK"
else:
    len_status = "FAIL"

if upper_count >= 1:
    upper_status = "OK"
else:
    upper_status = "FAIL"

if lower_count >= 1:
    lower_status = "OK"
else:
    lower_status = "FAIL"

if special_count >= 1:
    special_status = "OK"
else:
    special_status = "FAIL"

if digit_count >= 1:
    digit_status = "OK"
else:
    digit_status = "FAIL"

print(f"[{len_status}] At least 8 characters")
print(f"[{upper_status}] At one uppercase letter")
print(f"[{lower_status}] At least one lowercase letter")
print(f"[{digit_status}] At least one digit")
print(f"[{special_status}] At least one special character")

if len(password) < 8:
    len_points = 0
elif 11 >= len(password) >= 8:
    len_points = 1
elif len(password) >= 12:
    len_points = 2

type_points = 0

if digit_count > 0:
    type_points += 1

if special_count > 0:
    type_points += 1

if upper_count > 0:
    type_points += 1

if lower_count > 0:
    type_points += 1

total_score = type_points + len_points

if password.lower() in common_passwords:
    rating = "very weak"
elif len(password) < 8 or total_score <= 2:
    rating = "weak"
elif 3 <= total_score <= 4:
    rating = "medium"
elif 5 <= total_score <= 6:
    rating = "strong"

print(f"Score: {total_score} / 6")
print(f"Rating: {rating}")

