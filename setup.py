from setuptools import find_packages, setup # type: ignore
from typing import List

a = '-e .'
def get_requirement(file_path:str) -> list[str]:
    requirement = []
    with open(file_path) as file_obj:
        requirement = file_obj.readlines()
        requirement = [req.replace("\n"," ") for req in requirement]
        if a in requirement:
            requirement.remove(a)
    return requirement


setup(name = 'ml_project',
      version = '0.0.1',
      author = 'sayak',
      author_email = 'sayaksahaeconomics@gmail.com',
      packages = find_packages(),
      install_requires = get_requirement("requirements.txt")
      )