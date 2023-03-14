def encrypt(text, shift):
    """Encrypts a string using the Caesar Cipher algorithm."""
    result = ""
    # Iterate through each character in the input text
    for char in text:
        # If the character is a letter, shift it by the specified amount
        if char.isalpha():
            shifted = ord(char) + shift
            # Handle wraparound for letters at the end of the alphabet
            if char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            else:
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            # Append the shifted character to the result string
            result += chr(shifted)
        else:
            # If the character is not a letter, leave it as-is
            result += char
    return result

def decrypt(text, shift):
    """Decrypts a string that was encrypted using the Caesar Cipher algorithm."""
    # To decrypt, simply shift the text in the opposite direction
    # by using a negative shift value
    return encrypt(text, -shift)

print("\they There Welcome What do you want to do:")
choice = input("For Encrytion Press E and For Decryption press D\n")
if choice.lower() == 'e':
    text = str(input("Enter your Sentence to Encrypt:"))
    shift = int(input("Enter the Shift Value:"))
    encrypted = encrypt(text, shift)
    print(encrypted)  # "Khoor, zruog!"
    
elif choice.lower() == 'd':
    text1 = str(input("Enter your Sentence to Decrypt:"))
    shift = int(input("Enter the Shift value:"))
    decrypted = decrypt(text1, shift)
    print(decrypted)  # "Hello, world!"




