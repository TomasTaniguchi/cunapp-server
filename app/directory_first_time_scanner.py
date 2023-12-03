from os import walk
import jsonlines
from datetime import datetime
from models.script import Script
import uuid
from typing import List

def ls(path: str) -> dict:
    _, subdirs, files = next(walk(path))    
    return {'scripts': files, 'sub_directories': subdirs}

def script_generator(script: str) -> Script:
    return Script(id=str(uuid.uuid4()), name=script, description=script, started_at=datetime.now(), last_time_run=datetime.now())


def script_loader(fn,args: list) -> List[Script]:
    return list(map(fn,args.get('scripts')))


