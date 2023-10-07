from pydantic import BaseModel
from datetime import datetime


class Script(BaseModel):
    id: int
    name: str
    description: str | None = None
    started_at: datetime
    last_time_run: datetime
