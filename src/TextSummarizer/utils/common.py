import os 
from box.exceptions import BoxValueError
import yaml
from TextSummarizer.logging import logger
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any



@ensure_annotations
def read_yaml(path_to_yaml: Path)-> ConfigBox:
    """
    Reads a yaml file and returns 

    Args: 
        path_to_yaml (str): path like input
    

    Raises:
        FileNotFoundError : If the given filepath does not exist or is invalid
        BoxValueError : If the yaml file is invalid
        e: empty file
    
    Returns:
        ConfigBox: Configbox type
    
    """
    
    try:
        with open(path_to_yaml) as yml_file:
            data = yaml.safe_load(yml_file)
            logger.info(f'yaml file: {path_to_yaml} loaded successfully')
            return ConfigBox(data)
    except BoxValueError:
        raise ValueError('yaml file is empty.')
    except Exception as e:
        raise e
    



@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    '''
    Creates a list of directories
    Arguments:
        path_to_directories (list): list of directories
        verbose (bool, optional): ignore if multiple directories are to be created. Defaults to True.
    '''
    for directory in path_to_directories:
        os.makedirs(directory, exist_ok=True)
        if verbose:
            logger.info(f'created directory at: {directory}')




@ensure_annotations
def get_size(path: Path)-> str:
    '''
    Returns the size of a file in KB
    Arguments:
        path (Path): path to file
    '''
    
    return f'~ {round(os.path.getsize(path)/1024)} KB'
