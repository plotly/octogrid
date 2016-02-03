from os.path import dirname, join
from octogrid import __version__
from setuptools import setup


def read(filename):
    """
    Read content from utility files
    """

    return open(join(dirname(__file__), filename)).read()


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
    install_requires=[
        'colorlover>=0.2.1',
        'decorator>=4.0.6',
        'docopt>=0.6.2',
        'github3.py>=0.9.4',
        'ipython>=4.0.3',
        'ipython-genutils>=0.1.0',
        'path.py>=8.1.2',
        'pexpect>=4.0.1',
        'pickleshare>=0.6',
        'plotly>=1.9.5',
        'ptyprocess>=0.5',
        'python-igraph>=0.7.1.post6',
        'pytz>=2015.7',
        'requests>=2.9.1',
        'simplegeneric>=0.8.1',
        'six>=1.10.0',
        'traitlets>=4.1.0',
        'uritemplate.py>=0.3.0',
        'wheel>=0.24.0'
    ],
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
