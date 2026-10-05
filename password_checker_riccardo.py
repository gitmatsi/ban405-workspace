# Assignment 1 — Password Strength Checker

# Characters that count as special characters
special_characters = "!@#$%&*?"

# Passwords that are too common to be safe (all in lowercase)
common_passwords = ["password", "password1", "password123", "password123!", "passord",
                    "passord123", "123456", "12345678", "qwerty", "qwerty123", "iloveyou", "admin"]

# The password your program should check. To try a different test password,
# move the "#" from that line to the active one.
#password = "Sunshine26"
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
num_checks = 0

while True:
    password = input('Choose a password (or press Enter to quit):  ')
    if password == '':
        print(f'No password chosen. Passwords checked: {num_checks}')
        break

    num_checks += 1

    uppercase_letters = 0
    lowercase_letters = 0
    digits_num = 0
    special_in_password = 0
    for letter in password:
        if letter.isupper():
            uppercase_letters += 1
        if letter.islower():
            lowercase_letters += 1
        if letter.isdigit():
            digits_num += 1
        if letter in special_characters:
            special_in_password += 1
    print(f'''
Lenght: {len(password)}
Uppercase letters: {uppercase_letters}
Lowercase letters: {lowercase_letters}
Digits: {digits_num}
Special characters: {special_in_password}''')
    print('')

    # RULES
    eight_characters = len(password) >= 8 

    if eight_characters:
        print('[OK]   At least 8 characters')
    else: 
        print('[FAIL] At least 8 characters')
    if uppercase_letters > 0:
        print('[OK]   At least one uppercase letter')
    else:
        print('[FAIL] At least one uppercase letter')
    if lowercase_letters > 0:
        print('[OK]   At least one lowercase letter')
    else:
        print('[FAIL] At least one lowercase letter')
    if digits_num > 0:
        print('[OK]   At least one digit')
    else:
        print('[FAIL] At least one digit')
    if special_in_password > 0: 
        print('[OK]   At least one special character')
    else:
        print('[FAIL] At least one special character')
    print('')
    

    # STEP 3
    score = 0

    if 8 <= len(password) <= 11:
        score += 1
    elif len(password) > 11:
        score += 2
    if uppercase_letters > 0:
        score += 1
    if lowercase_letters > 0:
        score += 1
    if digits_num > 0:
        score += 1
    if special_in_password > 0:
        score += 1

    rating = ''
    if password.lower() in common_passwords:
        rating = 'Very weak'
        print(f'Score: 0 / 6\nRating: {rating}')
    elif len(password) < 8 or score <= 2:
        rating = 'Weak'
        print(f'Score: {score} / 6\nRating: {rating}')
    elif 2 < score < 5:
        rating = 'Medium'
        print(f'Score: {score} / 6\nRating: {rating}')
    else:
        rating = 'Strong'
        print(f'Score: {score} / 6\nRating: {rating}')

        print(f'Password accepted! Passwords checked: {num_checks}')
        break



# TRYING WITH THE FUNCTIONS

def is_common(password):
    '''Return if the password is a common password'''
    return password.lower() in common_passwords

def count_uppercase(password):
    '''Return how many uppercase letter the password has'''
    uppercase_letters = 0
    for letter in password:
        if letter.isupper():
            uppercase_letters += 1
    return uppercase_letters

def count_lowercase(password):
    '''Return how many lowercase letter the password has'''
    lowercase_letters = 0
    for letter in password:
        if letter.islower():
            lowercase_letters += 1
    return lowercase_letters

def count_digits(password):
    '''Return how many digits the password has'''
    digits_num = 0
    for letter in password:
        if letter.isdigit():
            digits_num += 1
    return digits_num

def count_special(password):
    '''Return how many special characters the password has'''
    special_in_password = 0
    for letter in password:
        if letter in special_characters:
            special_in_password += 1
    return special_in_password
        

def display_analysis_password(password):
    print(f'''
Lenght: {len(password)}
Uppercase letters: {count_special(password)}
Lowercase letters: {count_lowercase(password)}
Digits: {count_digits(password)}
Special characters: {count_special(password)}''')


def display_rules(password):
    eight_characters = len(password) >= 8 

    if eight_characters:
        print('[OK]   At least 8 characters')
    else: 
        print('[FAIL] At least 8 characters')
    if count_uppercase(password) > 0:
        print('[OK]   At least one uppercase letter')
    else:
        print('[FAIL] At least one uppercase letter')
    if count_lowercase(password) > 0:
        print('[OK]   At least one lowercase letter')
    else:
        print('[FAIL] At least one lowercase letter')
    if count_digits(password) > 0:
        print('[OK]   At least one digit')
    else:
        print('[FAIL] At least one digit')
    if count_special(password) > 0: 
        print('[OK]   At least one special character')
    else:
        print('[FAIL] At least one special character')



def score_password(password):
    score = 0

    if 8 <= len(password) <= 11:
        score += 1
    elif len(password) > 11:
        score += 2
    if count_uppercase(password) > 0:
        score += 1
    if count_lowercase(password) > 0:
        score += 1
    if count_digits(password) > 0:
        score += 1
    if count_special(password) > 0:
        score += 1
    return score

def rating_password(password):
    rating = ''
    if password.lower() in common_passwords:
        rating = 'Very weak'
    elif len(password) < 8 or score_password(password) <= 2:
        rating = 'Weak'
    elif 2 < score_password(password) < 5:
        rating = 'Medium'
    else:
        rating = 'Strong'
    return rating


def display_rating(password):
    if rating_password(password) == 'Very weak':
        print('Score: 076\nRating: Very weak')
    else:
        print(f'Score: {score_password(password)}/6\nRating: {rating_password(password)}')


def main():
    num_checks = 0
    while True:
        password = input('Choose a password (or press Enter to exit):  ')
        if password == '':
            print(f'No password chosen. Passwords checked : {num_checks}')
            break
        elif rating_password(password) == 'Strong':
            num_checks += 1
            display_analysis_password(password)
            print('')
            display_rules(password)
            print('')
            display_rating(password)
            print(f'Password accepted! Passwords checked: {num_checks}')
            break
        else:
            num_checks += 1
            display_analysis_password(password)
            print('')
            display_rules(password)
            print('')
            display_rating(password)
main()