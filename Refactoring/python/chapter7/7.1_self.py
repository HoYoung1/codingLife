from typing import Dict



def get_organization_object():
    return Organization(_name="애크미 구스베리", _country="GB")


organization = {
    "name": "애크미 구스베리",
    "country": "GB"
}

from dataclasses import dataclass


@dataclass
class Organization:
    _name: str
    _country: str

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, t) -> None:
        self._name = t

    @property
    def country(self) -> str:
        return self._country

    @country.setter
    def country(self, t) -> None:
        self._country = t


## client
result = get_organization_object().name
get_organization_object().name = "tttnewName"

# assert result == "애크미 구스베리"
# assert organization["name"] == "tttnewName"

organization = Organization(_name="애크미 구스베리", _country="GB")

