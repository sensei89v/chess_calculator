from setuptools import setup

setup(name='setupcalculator',
      version='1',
      description='Package to work with post codes',
      packages=['setupcalculator'],
      package_dir={'setupcalculator':'src'}
      install_requires=[
          'flask',
      ],
     )
