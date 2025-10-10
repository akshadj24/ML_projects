# This wil consist the commane functionality which remain smae throughout the project implemenatation 

import numpy as np
import pandas as pd
import sys
import os
from src.exception import CustomeException
from src.logging import logging
import dill


def save_file(file_path,obj):
    try:

        dir_path=os.path.dirname(file_path)

        os.makedirs(dir_path,exist_ok=True)

        with open(file_path,'wb' ) as file_obj:
            dill.dump(obj,file_obj)

    except Exception as e:
        raise CustomeException(sys,e)        

    



    

