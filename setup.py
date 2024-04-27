#this is setup.py file, generally we used to create package of entire project !
#so importing all the important library which is used to create setup module

from setuptools import setup,find_packages
from typing import List


#creating user defined function to get all the requirement of library in a list object 
def get_requirements(filename:str)->list[str]:
    requirements = []
    with open(filename,'r') as f:
        #now reading all content from file
        text = f.read()
        #splitting that content into lines
        rows = text.split('\n')

        for line in rows:
            if '-e .' in line:
                continue
            else:
                requirements.append(line)
    return requirements





#creating an object of setup class

setup(
    name="Python_Automobile_Project",
    version="0.0.1",
    author="Raees Azam Shaikh",
    author_email='shaikhraishazam@gmail.com',
    url = 'https://github.com/raish123/ML_AUTOMOBILE_PROJECT',
    long_description=open('readme.md').read(),
    #creating an object of find_packages class
    packages=find_packages(), # Automatically find packages in the project directory
    install_requires = get_requirements('requirements.txt'),
    classifiers=[
        'Programming Language :: Python :: 3.11.5',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ]



)