import re
# digit_pattern =r'\+?[\d-]+'
with open("text_emails.txt", "r") as file:
    emails_data = file.read()

# email_pattern = r"[\w.%+-]+@[\w.%+-]+\.[A-Za-z]+"
pattern = r"\w*.\w*@.*.com"

for email in re.findall(pattern, emails_data):
    print(email)