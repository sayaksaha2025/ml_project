from setuptools import find_packages, setup
from typing import List
a = '-e .'

def get_requirement(file_path:str)-> list[str]:
    '''This function will return the list of requirements'''
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n"," ") for req in requirements]
        if a in requirements:
            requirements.remove(a)
    return requirements



setup(
name = 'ml_project',
version = '0.0.1',
author = 'Sayak',
author_email = 'sayaksahaeconomics@gmail.com',
packages = find_packages(),
install_requires = get_requirement('requirements.txt')
)