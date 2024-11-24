import random
import string

def check_password_strength(password):
    conditions_met = 0
    length = len(password) >= 12

    if any(char.isdigit() for char in password):
        conditions_met += 1
    if any(char.islower() for char in password):
        conditions_met += 1
    if any(char.isupper() for char in password):
        conditions_met += 1
    if any(char in string.punctuation for char in password):
        conditions_met += 1

    if length and conditions_met == 4:
        return "Strong", "Your password meets all the criteria."
    elif conditions_met == 3:
        return "Moderate", "Your password meets most of the criteria but could be improved."
    else:
        return "Weak", "Your password is weak and should be strengthened by meeting more criteria."

def suggest_strong_password():
    password = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=8)
    random.shuffle(password)
    return ''.join(password)

password = input("Enter your password: ")
strength, message = check_password_strength(password)
print(f"Password Strength: {strength}")
print(message)

if strength in ["Moderate", "Weak"]:
    print("Here's a suggestion for a strong password:")
    suggested_password = suggest_strong_password()
    print(suggested_password)
