import os
from octogrid import __version__
from setuptools import setup


def read(filename):
    """
    Read content from utility files
    """

    return open(os.path.join(os.path.dirname(__file__), filename)).read()


def build_dependecies():
    """
    Returns a list representing all the required packages
    """

    package_list = []

    with open('requirements.txt', 'r') as f:
        lines = f.readlines()

    for line in lines:
        name, version = line.split('==')
        package_list.append('{0}>={1}'.format(name, version))

    return package_list


setup(
    name='octogrid',
    version=__version__,
    author='Pravendra Singh',
    author_email='hackpravj@gmail.com',
    description=('GitHub following network visualizer for Humans'),
    license = 'MIT',
    keywords = 'github network graph plotly plot chart visualization',
    url = 'https://github.com/pravj/octogrid',
    packages=['octogrid', 'octogrid.parser', 'octogrid.generator', 'octogrid.auth', 'octogrid.builder', 'octogrid.publisher', 'octogrid.store', 'octogrid.utils'],
    install_requires=build_dependecies(),
    long_description=read('README.rst'),
    entry_points={
        'console_scripts': ['octogrid = octogrid.octogrid:main']
    },
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Environment :: Console',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7'
    ]
)
