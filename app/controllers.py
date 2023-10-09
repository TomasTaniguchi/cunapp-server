from models.script import Script
from datetime import datetime
import subprocess


# Esto debe ser una DB cuña o la forma en la que tengas almacenados tus scripts
MOCK_DATA = [Script(id=1, name="hello.sh", description="Hello from Bash script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id=2, name="hello.py",
                    description="Hello from python script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id=3, name="hello.js", description="Hello from JS script",
                    started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id=4, name="anormal.js", description="Ejecutando a anormales", started_at=datetime.now(), last_time_run=datetime.now())]

# Esto no va aca, podes ponerlo en un common file


class InvalidScriptException(Exception):
    'Not matching script found'
    pass


def runntime_selector(script):
    def ext_checker(ext, runner):
        return subprocess.run([runner, script.name], check=True) if script.name.endswith(ext) else None
    return ext_checker


async def get_script(script_id: int) -> Script:
    try:
        return list(filter(lambda x: (x.id == script_id), MOCK_DATA))[0]
    except IndexError:
        return Exception("the id does not exist")


async def get_all_scripts() -> [Script]:
    return MOCK_DATA  # Aca podes agregar validaciones si la data es diferente de null si pasa el modelo Script etc etc,
    # Pero como es un mock no lo hago


async def script_runner(script: Script) -> tuple | None:
    selector = runntime_selector(script)
    return tuple(filter(lambda x: x != None, (selector("py", "python3"),
                                              selector("js", "node"),
                                              selector("sh", "bash"),
                                              selector("lua", "lua"))))
