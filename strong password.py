def is_strong_password(password):

    if len(password) < 8:
        return False

    has_uppercase = False
    has_lowercase = False
    has_digit = False
    has_special = False

    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase = True
        elif char.isdigit():
            has_digit = True
        else:
            has_special = True

    if not (has_uppercase and has_lowercase and has_digit and has_special):
        return False

    return True

password = input("Enter your password: ")
if is_strong_password(password):
    print("Strong password!")
else:
    print("Weak password! Your password must be at least 8 characters long and contain a mix of uppercase and lowercase letters, digits, and special characters.")
