import hashlib
import random

ALPHABET = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"


def hash_password(username, salt):
    """ Takes in an username and salt and returns a hash
    :param username: string
    :param salt: string
    :return: hash - 64 digits
    """
    return hashlib.sha256(str(username).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()


def generate_salt(len):
    return ''.join(random.choice(ALPHABET) for i in range(len))