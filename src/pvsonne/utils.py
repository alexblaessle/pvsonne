import json
import os

from typing import Optional


def read_json(fn:str)->dict:

    with open(fn,'r') as f:
        ret=json.load(f)
    return ret

def get_package_data_dir():
    
    return os.path.join(os.path.dirname(__file__),"data")
    

def get_package_data(fn:str)-> str:
    return os.path.join(get_package_data_dir(),fn)

def get_package_conf(fn:Optional[str]=None)->dict:
    if fn:
        ret=read_json(fn)
    else:
        ret=read_json(get_package_data("conf.json"))
    return ret