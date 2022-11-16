import yaml
from customer_personality.exception.exception_handler import AppException
import sys

def read_yaml_file(file_path:str) -> dict:
    """
    Reads YAML file and return content as dict
    """
    try:
        with open(file_path,'rb') as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise AppException(e,sys) from e