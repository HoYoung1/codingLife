import dataclasses
from typing import Dict


@dataclasses.dataclass
class Organization:
    _data: Dict

    def __init__(self, data) -> None:
        # self._data = data
        self._name = data["name"]
        self._country = data["country"]

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, t):
        self._name = t

    @property
    def country(self):
        return self._country

    @name.setter
    def country(self, t):
        self._country = t


organization = Organization(data={
    "name": "애크미 구스베리",
    "country": "GB"
})


def get_organization():
    return organization


## client
result = get_organization().name

get_organization().name = "tttnewName"
