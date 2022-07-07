import dataclasses
from typing import Dict


@dataclasses.dataclass
class Organization:
    _data: Dict

    @property
    def data(self):
        return self._data


organization = Organization({
    "name": "애크미 구스베리",
    "country": "GB"
})


def get_raw_data_of_organization():
    return organization.data


def get_organization():
    return organization


## client
result = get_raw_data_of_organization()["name"]

get_raw_data_of_organization()["name"] = "tttnewName"
