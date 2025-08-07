from sonnenbatterie2 import SonnenBatterieV2
from typing import Optional
from .utils import get_package_conf
import logging

class PVSonne(SonnenBatterieV2):

    def __init__(self, fn_conf:Optional[str]=None):
        conf=get_package_conf(fn_conf)
        logging.info(f"Connecting to SonnenBatterie with {conf}")
        super().__init__(conf['host'],conf['token'])

            
