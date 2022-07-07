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
        return self._courses.copy()

    def add_course(self, c: Course) -> None:
        self._courses.append(c)

    def remove_course(self, c: Course):
        idx = self._courses.index(c)
        del self.courses[idx]






p = Person("hy")
p.add_course(Course("math", False))
p.add_course(Course("science", True))
p.add_course(Course("english", False))

p.courses.append(Course("직접 접근?;", False))
print(p.courses)

# print(p.courses[0])
# print(p.courses[0])

p.courses[0].name = "k"

print(p.courses)

# print(id(p.courses))
# print(len(list(filter(lambda c: c.is_advanced, p.courses))))


# del p.courses[1]

def read_basic_course_names() -> List[str]:
    return ["m", "s", "e"]


basic_course_names = read_basic_course_names()
# print(basic_course_names)

# p.courses = list(map(lambda name: Course(name, False), basic_course_names))
# print(p.courses)

for name in read_basic_course_names():
    # p.courses.append(Course(name, False))
    p.add_course(Course(name, False))
# print(p.courses)
