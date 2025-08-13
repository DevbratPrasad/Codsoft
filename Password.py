import random
import string

def welcome():
    print("\nWelcome to the Secure Password Generator!")
    print("This tool helps you create strong and random passwords.\n")

def get_password_length():
    while True:
        try:
            length = int(input("Enter the desired password length (minimum 4): "))
            if length >= 4:
                return length
            else:
                print("Password length should be at least 4. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def generate_password(length):
    # Define all possible characters
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password contains at least one of each character type
    base = [
        random.choice(string.ascii_lowercase),
        random.choice(string.ascii_uppercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]

    if length > 4:
        base += random.choices(characters, k=length - 4)

    random.shuffle(base)
    return ''.join(base)

def main():
    welcome()
    length = get_password_length()
    password = generate_password(length)
    print(f"\nYour secure password is: {password}\n")

if __name__ == "__main__":
    main()
