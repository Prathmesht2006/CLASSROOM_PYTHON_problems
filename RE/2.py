import re

# Mobile Number Validation (10 digits, starts with 6-9)
mobile = input("Enter mobile number: ")
if re.fullmatch(r"[6-9]\d{9}", mobile):
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number")

# Email Validation
email = input("Enter email: ")
if re.fullmatch(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", email):
    print("Valid Email")
else:
    print("Invalid Email")

# Date of Birth Validation (DD-MM-YYYY)
dob = input("Enter DOB (DD-MM-YYYY): ")
if re.fullmatch(r"(0[1-9]|[12][0-9]|3[01])-(0[1-9]|1[0-2])-\d{4}", dob):
    print("Valid DOB")
else:
    print("Invalid DOB")

# Aadhaar Number Validation (12 digits)
aadhaar = input("Enter Aadhaar number: ")
if re.fullmatch(r"\d{12}", aadhaar):
    print("Valid Aadhaar Number")
else:
    print("Invalid Aadhaar Number")
