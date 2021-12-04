from setuptools import setup
from asltam import __version__ as version

setup(
  name='asltam',
  version=version,
  description="Outils d'études de politique des prix des compagnies d'autoroutes",
  url='https://github.com/Eldohrim/Project_2021_HAX712X.git',
  author='CARVAILLO Thomas, BOUARROUDJI Abdelmalek et CAPEL Alexandre',
  author_email='alexcaapel@gmail.com',
  license='MIT',
  packages=['asltam','asltam.io', 'asltam.map', 'asltam.price_distribution','asltam.graph'],
  zip_safe=False
)
