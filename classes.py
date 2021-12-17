def average_in_dict(grades):
    if grades:
        summary = length = 0
        for course in grades:
            summary += sum(grades[course])
            length += len(grades[course])
        return str(round(summary / length, 3))
    else:
        print('Оценок нет')


def average_in_students_list(students, course):
    result = length = 0
    for student in students:
        if isinstance(student, Student):
            if course in student.finished_courses or course in student.courses_in_progress:
                result += sum(student.grades[course])
                length += len(student.grades[course])
        else:
            print(f'skip element {students.index(student)} in list')
    return result / length


def average_in_lecturers_list(lecturers, course):
    result = length = 0
    for lecturer in lecturers:
        if isinstance(lecturer, Lecturer):
            if course in lecturer.courses_attached:
                result += sum(lecturer.grades[course])
                length += len(lecturer.grades[course])
        else:
            print(f'skip element {lecturers.index(student)} in list')
    return result / length


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

    def __lt__(self, other):
        if isinstance(other, Student):
            if average_in_dict(self.grades) < average_in_dict(other.grades):
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, Student):
            if average_in_dict(self.grades) <= average_in_dict(other.grades):
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, Student):
            if average_in_dict(self.grades) == average_in_dict(other.grades):
                return True
            else:
                return False

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

    def __lt__(self, other):
        if isinstance(other, Lecturer):
            if average_in_dict(self.grades) < average_in_dict(other.grades):
                return True
            else:
                return False

    def __le__(self, other):
        if isinstance(other, Lecturer):
            if average_in_dict(self.grades) <= average_in_dict(other.grades):
                return True
            else:
                return False

    def __eq__(self, other):
        if isinstance(other, Lecturer):
            if average_in_dict(self.grades) == average_in_dict(other.grades):
                return True
            else:
                return False


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
