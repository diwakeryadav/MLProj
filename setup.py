from setuptools import find_packages,setup 
from typing import List

hypen_e='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION RETURNS THE LIST OF REQUIRMENTS
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"")for req in requirements]
    if hypen_e in requirements:
        requirements.remove(hypen_e)


setup(
name='mlproject',
version='0.0.1',
author='diwaker',
author_email='diwaker.yadav27@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)