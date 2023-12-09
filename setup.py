"""A setuptools based setup module.

See:
https://packaging.python.org/en/latest/distributing.html
https://github.com/pypa/sampleproject
"""

# To use a consistent encoding
from os import path

# Always prefer setuptools over distutils
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
try:
    with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
        long_description = f.read()
except Exception as e:
    long_description = "LexPredict LexNLP: A swiss-army knife library built for working with real, unstructured legal text."

setup(
    name='lexnlp',

    # Versions should comply with PEP440.  For a discussion on single-sourcing
    # the version across setup.py and the project code, see
    # https://packaging.python.org/en/latest/single_source_version.html
    version='2.3.0',

    description='LexPredict LexNLP',
    long_description=long_description,

    # The project's main homepage.
    url='https://contraxsuite.com',

    # Author details
    author='ContraxSuite, LLC',
    author_email='support@contraxsuite.com',

    # Choose your license
    license='AGPL',

    # version ranges for supported Python distributions
    python_requires='~=3.6',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 4 - Beta',

        # Indicate who your project is intended for
        'Intended Audience :: Information Technology',
        'Intended Audience :: Legal Industry',
        'Intended Audience :: Developers',

        # Pick your license as you wish (should match "license" above)
        # 'License :: OSI Approved :: MIT License',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'License :: Other/Proprietary License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 3.6',

        # Topics
        'Natural Language :: English',
        'Topic :: Office/Business',
        'Topic :: Text Processing :: Linguistic',

    ],

    # What does your project relate to?
    keywords='legal contract document analytics nlp ml machine learning natural language',

    # You can just specify the packages manually here if your project is
    # simple. Or you can use find_packages().
    packages=find_packages(exclude=['*tests*']),

    # Alternatively, if you want to distribute just a my_module.py, uncomment
    # this:
    # py_modules=['lexnlp'],

    # List run-time dependencies here.  These will be installed by pip when
    # your project is installed. For an analysis of "install_requires" vs pip's
    # requirements files see:
    # https://packaging.python.org/en/latest/requirements.html
    install_requires=[
        'beautifulsoup4>=4.11.1',
        'cloudpickle>=2.2.0',
        'dateparser>=1.1.3',
        'elasticsearch>=8.5.0',
        'gensim>=4.1.2',
        'importlib-metadata>=5.0.0',
        'joblib>=1.2.0',
        'lxml>=4.9.1',
        'nltk>=3.7',
        'num2words>=0.5.12',
        'numpy>=1.23.4',
        'pandas>=1.5.1',
        'psutil>=5.9.4',
        'pycountry>=22.3.5',
        'python-dateutil>=2.8.2',
        'regex>=2022.3.2',
        'reporters-db>=3.2.32',
        'requests>=2.28.1',
        'scikit-learn>=0.24',
        'scipy>=1.9.3',
        'tqdm>=4.64.1',
        'Unidecode>=1.3.6',
        'us>=2.0.2',
        'zahlwort2num>=0.4.2'
    ],

    # Install any data files from packages.
    # The data files must be specified via the distutils’ MANIFEST.in file.
    include_package_data=True,

    # List additional groups of dependencies here (e.g. development
    # dependencies). You can install these using the following syntax,
    # for example:
    # $ pip install -e .[dev,test]
    extras_require={
        'dev': ['pytest>=2.8.5', 'mock', 'pytz>=2015.7', 'nose', 'memory-profiler', 'psutil', 'matplotlib',
                'Sphinx>=5.3.0'],
        'test': ['pytest>=2.8.5', 'mock', 'pytz>=2015.7', 'nose', 'memory-profiler', 'psutil', 'Sphinx>=5.3.0'],
    },

    # If there are data files included in your packages that need to be
    # installed, specify them here.  If using Python 2.6 or less, then these
    # have to be included in MANIFEST.in as well.
    # package_data={
    #     'sample': ['package_data.dat'],
    # },

    # Although 'package_data' is the preferred approach, in some case you may
    # need to place data files outside of your packages. See:
    # http://docs.python.org/3.4/distutils/setupscript.html#installing-additional-files # noqa
    # In this case, 'data_file' will be installed into '<sys.prefix>/my_data'
    # data_files=[('my_data', ['data/data_file'])],

    # To provide executable scripts, use entry points in preference to the
    # "scripts" keyword. Entry points provide cross-platform support and allow
    # pip to create the appropriate form of executable for the target platform.
    # entry_points={
    #     'console_scripts': [
    #         'sample=sample:main',
    #     ],
    # },
)
