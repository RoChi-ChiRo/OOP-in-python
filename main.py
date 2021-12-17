from classes import *

if __name__ == '__main__':
    # init
    students_list = [student1, student2] = [Student('A', 'AA', 'AAA'), Student('B', 'BB', 'BBB')]
    lecturers_list = [lecturer1, lecturer2] = [Lecturer('L1', '1'), Lecturer('L2', '2')]
    reviewers_list = [reviewer1, reviewer2] = [Reviewer('R1', '1'), Reviewer('R2', '2')]

    # courses
    student1.finished_courses += ['Python']
    student1.courses_in_progress += ['Not python']

    student2.courses_in_progress += ['Not python']

    #
    lecturer1.courses_attached += ['Python']
    lecturer1.courses_attached += ['Not python']

    lecturer2.courses_attached += ['Not python']

    #
    reviewer1.courses_attached += ['Python']

    reviewer2.courses_attached += ['Not python']

    # rates
    student1.rate_lecturer(lecturer1, 1)
    student1.rate_lecturer(lecturer2, 3)

    student2.rate_lecturer(lecturer1, 2)
    student2.rate_lecturer(lecturer2, 3)

    #
    reviewer1.rate_hw(student1, 'Python', 2)
    reviewer1.rate_hw(student2, 'Python', 2)

    reviewer2.rate_hw(student1, 'Not python', 3)
    reviewer2.rate_hw(student1, 'Python', 4)
    reviewer2.rate_hw(student2, 'Not python', 4)

    # print
    print('--students--')
    for student in students_list:
        print(student)
        print()

    print('--lecturers--')
    for lecturer in lecturers_list:
        print(lecturer)
        print()

    print('--reviewers--')
    for reviewer in reviewers_list:
        print(reviewer)
        print()

    print('--lt--')
    print(lecturer1 <= lecturer2)
    print(student1 == student1, student1 < student2)
    print()

    print('--average__')
    x=0
    for student in students_list:
        print(x, 'stud: ', student.grades)
        x+=1
    print(average_in_students_list(students_list, 'Not python'))
    print()

    x=0
    for lecturer in lecturers_list:
        print(x, 'lect: ', lecturer.grades)
        x+=1
    print(average_in_lecturers_list(lecturers_list, 'Not python'))
