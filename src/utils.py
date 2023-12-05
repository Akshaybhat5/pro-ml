import sys
import os
from src.exception import CustomException
from src.logger import logging
import pickle


def save_objects(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)
        
        with open(file_path) as file_obj:
            pickle.dump(obj, file_path)

    except Exception as e:
        raise CustomException(e, sys)