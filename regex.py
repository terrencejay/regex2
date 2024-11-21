import re

#the email domain we would like to exclude
invalid_email = "exclude.com"

#find emails that have small and large characters, followed by an @ symbol that is followed by our variable containig the invalid email address
valid_pattern = rf'\b[a-zA-Z0-9._%+-]+@{re.escape(invalid_email)}\b'

#string of emails to be verified
text = "Emails: user1@domain.com, user2@exclude.com, user3@domain.com"

#substituting the email that matches the validation password and returning invalid text. 
invalid_statment = re.sub(valid_pattern,"invalid email",text)

print(invalid_statment)