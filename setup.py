import os
from octogrid.utils import utils
from octogrid import __version__
from setuptools import setup


# read content from utility files
def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()

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
    install_requires=utils.build_dependecies(),
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
