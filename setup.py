from setuptools import setup , find_packages
from typing import List

hypen_e_dot = '-e .'

def get_requirement(filepath:str)->list[str]:
    requirements=[]
    with open(file_path) as f:
        requirements=f.readlines()
        requirements=[req.replace('/n','')for req in requirements]
        
        if hypen_e_dot in requirements:
            requirements.remove(hypen_e_dot)
        
        return requirements

setup(
    name = "src",
    version="0.0.1",
    Author="Raghavendra",
    author_email="dosinarayanaraghavendra@gmail.com",
    install_requires=get_requirement("requirements.txt"),
    Packages=find_packages()        
    )