class Group:
    def __init__(self, students=None):
        if students is None:
            self.students = []
        else:
            self.students = students

    def add_student(self, student):
        self.students.append(student)

    def remove_student(self, student):
        if student in self.students:
            self.students.remove(student)

    def find_a_student(self, surname):
        for student in self.students:
            if student == surname:
                return f'{student}\n'

    def __str__(self):
        return "\n".join(self.students) + '\n'