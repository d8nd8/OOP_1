class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

    def rate_lecturer(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in self.courses_in_progress and course in lecturer.courses_attached:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

    def get_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            for grade in grades:
                total_grades.append(grade)
        if total_grades:
            return round(sum(total_grades) / len(total_grades), 1)
        else:
            return 0

    def __str__(self):
        average_grade = self.get_average_grade()
        courses_in_progress_str = ', '.join(self.courses_in_progress)
        finished_courses_str = ', '.join(self.finished_courses)
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за домашние задания: {average_grade}\n"
                f"Курсы в процессе изучения: {courses_in_progress_str}\n"
                f"Завершенные курсы: {finished_courses_str}")

    def __lt__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Student):
            return False
        return self.get_average_grade() == other.get_average_grade()

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []

    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}"

class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}

    def get_average_grade(self):
        total_grades = []
        for grades in self.grades.values():
            for grade in grades:
                total_grades.append(grade)
        if total_grades:
            return round(sum(total_grades) / len(total_grades), 1)
        else:
            return 0

    def __str__(self):
        average_grade = self.get_average_grade()
        return (f"Имя: {self.name}\nФамилия: {self.surname}\n"
                f"Средняя оценка за лекции: {average_grade}")

    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.get_average_grade() < other.get_average_grade()

    def __le__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.get_average_grade() <= other.get_average_grade()

    def __eq__(self, other):
        if not isinstance(other, Lecturer):
            return False
        return self.get_average_grade() == other.get_average_grade()

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# Пример использования:
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['Введение в программирование']

another_student = Student('Jane', 'Doe', 'female')
another_student.courses_in_progress += ['Python']
another_student.finished_courses += ['Введение в программирование']

cool_lecturer = Lecturer('John', 'Smith')
cool_lecturer.courses_attached += ['Python']

another_lecturer = Lecturer('Emily', 'Davis')
another_lecturer.courses_attached += ['Python']

cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

another_reviewer = Reviewer('Ann', 'Brown')
another_reviewer.courses_attached += ['Python']

cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 9)
cool_reviewer.rate_hw(best_student, 'Python', 8)

another_reviewer.rate_hw(another_student, 'Python', 7)
another_reviewer.rate_hw(another_student, 'Python', 6)
another_reviewer.rate_hw(another_student, 'Python', 5)

best_student.rate_lecturer(cool_lecturer, 'Python', 9)
best_student.rate_lecturer(cool_lecturer, 'Python', 8)
best_student.rate_lecturer(cool_lecturer, 'Python', 10)

another_student.rate_lecturer(another_lecturer, 'Python', 7)
another_student.rate_lecturer(another_lecturer, 'Python', 6)
another_student.rate_lecturer(another_lecturer, 'Python', 5)

print(best_student)
print(another_student)
print(cool_lecturer)
print(another_lecturer)
print(cool_reviewer)
print(another_reviewer)
print(best_student > another_student)
print(cool_lecturer < another_lecturer)
