from typing import List


class ValidationError(ValueError):
    pass


class Student:

    def __init__(self, name: str, surname: str, group_number: int,
                 progress: list[int]):
        self.name = name
        self.surname = surname
        self.group_number = group_number
        self.progress = progress
        if not self.is_valid:
            raise ValidationError("Name and surname must be 'str'")

    def __str__(self):
        return f"{self.name} {self.surname}. Group: {self.group_number}"

    def __repr__(self):
        return f"{self.name} {self.surname}. Group: {self.group_number}"

    @property
    def is_valid(self) -> bool:
        if type(self.name) is not str:
            return False
        if type(self.surname) is not str:
            return False
        return True

    @property
    def average_point(self) -> float:
        return round(sum(self.progress) / len(self.progress), 2)

    @property
    def is_best_student(self) -> bool:

        return (
            len(list(filter(lambda x: x == 5 or x == 6, self.progress)))
            ==
            len(self.progress)
        )


class School:

    def __init__(self):
        self.__students_list = []

    def add_student(self, student: Student) -> None:
        self.__students_list.append(student)

    def get_students(self, group_number: int) -> List[Student]:
        return list(filter(lambda x: x.group_number == group_number,
                           self.__students_list))

    def get_best_students(self) -> List[Student]:
        return list(filter(lambda x: x.is_best_student, self.__students_list))

    def get_students_without_exams(self) -> List[Student]:
        return list(filter(lambda x: x.average_point >= 7,
                           self.__students_list))


def get_demo_school() -> School:
    school = School()
    students = [
        ("student", "1", 1, [8, 8, 8, 8, 8]),
        ("student", "2", 1, [5, 5, 5, 6, 5]),
        ("student", "3", 1, [4, 4, 5, 6, 7]),
        ("student", "4", 2, [4, 4, 5, 6, 7]),
        ("student", "5", 2, [4, 4, 5, 6, 7]),
        ("student", "6", 2, [5, 5, 5, 6, 5]),
        ("student", "7", 2, [4, 4, 5, 6, 7]),
        ("student", "8", 3, [4, 4, 5, 6, 7]),
        ("student", "9", 3, [8, 8, 8, 8, 8])
    ]
    for student in students:
        school.add_student(
            Student(*student)
        )
    return school


def main():
    demo_school = get_demo_school()
    group_students = demo_school.get_students(2)
    print("Group students", group_students)

    best_students = demo_school.get_best_students()
    print("Best students", best_students)

    students_without_exams = demo_school.get_students_without_exams()
    print("Students without exams", students_without_exams)

    print("Printing best students surname and group number")
    for student in best_students:
        print(f"Best user surname: {student.surname}")
        print(f"Group number:{student.group_number}")


if __name__ == '__main__':
    main()
