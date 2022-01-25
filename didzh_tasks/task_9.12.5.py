def is_password_hard(password: str) -> bool:
    """Returns True, if `password` hard, otherwise False."""
    if len(password) > 12 and any(map(str.isdigit, password)) and any(map(str.isupper, password)) and any(map(str.islower, password)): 
        return True
    return False


#Другой вариант
# def is_password_hard(password: str) -> bool:
#     """Returns True, if `password` hard, otherwise False."""
#     return all([len(password) > 12, not password.isalpha(), 
#     not password.isupper(), not password.islower(), not password.isdigit()])

#Через re
# import re

# def is_password_hard(password: str) -> bool:
#     expr = re.compile("(?=.*\d)(?=.*[A-Z])(?=.*[a-z]).{13,}")
#     return True if expr.search(password) else False

