import random
import string
def generate_password(length, complexity):
    if complexity == '1':
        characters = string.ascii_letters
    elif complexity == '2':
        characters = string.ascii_letters + string.digits
    elif complexity == '3':
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        return "Invalid choice. enter 1, 2, or 3."

    password = ''.join(random.choice(characters) for _ in range(length))
    return password


def password_generator():
    try:
        length = int(input("Enter the length of the password: "))
        if length < 1:
            print("Password length should be at least 1.")
            return

        print("Select from below :")
        print("1. Letters only")
        print("2. Letters and digits")
        print("3. Letters, digits, and special characters")

        complexity = input("Enter choice (1/2/3): ")

        operations = {
            '1': generate_password,
            '2': generate_password,
            '3': generate_password
        }

        if complexity not in operations:
            print("Invalid choice. enter 1, 2, or 3.")
            return

        password = operations[complexity](length, complexity)
        print(f"Generated Password: {password}")

    except ValueError:
        print("Invalid input. enter valid number for the length.")


if __name__ == "__main__":
    password_generator()
