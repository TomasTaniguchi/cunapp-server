from models.script import Script
from datetime import datetime
import subprocess


# Esto debe ser una DB cuña o la forma en la que tengas almacenados tus scripts
MOCK_DATA = [Script(id=1, name="hello.sh", description="Hello from Bash script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id=2, name="hello.py",
                    description="Hello from python script", started_at=datetime.now(), last_time_run=datetime.now()),
             Script(id=3, name="hello.js", description="Hello from JS script", started_at=datetime.now(), last_time_run=datetime.now())]

# Esto no va aca, podes ponerlo en un common file


class InvalidScriptException(Exception):
    'Not matching script found'
    pass


async def get_script(script_id: int) -> Script:
    try:
        return list(filter(lambda x: (x.id == script_id), MOCK_DATA))[0]
    except IndexError:
        return Exception("the id does not exist")


async def get_all_scripts() -> [Script]:
    return MOCK_DATA  # Aca podes agregar validaciones si la data es diferente de null si pasa el modelo Script etc etc,
    # Pero como es un mock no lo hago


async def script_runner(script: Script) -> Script | InvalidScriptException:
    # Selector primitivo para el runner de tus scripts
    if script.name.endswith('py'):
        print("running python"+script.name)
        subprocess.run(["python3", script.name])
        return script
    elif script.name.endswith('js'):
        print("Running javascript script")
        # Aca podes usas el runtime que quieras, node, deno, bun, etc
        subprocess.run(["node", script.name])
        return script
    elif script.name.endswith('sh') or script.name.endswith('bash'):
        print("Running bash script")
        subprocess.run(["bash", script.name])
        return script
    else:
        raise await InvalidScriptException
