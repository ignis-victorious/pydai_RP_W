#  Import LIBRARIES
from pydantic import BaseModel

#  Import FILES
#  ______________________
#


class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    fun_fact: str
