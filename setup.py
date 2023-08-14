#import all available packages into dir, setup 
from setuptools import find_packages, setup
from typing import List

#read list of requirements into list from file 
#'-e' == editable :: '.' connects setup.py with req.txt
HYPHEN = '-e .'
def get_requirements(file_path:str)->List[str]:
    requirements=[]
    #create temp_obj of file
    with open(file_path) as file_obj:
        #read file into req line by line
        requirements=file_obj.readlines()
        #replace default \n with empty space when reading req.txt
        requirements=[req.replace("\n","") for req in requirements]
        #rem -e . 
        if HYPHEN in requirements:
            requirements.remove(HYPHEN)
    return requirements

#metadata
setup(
    name = 'knmlpipeline',
    version = '0.0.1',
    author = 'pratywillsaveu',
    author_email = 'kandpalp200018@gmail.com',
    #find all modules under src dir
    packages=find_packages(),
    #read req libs using custom method from req.txt
    install_requires = get_requirements('requirements.txt') 
)


    

