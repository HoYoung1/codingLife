import dataclasses
from typing import List


@dataclasses.dataclass
class Course:
    _name: str
    _is_advanced: bool

    def __init__(self, name: str, is_advanced: bool) -> None:
        self._name = name
        self._is_advanced = is_advanced

    @property
    def name(self) -> str:
        return self._name

    @property
    def is_advanced(self) -> bool:
        return self._is_advanced


@dataclasses.dataclass
class Person:
    _name: str
    _courses: list

    def __init__(self, name) -> None:
        self._name = name
        self._courses = []

    @property
    def name(self) -> str:
        return self._name

    @property
    def courses(self) -> List[Course]:
        return self._courses

    @courses.setter
    def courses(self, aList: List[Course]) -> None:
        self._courses = aList


p = Person("hy")
p.courses = [
    Course("math", False),
    Course("science", True),
    Course("english", False),
]

print(len(list(filter(lambda c: c.is_advanced, p.courses))))


# del p.courses[1]

def read_basic_course_names() -> List[str]:
    return ["m", "s", "e"]


basic_course_names = read_basic_course_names()
print(basic_course_names)

# p.courses = list(map(lambda name: Course(name, False), basic_course_names))
# print(p.courses)

for name in read_basic_course_names():
    p.courses.append(Course(name, False))
print(p.courses)








