
"""
Write a password generator program of 8 characters that contains at least one uppercase, one lower case, one digit and
one special symbol? (Every new password should be different than the previously generated one).
"""

import string
import random
PWD_LEN = 8


def generate_password():
    """
    This function will generate password of 8 char, combination of upper, lower case, digit, special char
    :return: rand_pwd returns password
    """
    char = "@#$%^&*=()_:[]?<>/|~!"
    upper = string.ascii_uppercase
    lower = string.ascii_lowercase
    digits = string.digits

    pwd = list(upper + lower + char + digits)
    rand_pwd = random.choice(upper) + random.choice(lower) + random.choice(digits) + random.choice(char)

    for i in range(PWD_LEN - len(rand_pwd)):
        rand_pwd = rand_pwd + random.choice(pwd)
        random.shuffle(list(rand_pwd))
    return rand_pwd


if __name__ == "__main__":
    pwd = generate_password()
    print(f"Random password is '{pwd}'")
