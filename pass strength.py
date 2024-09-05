import re

def password_strength(password):
    
    if len(password) < 8:
        print("Password should be at least 8 characters long.")

    
    if not re.search(r"\d", password):
        print("Password should include at least one number.")

    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        print("Password should include at least one special character.")

    
    if not (re.search(r"[A-Z]", password) and re.search(r"[a-z]", password)):
        print("Password should include both uppercase and lowercase letters.")

    
    if (len(password) >= 8 and
        re.search(r"\d", password) and
        re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) and
        re.search(r"[A-Z]", password) and
        re.search(r"[a-z]", password)):
        print("Strong password 😁👍.")
    elif len(password) >= 8 and len([c for c in [re.search(r"\d", password),
                                                re.search(r"[!@#$%^&*(),.?\":{}|<>]", password),
                                                re.search(r"[A-Z]", password),
                                                re.search(r"[a-z]", password)] if c]) == 3:
        print("Moderate password 😑. Consider adding more variety (e.g., special characters, numbers).")
    else:
        print("Weak password 😢. Improve by following the suggestions.")

def main():
    password = input("Enter your password: ")
    password_strength(password)

if __name__ == "__main__":
    main()
