from setuptools import setup

setup(name='chess_calculator',
      version='1',
      description='Package to work with post codes',
      packages=['chess_calculator'],
      package_dir={'chess_calculator':'src'},
      install_requires=[
          'flask>=1.1.2',
          'marshmallow>=3.9.1',
          'uwsgi>=2.0.19'
      ],
     )
