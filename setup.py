from setuptools import setup, find_packages
from typing import List

hype='-e .'

def get_requirement(file_path:str)->list[str]:
    requirements=[]
    with open (file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]

        if hype in requirements:
            requirements.remove(hype)

    return requirements



setup(
    name="your_package_name",  # Replace with your package name
    version="0.1.0",  # Initial version
    author="Harchetan ",
    author_email="harchetansingh116@gmail.com",
    description="A short description of your package",
    long_description=open("README.md").read(),  # Optional: Include a README file
    long_description_content_type="text/markdown",
    url="https://github.com/Harchetan-singh-Chahal/ETE-ML_project",  # Replace with your repository URL
    packages=find_packages(),  # Automatically find packages in the directory
    install_requires=get_requirement('requirement.txt')
  
)