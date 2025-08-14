class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecture(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if grade in range(1, 11):
                if course in lecturer.grades:
                    lecturer.grades[course] += [grade]
                else:
                    lecturer.grades[course] = [grade]
            else:
                return 'Оценка должна быть от 1 до 10'
        else:
            return 'Ошибка'

    def average_rate_student(self):
        all_grades = []
        for subgrades in self.grades.values():
            for grade in subgrades:
                all_grades.append(grade)

        if len(all_grades) > 0:
            return round(sum(all_grades) / len(all_grades), 1)
        else:
            return None # У студента еще нет оценок

    def __lt__(self, other): # пока добавил просто так

        first_student = self.average_rate_student()
        second_student = other.average_rate_student()

        if first_student is None or second_student is None:
            raise ValueError("Сравнение невозможно, так как у одного из студентов нет оценок")

        return first_student < second_student

    def __gt__(self, other):
    # сейчас именно этот метод используется в функциях comperison для студентов и лекторов

        first_student = self.average_rate_student()
        second_student = other.average_rate_student()

        if first_student is None or second_student is None:
            raise ValueError("Сравнение невозможно, так как у одного из студентов нет оценок")

        return first_student > second_student

    def __eq__(self, other): # пока добавил просто так

        first_student = self.average_rate_student()
        second_student = other.average_rate_student()

        if first_student is None or second_student is None:
            raise ValueError("Сравнение невозможно, так как у одного из студентов нет оценок")

        return first_student == second_student

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за домашнее задание: {self.average_rate_student()} \n\
Курсы в процессе обучения: {", ".join(self.courses_in_progress)} \n\
Завершенные курсы: {", ".join(self.finished_courses)}\n'

def comparison_students(student1, student2):
    try:
        comparison = student1 > student2
        if comparison:
            print('Верно')
        else:
            print('Неверно')
    except ValueError as e:
        print(e)

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []
        self.grades = {}

    def average_rate_lecture(self):
        all_grades = []
        for subgrades in self.grades.values():
            for grade in subgrades:
                all_grades.append(grade)

        if len(all_grades) > 0:
            return round(sum(all_grades) / len(all_grades), 1)
        else:
            return None # У лектора еще нет оценок

    def __lt__(self, other): # пока добавил просто так

        first_lecturer = self.average_rate_lecture()
        second_lecturer = other.average_rate_lecture()

        if first_lecturer is None or second_lecturer is None:
            raise ValueError("Сравнение невозможно, так как у одного из лекторов нет оценок")

        return first_lecturer < second_lecturer

    def __gt__(self, other):
    # сейчас именно этот метод используется в функциях comperison для студентов и лекторов

        first_lecturer = self.average_rate_lecture()
        second_lecturer = other.average_rate_lecture()

        if first_lecturer is None or second_lecturer is None:
            raise ValueError("Сравнение невозможно, так как у одного из лекторов нет оценок")

        return first_lecturer > second_lecturer

    def __eq__(self, other): # пока добавил просто так

        first_lecturer = self.average_rate_lecture()
        second_lecturer = other.average_rate_lecture()

        if first_lecturer is None or second_lecturer is None:
            raise ValueError("Сравнение невозможно, так как у одного из лекторов нет оценок")

        return first_lecturer == second_lecturer

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n\
Средняя оценка за лекции: {self.average_rate_lecture()}\n'

def comparison_lecturers(lecturer1, lecturer2):
    try:
        comparison = lecturer1 > lecturer2
        if comparison:
            print('Верно')
        else:
            print('Неверно')
    except ValueError as e:
        print(e)

class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.courses_attached = []


    def rate_student(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if grade in range(1, 11):
                if course in student.grades.keys():
                    student.grades[course] += [grade]
                else:
                    student.grades[course] = [grade]
            else:
                return 'Оценка студента должна быть от 1 до 10'
        else:
            return 'Ошибка'

    def __str__(self):
        return f'Имя: {self.name}\nФамилия: {self.surname}\n'

# наполнение для проверки работоспособности кода к заданию №1

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
print(isinstance(lecturer, Mentor)) # True
print(isinstance(reviewer, Mentor)) # True
print(lecturer.courses_attached)    # []
print(reviewer.courses_attached)    # []

# наполнение для проверки работоспособности кода к заданию №2

lecturer = Lecturer('Иван', 'Иванов')
reviewer = Reviewer('Пётр', 'Петров')
student = Student('Алёхина', 'Ольга', 'Ж')

student.courses_in_progress += ['Python', 'Java']
lecturer.courses_attached += ['Python', 'C++']
reviewer.courses_attached += ['Python', 'C++']

print(student.rate_lecture(lecturer, 'Python', 7))  # None
print(student.rate_lecture(lecturer, 'Java', 8))  # Ошибка
print(student.rate_lecture(lecturer, 'С++', 8))  # Ошибка
print(student.rate_lecture(reviewer, 'Python', 6))  # Ошибка
print(lecturer.grades)  # {'Python': [7]}

# наполнение для проверки работоспособности кода к заданию №3

some_student = Student('Ruoy', 'Eman', 'F')
some_student.courses_in_progress += ['Python', 'Git']
some_lecturer = Lecturer('Some', 'Buddy')
some_lecturer.courses_attached += ['Python', 'Git']
some_reviewer = Reviewer('Some', 'Buddy')
some_reviewer.courses_attached += ['Python', 'Git']
print(some_reviewer)

some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Python', 10)
some_student.rate_lecture(some_lecturer, 'Git', 9)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)
some_student.rate_lecture(some_lecturer, 'Git', 10)
print(some_lecturer)

some_student.finished_courses += ['Введение в программирование']
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer.rate_student(some_student, 'Python', 9)
some_reviewer.rate_student(some_student, 'Python', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
some_reviewer.rate_student(some_student, 'Git', 10)
print(some_student)

some_reviewer.rate_student(student, 'Python', 10)
some_reviewer.rate_student(student, 'Python', 10)
some_reviewer.rate_student(student, 'Python', 10)

some_student.rate_lecture(lecturer, 'Python', 7)
some_student.rate_lecture(lecturer, 'Python', 7)
some_student.rate_lecture(lecturer, 'Python', 7)

comparison_students(student, some_student)
comparison_lecturers(lecturer, some_lecturer)