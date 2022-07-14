import dataclasses

@dataclasses.dataclass
class Telephone:
    _officeAreaCode: int
    _officeNumber: int

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
    def __str__(self):
        return f'{self.officeAreaCode} {self.officeNumber}'


@dataclasses.dataclass
class Person:
    _name: str
    _telephone = Telephone()

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, arg):
        self._name = arg

    @property
    def officeAreaCode(self):
        return self._telephone.officeAreaCode

    @officeAreaCode.setter
    def officeAreaCode(self, arg):
        self._telephone.officeAreaCode = arg

    @property
    def officeNumber(self):
        return self._telephone.officeNumber

    @officeNumber.setter
    def officeNumber(self, arg):
        self._telephone.officeNumber = arg

    @property
    def telephoneNumber(self):
        return str(self._telephone)
