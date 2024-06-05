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

class Reviewer(Mentor):
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

