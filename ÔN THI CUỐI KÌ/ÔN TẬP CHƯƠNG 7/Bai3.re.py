import re
def check_password(password):
    if len(password) < 6 or len(password) > 17:
        return False
    if not re.search('[a-z]',password):
        return False
    if not re.search('[A-Z]',password):
        return False
    if not re.search('[0-9]',password):
        return False
    return True
password = input()
print(check_password(password))