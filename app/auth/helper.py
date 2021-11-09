import os
import hashlib
import binascii

def hash_password(password):
    """
    Fungsi untuk hashing password sebelum disimpan pada database
    """
    salt = hashlib.sha256(os.urandom(50)).hexdigest().encode('ascii')
    password_hash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'), salt, 100000)
    password_hash = binascii.hexlify(password_hash)
    return (salt + password_hash)

def verify_password(provided_password, stored_password):
    """
    Fungsi untuk verifikasi password
    """
    stored_password = stored_password.decode('ascii')
    salt = stored_password[:50]
    stored_password = stored_password[50:]
    password_hash = hashlib.pbkdf2_hmac('sha512', provided_password.encode('utf-8'), salt.encode('ascii'), 100000)
    password_hash = binascii.hexlify(password_hash).decode('ascii')
    return password_hash == stored_password