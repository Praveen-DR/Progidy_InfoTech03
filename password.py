import re

def check_password_strength(password):
    # Initialize criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = re.search(r'[A-Z]', password) is not None
    lowercase_criteria = re.search(r'[a-z]', password) is not None
    number_criteria = re.search(r'\d', password) is not None
    special_char_criteria = re.search(r'\W', password) is not None

    # Calculate score
    score = sum([length_criteria, uppercase_criteria, lowercase_criteria, number_criteria, special_char_criteria])

    # Determine strength
    strength_levels = {
        5: "Very Strong",
        4: "Strong",
        3: "Medium",
        2: "Weak",
        0: "Very Weak",
        1: "Very Weak"
    }

    return strength_levels[score]

# Example usage
password = input("Enter a password to check its strength: ")
strength = check_password_strength(password)
print(f"Password Strength: {strength}")
