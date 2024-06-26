import os
from box.exceptions import BoxValueError
import yaml
from src.mlProject import logger
import json
import joblib
from ensure import ensure_annotations
from box import ConfigBox
from pathlib import Path
from typing import Any


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> ConfigBox:
    '''reads yaml file and return
        Args:
        path_to_yaml (str) : path like input

        raises: 
        Value Error : if yaml file is empty
        e: Empty file

        Returns: 
        ConfigBox : Configbox type
    '''
    
    try: 
        with open(path_to_yaml) as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"yaml file : {path_to_yaml} loaded successfully")
            return ConfigBox(content)
    except BoxValueError:
        raise ValueError('yaml file is empty')
    except Exception as e:
        raise e
    

@ensure_annotations
def create_directories(path_to_directories: list,verbose=True):
    '''
    create list of directories

    Args: 
        path_to_directories (list): list of path of directories
        ignore_log (bool,optional): ignore if multiple  dirs  is to be created. Default is False
    '''

    for path in path_to_directories:
        os.makedirs(path,exist_ok=True)
        if verbose:
            logger.info(f"Created a directory: {path}")


@ensure_annotations
def save_json(path: Path,data: dict):
    '''
    save json file

    Args:
        path (Path) : path of json file
        data (dict) : data to be saved in json file
    '''

    with open(path,'w') as f:
        json.dump(data,f,indent=4)

    logger.info(f'json file created: {path}')


@ensure_annotations
def load_json(path: Path) -> ConfigBox:
    """
    load json file data

    Args:
        path : path to json file

    Returns:
        configbox : data as class attributes instead of dict
    """

    with open(path) as f:
        content = load_json(f)


    logger.info(f"json file loaded successfully from: {path}")
    return ConfigBox(content)


@ensure_annotations
def save_bin(data: Any, path:Path):
    """
    save binary data

    Args:
        data (Any): data to be saved binary
        path (Path): path to binary file
    """

    joblib.dump(value=data, filename=path)
    logger.info(f"binary file saved at: {path}")


@ensure_annotations
def load_bin(path:Path) -> Any:
    """
    load binary data

    Args:
        path(Path): path to binary file

    Returns:
        Any: object stored in the file
    """

    data = joblib.load(path)
    logger.info(f"binary file loaded successfully :{path}")
    return data


@ensure_annotations
def get_size(path: Path):
    """
        get size in KB

        Args:
            path (Path): path of the file

        
        Returns:
            str: size in KB

    """
    size_in_kb = round(os.path.getsize(path)/1024)
    return f"~ {size_in_kb} KB"