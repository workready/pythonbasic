import argparse
import getpass
import hashlib
import os

# CONSTANTS
HELP_TEXT = 'My connection client'
SIGN_OFF = 'Author: John Doe <john@doe.com>'


# FUNCTIONS
def users_dict():
    USERNAME = 'pue'
    PASSWORD = 'mypassword'

    salt = os.urandom(32)  # A new salt for the user
    key = hashlib.pbkdf2_hmac('sha256', PASSWORD.encode('utf-8'), salt, 100000)
    users = {
        USERNAME: {
            'salt': salt,
            'key': key
        }
    }

    return users


def handle_arguments(description, epilog):
    parser = argparse.ArgumentParser(description=description, epilog=epilog)

    parser.add_argument("-u", "--username", help="Username. If not provided it will be read from USERNAME env var")
    parser.add_argument("-p", "--password", action="store_true", help="Ask for password")

    args = parser.parse_args()

    return args


def verify(username, password):
    users = users_dict()
    if username not in users:
        raise Exception('Username not found')

    salt = users[username]['salt']
    key = users[username]['key']
    new_key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)

    return key == new_key


# MAIN PROGRAM
if __name__ == "__main__":
    args = handle_arguments(HELP_TEXT, SIGN_OFF)

    username = args.username or os.getenv('USERNAME')
    if args.password:
        password = getpass.getpass("Introduce password: ")
    else:
        password = os.getenv('PASSWORD')

    if not username or not password:
        raise Exception("Error: user and password needed")

    if verify(username, password):
        print("Correct credentials")
    else:
        print("Wrong credentials")

