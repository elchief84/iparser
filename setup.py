from setuptools import setup, find_packages

version = '0.1'

setup(
      name='iparser',
      version=version,
      description="Extract informations from your .ipa files",
      keywords='ipa ios app plist',
      author='Vincenzo Romano',
      author_email='enzxx84@gmail.com',
      url='',
      license='ISC',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      entry_points={
        'console_scripts': ['iparser = iparser.cli:start']
      }
)