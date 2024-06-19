import random
import string

def generate_password(length):
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    
    password = ''.join(random.choices(all_characters, k=length))
    
    return password

def main():
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            if length <= 0:
                print("Please enter a positive integer greater than zero.")
            else:
                break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
    
    password = generate_password(length)
    
    print("Generated password:", password)

if __name__ == "__main__":
    main()



