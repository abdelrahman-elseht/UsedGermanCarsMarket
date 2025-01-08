from setuptools import setup,find_packages


def get_requirements(file_path:str)->list:
  requirements = []
  with open(file_path) as file_obj:
    requirements = file_obj.readlines()
    requirements = [req.replace("\n","") for req in requirements]

    if ('-e .') in requirements:
      requirements.remove('-e .')

  return requirements






setup(
  name= 'Mlporject',
  version = '0.1',
  packages = find_packages(),
  author = 'Abdelrahman Elseht',
  license = 'MIT',
  author_email='elsehtabdelrahman@gmail.com',
  install_requires = get_requirements('requirements.txt')
)