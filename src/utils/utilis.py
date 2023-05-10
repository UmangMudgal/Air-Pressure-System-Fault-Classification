from src.logger import logging
from src.exception import CustomException
import sys, os
import yaml
import numpy as np
import dill


def read_yaml_file(file_path:str)->dict:
    try:
        with open(file_path, 'rb') as yml_file:
            return yaml.safe_load(yml_file)
    except Exception as e:
        raise CustomException(e, sys)
    
def write_yaml_file(file_path: str, content: object, replace:bool = False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        with open(file_path, 'w') as file:
            yaml.dump(content, file)

    except Exception as e:
        raise CustomException(e, sys)
    

def save_numpy_array_data(file_path:str, array:np.array):
    """Description : Save Numpy array data to file
       file_path : str location of file to save 
       array : np.array data to save
    """
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        with open(file_path, 'wb') as file_obj:
            np.save(file_obj,array)

    except Exception as e:
        raise CustomException(e, sys)
    

def load_numpy_array_data(file_path : str) -> np.array:
    """Description: Load the numpy array data from file
       file_path : str location of file to load
       return : np.array data loaded
    """

    try:
        with open(file_path, 'rb') as file_obj:
            return np.load(file_obj)
    except Exception as e:
        raise CustomException(e,sys)
    
def save_object(file_path : str, obj: object) -> None:
    """Description: Seriallization process
    """

    try:
        logging.info("Entered the save_object method of utils")
        os.makedirs(os.path.dirname(file_path), exist_ok = True)
        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
        logging.info("Exited the save_object method of utils")
    except Exception as e:
        raise CustomException(e,sys)

