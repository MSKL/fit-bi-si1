import hashlib
import random


class Crypto:
    @staticmethod
    def hash_password(passw, salt):
        """ Takes in an username and salt and returns a hash
        :param passw: string
        :param salt: string
        :return: hash - 64 digits
        """
        return hashlib.sha256(str(passw).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()

    @staticmethod
    def _generate_salt(length):
        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(alphabet) for i in range(length))

    @staticmethod
    def generate_password_salt(passw):
        salt = Crypto._generate_salt(16)
        hashed = Crypto.hash_password(passw, salt)
        return hashed, salt
