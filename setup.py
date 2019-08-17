"""setup.py
"""
from setuptools import setup, find_packages

with open('README.md') as fh:
    long_description = fh.read()

setup(
    name='qubu',
    version='0.1',
    author='Oleksandr Shepetko',
    author_email='a@shepetko.com',
    description='A Simple Database Query Builder',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://github.com/ashep/qubu',
    download_url='https://github.com/ashep/qubu/archive/master.zip',
    packages=find_packages(exclude=['tests']),
    install_requires=['dicmer'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest', 'pytest-cov'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Database',
        'Topic :: Software Development :: Code Generators',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
