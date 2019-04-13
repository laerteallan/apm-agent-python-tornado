"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/laerteallan
"""

# Always prefer setuptools over distutils
from setuptools import setup, find_packages
from os import path
import os

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
packages = open("requirements.txt").readlines()
reqs = [package.strip('\n') for package in packages]

here = path.abspath(path.dirname(__file__))

setup(
    name='tornado_elastic',
    version='0.0.1',
    description='Project Apm Elastic for tornado-framework',
    author='Neighbors LTDA',
    author_email='laerte.allan@gmail.com',

    classifiers=[  # Optional

        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
    include_package_data=True,
    package_dir={here: 'tornado_elastic'},
    keywords='sample setuptools development',
    packages=find_packages(here, exclude=['contrib', 'docs', 'tests', 'main.py']),
    package_data={'tornado_elastic': ['*']},
    install_requires=reqs,  # Optional

)
