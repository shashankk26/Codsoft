import random
import string


def get_password_length():
    while True:
        try:
            length = int(input("Enter the  password  "))
            if length < 5:
                print("Password length should be at least 5 characters for security.")
            else:
                return length
        except ValueError:
            print("Please enter a valid number.")


def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choices(all_characters, k=length))
    
    return password


def display_password(password):
    print(f"Your generated password is: {password}")

def main():
    
    length = get_password_length()
    
    
    password = generate_password(length)
    
    
    display_password(password)


if __name__ == "__main__":
    main()