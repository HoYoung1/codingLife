import dataclasses


@dataclasses.dataclass
class Department:
    _chargeCode: int
    _manager: str

    @property
    def chargeCode(self):
        return self._chargeCode

    @chargeCode.setter
    def chargeCode(self, arg):
        self._chargeCode = arg

    @property
    def manager(self):
        return self._manager

    @manager.setter
    def manager(self, arg):
        self._manager = arg


@dataclasses.dataclass
class Person:
    _name: str
    _department: Department

    def __init__(self, name) -> None:
        self._name = name

    @property
    def name(self):
        return self._name

    @property
    def manager(self):
        return self._department.manager


aPerson = Person('hy')

# manager = aPerson.department.manager
manager = aPerson.manager


