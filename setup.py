#!/usr/bin/env python
"""
setup.py script for wmatz
"""
import ez_setup
ez_setup.use_setuptools()
from setuptools import setup, find_packages
from os import chdir
from os.path import abspath, dirname, join


def readme(filepath):
    """
    Returns contents of a readme file.
    """
    with open(filepath, 'r') as rm:
        return rm.read()


setup_options = dict(name='wmatz',
                     version='0.0.1',
                     description='Weighted center of minimum aggregate travel example',
                     license='Other/Proprietary License',
                     long_description=readme(join(dirname(__file__),
                                                  'README.rst')),
                     author='Allan Adair',
                     author_email='allan.m.adair@gmail.com',
                     url='https://github.com/allanadair/wmatz',
                     packages=find_packages('.'),
                     package_dir={'wmatz': 'wmatz'},
                     zip_safe=False,
                     classifiers=('Development Status :: 1 - Planning',
                                  'Intended Audience :: Developers',
                                  'Natural Language :: English',
                                  'License :: Other/Proprietary License',
                                  'Programming Language :: Python',
                                  'Programming Language :: Python :: 2.7',
                                  'Programming Language :: Python :: 3',
                                  'Programming Language :: Python :: 3.4'))

if __name__ == '__main__':
    chdir(dirname(abspath(__file__)))
    setup(**setup_options)
