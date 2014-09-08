"""Database stuff."""
from random import SystemRandom
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from app import db
from hmac import compare_digest
from hashlib import pbkdf2_hmac

ROLE_USER = 0
ROLE_TUTOR = 1
ROLE_ADMIN = 2


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(50), index = True, unique = True)
    _password = db.Column(db.LargeBinary(120))
    _salt = db.Column(db.String(120))
    email = db.Column(db.String(120), index = True, unique = True)
    role = db.Column(db.SmallInteger, default = ROLE_USER)

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    @hybrid_property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if self._salt is None:
            self._salt = bytes(SystemRandom().getrandbits(128))
        self._password = self._hash_password(value)

    def is_valid_password(self, password):
        new_hash = self._hash_password(password)
        return compare_digest(new_hash, self._password)

    def _hash_password(self, password):
        pwd = password.encode("utf-8")
        salt=bytes(self._salt)
        buff = pbkdf2_hmac("sha512", pwd, salt, 100000)
        return bytes(buff)

    def __repr__(self):
        return '<User #{0}>'.format(self.id)
