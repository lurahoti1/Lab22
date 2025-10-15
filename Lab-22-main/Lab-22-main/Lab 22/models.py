import dataclasses

@dataclasses.dataclass
class Teacher:
    id: int
    full_name: str
    email: str

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("ID e mësuesit duhet të jetë numër pozitiv.")
        if "@" not in self.email or "." not in self.email.split('@')[1]:
            raise ValueError(f"Formati i email-it '{self.email}' është i pavlefshëm.")

@dataclasses.dataclass
class Student:
    id: int
    full_name: str
    grade: int

    def __post_init__(self):
        if self.id <= 0:
            raise ValueError("ID e studentit duhet të jetë numër pozitiv.")
        if not 10 <= self.grade <= 12:
            raise ValueError(f"Klasa e studentit duhet të jetë ndërmjet 10 dhe 12, por është {self.grade}.")

class Course:
    def __init__(self, code: str, title: str, capacity: int, teacher: Teacher):
        if not title:
            raise ValueError("Titulli i kursit nuk mund të jetë bosh.")
        if capacity < 1:
            raise ValueError(f"Kapaciteti i kursit duhet të jetë të paktën 1, por është {capacity}.")
        
        self.code = code
        self.title = title
        self.capacity = capacity
        self.teacher = teacher
        self.students: list[Student] = []

    def is_full(self) -> bool:
        """Checks if the course has reached its capacity."""
        return len(self.students) >= self.capacity

    def add_student(self, student: Student):
        """Adds a student to the course if it is not full and the student is not already enrolled."""
        if self.is_full():
            print(f"GABIM: Kursi '{self.title}' është plot. Nuk mund të shtohet studenti '{student.full_name}'.")
            return
        if student in self.students:
            print(f"INFO: Studenti '{student.full_name}' është tashmë i regjistruar në kursin '{self.title}'.")
            return
            
        self.students.append(student)
        print(f"SUKSES: Studenti '{student.full_name}' u shtua në kursin '{self.title}'.")

    def remove_student(self, student: Student):
        """Removes a student from the course."""
        if student in self.students:
            self.students.remove(student)

    def __str__(self) -> str:
        """Returns a string representation of the course."""
        return (
            f"Course[{self.code}] {self.title} ({len(self.students)}/{self.capacity}) — "
            f"Teacher: {self.teacher.full_name}"
        )

# Shembull I/O
if __name__ == "__main__":
    try:
        t = Teacher(1, "Ardit Kola", "ardit.kola@shkolla.al")
        c = Course("PY101", "Python Bazë", 2, t)
        s1 = Student(10, "Elira Deda", 12)
        s2 = Student(11, "Klodian Meta", 11)
        s3 = Student(12, "Ana Koci", 10) # Student shtesë për testim

        print(f"Is course '{c.title}' full? {c.is_full()}")  # False

        print("\nAdding students...")
        c.add_student(s1)
        c.add_student(s2)

        print(f"Is course '{c.title}' full? {c.is_full()}")  # True
        print(c)

        print("\nTrying to add another student to a full course...")
        c.add_student(s3) # Mesazhi i gabimit do të printohet

        print("\nRemoving a student...")
        c.remove_student(s1)
        print(f"Is course '{c.title}' full? {c.is_full()}") # False
        print(c)

    except ValueError as e:
        print(f"Error: {e}")