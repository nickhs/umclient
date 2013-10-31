from setuptools import setup
import os


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(name='umclient',
    version='0.0.1',
    description='Authenticated Client for University of Michigan Web Services',
    url='http://github.com/nickhs/umclient',
    author='Nick HS',
    author_email='nickhs@umich.edu',
    license='MIT',
    long_description=read('README.md'),
    packages=['umclient'],
    install_requires=[
        'requests',
    ])
