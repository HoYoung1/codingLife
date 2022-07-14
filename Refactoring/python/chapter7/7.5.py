import dataclasses


@dataclasses.dataclass
class Person:
    _name: str
    _officeAreaCode: int
    _officeNumber: int

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def officeAreaCode(self):
        return self._officeAreaCode

    @officeAreaCode.setter
    def officeAreaCode(self, arg):
        self._officeAreaCode = arg

    @property
    def officeNumber(self):
        return self._officeNumber

    @officeNumber.setter
    def officeNumber(self, arg):
        self._officeNumber = arg

    @property
    def telephoneNumber(self):
        return f'{self.officeNumber} {self.officeNumber}'


