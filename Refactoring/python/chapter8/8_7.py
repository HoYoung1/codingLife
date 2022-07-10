import dataclasses
import sys
from functools import reduce


def youngest_age(people):
    return min(people, key=lambda p: p.age)



@dataclasses.dataclass
class People:
    age: int
people = [People(3), People(5), People(1)]

def total_salary(people):\
    return reduce(lambda total, p: total+p.age, people, 0)

print(total_salary(people))

print(youngest_age(people))
def tttt(people):
    # people = []
    youngest = youngest_age(people)
    totalSalary = total_salary(people)
    return f'최연소: {youngest}, 총 급여: {totalSalary}'


tttt(people)
