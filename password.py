import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for better security.")
        return None

    # Define character sets
    all_chars = string.ascii_letters + string.digits + string.punctuation

    # Randomly generate password
    password = ''.join(random.choice(all_chars) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a numeric value.")

# Run the program
main()
