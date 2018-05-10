import hashlib
import random


class Crypto:
    """Crypto class handles the login security hashing and salt generation."""

    @staticmethod
    def _generate_salt(length):
        """
        Generate a random salt of a given length

        :type length: int
        :param length: length of the desired salt string
        :rtype: string
        :return: salt string of the given length
        """

        alphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        return ''.join(random.choice(alphabet) for i in range(length))

    @staticmethod
    def hash_password(passw, salt):
        """
        Hash the password with salt and return the hash.

        :type passw: string
        :param passw: password
        :type salt: string
        :param salt: salt
        :return: hashed password
        """

        return hashlib.sha256(str(passw).encode('utf-8') + str(salt).encode('utf-8')).hexdigest()

    @staticmethod
    def generate_password_salt(passw):
        """
        Return a hashed password and generated salt.

        :type passw: string
        :param passw: password
        :rtype: tuple
        :return: hash, salt
        """

        salt = Crypto._generate_salt(16)
        hashed = Crypto.hash_password(passw, salt)
        return hashed, salt
