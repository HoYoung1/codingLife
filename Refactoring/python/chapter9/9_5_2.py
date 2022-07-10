import dataclasses


@dataclasses.dataclass
class Customer:
    def __init__(self, id) -> None:
        self._id = id

    @property
    def id(self):
        return self._id


@dataclasses.dataclass
class Order:
    def __init__(self, data) -> None:
        self._number = data.number
        self._customer = registerCustomer(data.customer)  # data.cusomter = 고객 id


_repositoryData = None


def initialize():
    _repositoryData = {}
    _repositoryData.customers = {}


def registerCustomer(id):
    _repositoryData = None
    if not _repositoryData.customers.has(id):
        _repositoryData.customers.set(id, Customer(id))
    return findCustomer(id)


def findCustomer(id):
    return _repositoryData.customers.get(id)
