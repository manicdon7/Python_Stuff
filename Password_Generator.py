import random
import string

def generate_password(length, uppercase=True, lowercase=True, numbers=True, special_chars=True):
    """
    Generates a password with the specified length and character types.
    """
    chars = ''
    if uppercase:
        chars += string.ascii_uppercase
    if lowercase:
        chars += string.ascii_lowercase
    if numbers:
        chars += string.digits
    if special_chars:
        chars += string.punctuation
    
    password = ''.join(random.choice(chars) for _ in range(length))
    return password

# Example usage
password_length = int(input("Enter password length: "))
use_uppercase = input("Use uppercase letters? (y/n): ").lower() == 'y'
use_lowercase = input("Use lowercase letters? (y/n): ").lower() == 'y'
use_numbers = input("Use numbers? (y/n): ").lower() == 'y'
use_special_chars = input("Use special characters? (y/n): ").lower() == 'y'

password = generate_password(password_length, use_uppercase, use_lowercase, use_numbers, use_special_chars)
print("Generated password:", password)
