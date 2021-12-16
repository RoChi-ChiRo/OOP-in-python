class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, grade):
        if isinstance(lecturer, Lecturer):
            for course in self.courses_in_progress:
                if course in lecturer.grades:
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
        if isinstance(student, Student) and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка class Student'


if __name__ == '__main__':
    # init
    student1 = Student('A', 'AA', 'AAA')
    student2 = Student('B', 'BB', 'BBB')
    lecturer1 = Lecturer('L', '1')
    lecturer2 = Lecturer('L', '2')
    reviewer1 = Reviewer('R', '1')
    reviewer2 = Reviewer('R', '2')

    # courses
    student1.courses_in_progress += ['q']
    student2.courses_in_progress += ['w']

    lecturer1.courses_attached += ['q']
    lecturer1.courses_attached += ['w']
    lecturer2.courses_attached += ['w']

    reviewer1.courses_attached += ['q']
    reviewer2.courses_attached += ['w']

    # rates
    student1.rate_lecturer(lecturer1, 1)
    student1.rate_lecturer(lecturer2, 1)
    student2.rate_lecturer(lecturer1, 2)
    student2.rate_lecturer(lecturer2, 2)

    reviewer1.rate_hw(student1, 'p', 2)
    reviewer1.rate_hw(student2, 'p', 2)
    reviewer2.rate_hw(student1, 'p', 4)
    reviewer2.rate_hw(student2, 'p', 4)

    # print
    print(f'1 lecturer grades: {lecturer1.grades}')
    print(f'1 student  grades: {student1.grades}')
    print(f'2 lecturer grades: {lecturer2.grades}')
    print(f'2 student  grades: {student2.grades}')
