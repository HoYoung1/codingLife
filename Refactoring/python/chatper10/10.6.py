import dataclasses


@dataclasses.dataclass
class Customer:

    @property
    def name(self):
        return "미확인 고객"

    @property
    def billingPlan(self):
        return "요금제"

    @billingPlan.setter
    def billingPlan(self, arg):
        pass

    @property
    def paymentHistory(self):
        pass

    @property
    def isUnknown(self):
        return False

    def __eq__(self, other: object):
        if isinstance(other, str):
            return self.name == other


class NullPaymentHistory:
    pass


class UnknownCustomer:
    @property
    def isUnknown(self):
        return True

    @property
    def name(self):
        return "거주자"

    @property
    def billingPlan(self):
        return registry

    @property
    def paymentHistory(self):
        NullPaymentHistory()


@dataclasses.dataclass
class Site:
    _customer: Customer

    @property
    def customer(self):
        return UnknownCustomer() if self._customer == "미확인 고객" else self._customer


def isUnknown(arg: Customer):
    if not (isinstance(arg, UnknownCustomer) or arg == "미확인 고객"):
        raise Exception('잘못된 값과 비교')
    return arg.isUnknown


# 클라이언트 1
site = Site(Customer())
aCustomer = site.customer
##### 수많은 코드
customerName = aCustomer.name

# 클라언트 2
registry = None
plan = None
if aCustomer.isUnknown:
    plan = registry
else:
    plan = aCustomer.billingPlan

# 클라이언트 3
newPlan = None
if not aCustomer.isUnknown:
    aCustomer.billingPlan = newPlan

# 클라이언트 4
weeksDelinquent = 0 if isUnknown(aCustomer) else aCustomer.paymentHistory
