class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in (self.finished_courses or self.courses_in_progress):
            if course in lecturer.grades.keys():
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка class Lecturer'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = dict()


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and \
                course in self.courses_attached and \
                course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка class Student'


if __name__ == '__main__':
    student = Student('Vasya', 'Pupkin', True)
    lecturer = Lecturer('Misha', 'Ponovoy')
    reviewer = Reviewer('Kesha', 'Veseliy')

    student.courses_in_progress += ['p']
    lecturer.courses_attached += ['p']
    student.rate_lecturer(lecturer, 'p', 3)
    student.rate_lecturer(lecturer, 'p', 5)

    print(lecturer.grades)
