import re

def valid_email(email):
    pattern=r"^[\w\d\._]+@[\w\.-]+\.(com|org|in)"
    return re.fullmatch(pattern,email,re.IGNORECASE) is not None

email="himasai.199758@gmail.com"
email1="20H71A0519@mictech.ac.in"
print(valid_email(email))
print(valid_email(email1))