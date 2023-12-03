import os
import subprocess
from datetime import datetime
from models.script import Script

# Esto debe ser una DB cuña o la forma en la que tengas almacenados tus scripts
MOCK_DATA = [Script(id="1", name="hello.sh", description="Hello from Bash script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id="2", name="hello.py",
                    description="Hello from python script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id="3", name="hello.js", description="Hello from JS script",
                    started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id="4", name="anormal.js", description="Ejecutando a anormales", started_at=datetime.now(), last_time_run=datetime.now())]

# Esto no va aca, podes ponerlo en un common file


class InvalidScriptException(Exception):
    'Not matching script found'
    pass


async def runntime_selector(script: Script):
    async def ext_checker(ext, runner):
        return subprocess.run([runner, os.path.join('..', 'scripts', script.name)], check=True) if script.name.endswith(ext) else None
    return ext_checker
# os.path.join(os.chdir('..'), "scripts", script.name)


async def get_script(script_id: int) -> Script:
    try:
        return list(filter(lambda x: (x.id == script_id), MOCK_DATA))[0]
    except IndexError:
        return Exception("the id does not exist")


async def get_all_scripts() -> [Script]:
    return MOCK_DATA  # Aca podes agregar validaciones si la data es diferente de null si pasa el modelo Script etc etc,
    # Pero como es un mock no lo hago


async def script_runner(script: Script) -> tuple | None:
    selector = await runntime_selector(script)
    return tuple(filter(lambda x: x != None, (await selector("py", "python3"),
                                              await selector("js", "node"),
                                              await selector("sh", "bash"),
                                              await selector("lua", "lua"))))
