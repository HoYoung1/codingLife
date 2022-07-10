import dataclasses


@dataclasses.dataclass
class TelephoneNumber:
    _areaCode: int
    _number: int

    @property
    def areaCode(self):
        return self._areaCode

    @areaCode.setter
    def areaCode(self, arg):
        self._areaCode = arg

    @property
    def number(self):
        return self._number

    @number.setter
    def number(self, arg):
        self._number = arg


@dataclasses.dataclass
class Person:
    def __init__(self) -> None:
        self._telephoneNumber = TelephoneNumber()

    @property
    def officeAreaCode(self):
        return self._telephoneNumber.areaCode

    @officeAreaCode.setter
    def officeAreadCode(self, arg):
        self._telephoneNumber.areaCode = arg

    @property
    def officeNumber(self):
        return self._telephoneNumber.number

    @officeNumber.setter
    def officeNumber(self, arg):
        self._telephoneNumber.number = arg
