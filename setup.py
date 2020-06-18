import os
from setuptools import setup

README = open(os.path.join(os.path.dirname(__file__), 'README.md')).read()


setup(
    name='yandex-api',
    version='1.0.2',
    packages=['yandex'],
    url='https://github.com/akshay-movieverse/yandex-api',
    license='MIT License',
    author='Akshay Singh',
    author_email='akshayrameshwar2018@gmail.com',
    description='Yandex.disk http api client',
    long_description=README,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries',
    ],
    install_requires = [
        'requests >= 2.9.1',
    ],
)
