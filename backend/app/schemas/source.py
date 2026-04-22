from typing import Literal

from pydantic import BaseModel


class SourceStatusRead(BaseModel):
    country: str
    portal: str
    status: Literal["connected", "pilot", "planned"]
    cadence: str
