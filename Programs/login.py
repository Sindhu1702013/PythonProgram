class LoginSystem:
    def __init__(self):
        self.valid_email = os.getenv("VALID_EMAIL")
        self.valid_password = os.getenv("VALID_PASSWORD")
        self.failed_attempts = 0
        self.locked = False

    def login(self, email, password):
        if self.locked:
            return "Account is locked. Contact support."

        if email == self.valid_email and password == self.valid_password:
            self.failed_attempts = 0
            return "Login Successful ✅"

        else:
            self.failed_attempts += 1

            if self.failed_attempts >= 3:
                self.locked = True
                return "Account locked due to 3 failed attempts ❌"

            return f"Invalid credentials. Attempts left: {3 - self.failed_attempts}"

# ----- Testing the function -----

app = LoginSystem()

print(app.login("wrong@test.com", "123"))   # Test case 1
print(app.login("wrong@test.com", "123"))   # Test case 2
print(app.login("wrong@test.com", "123"))   # Test case 3 (locks account)
print(app.login("user@test.com", "Password@123"))  # Should fail because account is locked
print("TC4:", app.login("wrong@test.com", "123"))  # This will now lock
print("TC5:", app.login("user@test.com", "Password@123"))  # Locked account case
