from octogrid import __version__
import os
from setuptools import setup


# read content from utility files
def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

setup(
    name='octogrid',
    version=__version__,
    author='Pravendra Singh',
    author_email='hackpravj@gmail.com',
    description=('command line tool to export your GitHub network as GML format'),
    license = 'MIT',
    keywords = 'github network graph',
    url = 'https://github.com/pravj/octogrid',
    packages=['octogrid', 'octogrid.parser', 'octogrid.exporter', 'octogrid.auth', 'octogrid.builder'],
    install_requires=['docopt', 'github3.py', 'requests', 'uritemplate.py', 'wheel'],
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
