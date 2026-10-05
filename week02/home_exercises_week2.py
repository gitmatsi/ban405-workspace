# Exercise 1

import random

print(random.randint(1, 6))

# This will return B
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")

# This will return B and C
score = 85

if score >= 90:
    print("A")
if score >= 80:
    print("B")
if score >= 70:
    print("C")

# This returns False and True
print(0.1 + 0.2 == 0.3)
print(round(0.1 + 0.2, 2) == 0.3)

# Returns True and False
is_member = False
age = 70

print(is_member and age >= 18 or age >= 67)
print(is_member and (age >= 18 or age >= 67))

# True and True - Correction "B" and True
answer = "B"

print(answer == "A" or "B")
print(answer == "A" or answer == "B")

# Returns 3.14, None and None? - wrong, returns false, false, false. Because only INT numbers work with isdigit
print("3.2".isdigit())
print("-7".isdigit()) 
print("".isdigit())

# Returns false as both = false

code = ""

print(len(code) > 0 and code[0] == "N")

# True, false, true, true, false, true, false, false

print(bool("0"))
print(bool([]))
print(bool({"a": 0}))
print(bool(" "))
print(bool(0))
print(bool([[]]))
print(bool(""))
print(bool({}))

# 1

grade = "A"
if grade == "A":
    print("Helt greit")
else:
    print("Forferdelig fyr")

# 2 - meant to accept any score from 0 to 100
score = 100
if 0 <= score <= 100:
    print("Valid score")
else:
    print("Invalid score")

# 3 - meant to check that a name starts with a capital letter
name = "roger"
if name[0].isupper() and len(name) > 0:
    print("Starts with a capital")
else:
    print("Doesn't start with capital")

# Exercise 2
password = "CopyCat123"

long_enough = len(password) >= 8
has_upper = any(upper.isupper() for upper in password)
digit_start = not password[0].isdigit()
contains_digit = any(character.isdigit() for character in password)

print(contains_digit)

print(digit_start)

print(long_enough)

print(has_upper)

strong = long_enough and has_upper and digit_start and contains_digit
print(strong)

if strong == True:
    print("Strong password")
elif long_enough == False:
    print("Too short")
elif long_enough == True and strong == False:
    print("Long enough, but breaks a condition")
else:
    print("Not sufficient")

# Exercise 3


