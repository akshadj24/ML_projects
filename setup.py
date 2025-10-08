from setuptools import find_packages,setup
from typing import List


DOT_E='-e  .'
def requiremnets_list(file_path:str)->List[str]:
    requiremnets=[]

    with open(file_path) as obj:
        requiremnets=obj.readlines()

        requiremnets=[ i.replace("\n","") for i in requiremnets]

    if DOT_E in requiremnets:
        requiremnets.remove(DOT_E)

    return requiremnets

 
setup(
    name='MLProject',
version='0.0.1',
author='Akshad',
author_email='akshadj2005@gmail.com',
packages=find_packages(),
install_requires=requiremnets_list('requirements.txt')
)
