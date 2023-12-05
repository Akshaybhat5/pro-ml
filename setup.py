from setuptools import setup, find_packages
from typing import List

HYPEN_DOT_E = "-e ."

def get_requirements(file_path:str)->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [words.replace("\n", "") for words in requirements]

        if HYPEN_DOT_E in requirements:
            requirements.remove(HYPEN_DOT_E)

    return requirements


setup(
    name="ml project",
    version="0.0.1",
    author="Akshay Bhat",
    packages=find_packages(),
    install_requires = get_requirements("requirements.txt")
)



