import random
import string

def generate_password(length=12):
    """
    Generate a random password that meets the following requirements:
    - At least 8 characters long
    - Contains at least one uppercase letter
    - Contains at least one lowercase letter
    - Contains at least one number
    - Contains at least one special character
    
    Args:
        length (int): Length of the password (default: 12)
    
    Returns:
        str: Generated password
    """
    # Ensure minimum length of 8
    length = max(8, length)
    
    # Define character sets
    uppercase_letters = string.ascii_uppercase
    lowercase_letters = string.ascii_lowercase
    digits = string.digits
    special_chars = "!@#$%^&*()_+-=[]{}|;:,.<>?"
    
    # Ensure at least one character from each required set
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(digits),
        random.choice(special_chars)
    ]
    
    # Fill the rest of the password with random characters from all sets
    all_chars = uppercase_letters + lowercase_letters + digits + special_chars
    password.extend(random.choice(all_chars) for _ in range(length - 4))
    
    # Shuffle the password to make it more random
    random.shuffle(password)
    
    return ''.join(password)

if __name__ == "__main__":
    # Example usage
    password = generate_password()
    print(f"Generated password: {password}") 