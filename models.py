#  Import LIBRARIES
from typing import Any

import requests
from pydantic import BaseModel

#  Import FILES
#  ______________________
#


class CityInfo(BaseModel):
    name: str
    country: str
    population: int
    fun_fact: str


class UserDatabase:
    """Simulate a user database using the JSONPlaceholder users API."""

    _base_url: str = "https://jsonplaceholder.typicode.com"

    def get_user_info(self, user_id: int) -> Any:
        response: requests.Response = requests.get(url=f"{self._base_url}/users/{user_id}")
        response.raise_for_status()
        return response.json()


class UserSummary(BaseModel):
    name: str
    email: str
    company: str
