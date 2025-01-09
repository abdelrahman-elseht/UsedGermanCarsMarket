from setuptools import setup,find_packages
from src.utils import get_requirements









setup(
  name= 'Mlporject',
  version = '0.1',
  packages = find_packages(),
  author = 'Abdelrahman Elseht',
  license = 'MIT',
  author_email='elsehtabdelrahman@gmail.com',
  install_requires = get_requirements('requirements.txt')
)