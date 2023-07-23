# Copy your code from part A or Part C here then change it as required
# Copy your code from part A here then change it as required
import secrets
import string
# add more imports and general constant definitions here if you wish

# add any constants here

def generate_pwd(length):

    if length <8:
        print("Invalid length, generating password of minimum length")
        return generate_pwd(8)
    elif length >20:
        print("invalid length, generating password of maximum length")
        return generate_pwd(20)

    lowercase_char = string.ascii_lowercase
    uppercase_char = string.ascii_uppercase
    digits = string.digits
    special_char = string.punctuation
    """write a suitable doc string here"""
    # your code here
    p1 = secrets.choice(lowercase_char)
    p2 = secrets.choice(uppercase_char)
    p3 = secrets.choice(digits)
    p4 = secrets.choice(special_char)

    all_characters = lowercase_char + uppercase_char + digits + special_char

    while True:
        # Generate a random password of the required length
        password = ''.join(secrets.choice(all_characters) for i in range(length))
        # Check if the password meets all requirements
        if (any(c.islower() for c in password) and
            any(c.isupper() for c in password) and
            any(c.isdigit() for c in password) and
            any(not c.isalpha() or not c.isdigit() or not c.isspace() for c in password)):
            return password
