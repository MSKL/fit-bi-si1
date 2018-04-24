import hashlib
import random


class Crypto:

    @staticmethod
    def _generate_salt(length):
        """Generate a random salt of a given length"""
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(alphabet) for i in range(length))

    @staticmethod
    def hash_password(passw, salt):
        """ Takes in an username and salt and returns a hash"""
        return hashlib.sha256(str(passw).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()

    @staticmethod
    def generate_password_salt(passw):
        """Generated a password_hash, salt tuple"""
        salt = Crypto._generate_salt(16)
        hashed = Crypto.hash_password(passw, salt)
        return hashed, salt
