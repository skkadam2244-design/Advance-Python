class EmailValidator:
    def __init__(self):
        self.valid_emails = []

    @staticmethod
    def validate_email(email):
        if "@" not in email:
            return False

        parts = email.split("@")

        if len(parts) != 2:
            return False

        username, domain = parts

        if username == "" or domain == "":
            return False

        if "." not in domain:
            return False

        if domain.startswith(".") or domain.endswith("."):
            return False

        return True

    def add_email(self, email):
        if EmailValidator.validate_email(email):
            self.valid_emails.append(email)
            print("Valid email:", email)
        else:
            print("Invalid email:", email)

    def show_valid_emails(self):
        print("\nValid Email Addresses:")
        for email in self.valid_emails:
            print(email)


# Input list of emails
emails = [
    "student@gmail.com",
    "abc@yahoo.com",
    "invalidemail.com",
    "test@",
    "@gmail.com",
    "hello@gmail",
    "user123@outlook.com"
]

# Create object
validator = EmailValidator()

# Validate and store emails
for email in emails:
    validator.add_email(email)

# Display valid emails
validator.show_valid_emails()