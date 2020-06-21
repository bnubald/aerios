from setuptools import setup
from os import path

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='aerios',
      version='0.0.1',
      description='Machine learning with polynomials',
      long_description=readme(),
      classifiers=[
        'Programming Language :: Python :: 2.7',
	      'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
      ],
      packages=['aerios'],
      data_files=['aerios/data/airlines.xml', 'aerios/data/engines.xml', 'aerios/data/aircraft.xml', 'aerios/data/airports.xml'],
      install_requires=[
          'numpy',
          'scipy >= 0.15.0',
          'matplotlib >= 3.2'
      ],
      test_suite='nose.collector',
      tests_require=['nose'],
      include_package_data=True,
      zip_safe=False)
