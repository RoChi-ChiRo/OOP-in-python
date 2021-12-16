def average_in_dict(grades):
    if grades:
        summary = length = 0
        for course in grades:
            summary += sum(grades[course])
            length += len(grades[course])
        return str(round(summary / length, 3))
    else:
        print('Оценок нет')


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def __str__(self):
        result = str()
        result += f'Имя: {self.name}'
        result += f'\nФамилимя: {self.surname}'
        result += f'\nСредняя оценка за домашнее задание {average_in_dict(self.grades)}'

        result += f'\nКурсы в процессе изучения: '
        if self.courses_in_progress:
            for course in self.courses_in_progress:
                result += course + ', '
            result = result[0:-2]
        else:
            result += 'не найдено'

        result += f'\nЗвершённые курсы: '
        if self.finished_courses:
            for course in self.finished_courses:
                result += course + ', '
            result = result[0:-2]
        else:
            result += 'не найдено'

        return result

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

    def __str__(self):
        res = 'Имя: ' + self.name
        res += '\nФамилия: ' + self.surname
        res += '\nСредняя оценка за лекции: ' + average_in_dict(self.grades)
        return res


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Имя: {self.name} \nФамилия: {self.surname}'

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
    lecturer1 = Lecturer('L1', '1')
    lecturer2 = Lecturer('L2', '2')
    reviewer1 = Reviewer('R1', '1')
    reviewer2 = Reviewer('R2', '2')

    # courses
    student1.finished_courses += ['w']
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

    reviewer1.rate_hw(student1, 'q', 2)
    reviewer1.rate_hw(student2, 'q', 2)
    reviewer2.rate_hw(student1, 'w', 4)
    reviewer2.rate_hw(student1, 'q', 3)
    reviewer2.rate_hw(student2, 'w', 4)

    # print
    print(f'1 lecturer grades: {lecturer1.grades}')
    print(f'1 student  grades: {student1.grades}')
    print(f'2 lecturer grades: {lecturer2.grades}')
    print(f'2 student  grades: {student2.grades}')

    print('---')
    print(student1)
    print(student2)
    print('---')
    print(lecturer1)
    print(lecturer2)
    print('---')
    print(reviewer1)
    print(reviewer2)
