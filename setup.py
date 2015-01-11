import os
from setuptools import setup, find_packages

README = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()

setup(
    name='matasano-crypto',
    packages=find_packages('src', exclude=('tests',)),
    package_dir={'': 'src'},
    description='My attempt at the Matasano Crypto Challenges.\
                 http://cryptopals.com/',
    long_description=README,
    url='https://github.com/mthpower/matasano-crypto',
    author='Matthew Power',
    author_email='mth.power@gmail.com',
    zip_safe=True,
    install_requires=[
    ]
)
