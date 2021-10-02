import os
from setuptools import setup, find_packages

requires = (
    "flask",
    "flask-sqlalchemy",
    "flask_wtf",
    "WTForms",
    "email-validator",
    "flask-bcrypt",
    "flask-login"
)

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "python_blog",
    author = "Travis Pandos",
    author_email = "travis.pandos@gmail.com",
    license = "MIT",
    packages=find_packages(),
    install_requires=requires,
)