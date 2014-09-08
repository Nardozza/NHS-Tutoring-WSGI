"""Configuration file for flask."""
import os
CSRF_ENABLED = True
SECRET_KEY = 'WE2SZqXxV4QzWaj49ha4Dja3sNZurvej99RBDYWsMGr26tjh2thF7aCNhLzdprvmKet3ryr8'

OPENID_PROVIDERS = [{'name': 'Google', 'url': 'https://www.google.com/accounts/o8/id'}]

basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')