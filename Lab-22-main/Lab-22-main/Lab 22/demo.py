from models import Teacher, Student, Course

def create_dataset():
    """Creates a sample dataset of teachers, students, and courses."""
    # 1. Krijo dataset testimi
    # Mësuesit
    t1 = Teacher(1, "Ardit Kola", "ardit.kola@shkolla.al")
    t2 = Teacher(2, "Elona Hoxha", "elona.hoxha@shkolla.al")
    teachers = [t1, t2]

    # Studentët
    s1 = Student(10, "Elira Deda", 12)
    s2 = Student(11, "Klodian Meta", 11)
    s3 = Student(12, "Ardi Leka", 10)
    s4 = Student(13, "Besa Tola", 12)
    s5 = Student(14, "Genti Pano", 11)
    s6 = Student(15, "Drita Vogli", 10)
    students = [s1, s2, s3, s4, s5, s6]

    # Kurset
    c1 = Course("PY101", "Python Bazë", 2, t1)
    c2 = Course("DB102", "Baza të të Dhënave", 3, t1)
    c3 = Course("WD103", "Web Development", 4, t2)
    courses = [c1, c2, c3]

    # 2. Regjistro studentët në kurse
    c1.add_student(s1)
    c1.add_student(s2)
    
    # Test tejkalimi kapaciteti
    print("--- Duke testuar tejkalimin e kapacitetit ---")
    c1.add_student(s3) 
    print("----------------------------------------\n")

    c2.add_student(s3)
    c2.add_student(s4)

    c3.add_student(s5)
    
    # Test regjistrimi i dyfishtë
    print("\n--- Duke testuar regjistrimin e dyfishtë ---")
    c2.add_student(s4)
    print("----------------------------------------\n")


    return teachers, students, courses

def test_edge_cases():
    """Tests validation and error handling for edge cases."""
    print("--- TESTIMI I RASTEVE KUFITARE ---")
    try:
        # Email i pavlefshshëm
        Teacher(99, "Test Teacher", "test.email.com")
    except ValueError as e:
        print(f"Test 1/3 (Email pa @): OK - {e}")

    try:
        # Kapacitet zero
        t = Teacher(1, "Ardit Kola", "ardit.kola@shkolla.al")
        Course("FAIL101", "Kurs i dështuar", 0, t)
    except ValueError as e:
        print(f"Test 2/3 (Kapacitet=0): OK - {e}")

    try:
        # Klasë e pavlefshme
        Student(99, "Test Student", 13)
    except ValueError as e:
        print(f"Test 3/3 (Klasë > 12): OK - {e}")
    print("------------------------------------\n")


def print_reports(teachers, students, courses):
    """Prints all the required reports."""
    
    # 3. Raporti R1: Për çdo kurs
    print("--- RAPORTI I KURSEVE ---")
    for course in courses:
        student_names = ", ".join([s.full_name for s in course.students])
        if not student_names:
            student_names = "Asnjë student i regjistruar"
        print(
            f'- {course.code} "{course.title}" — {len(course.students)}/{course.capacity} studentë: {student_names}'
        )
    print("\n" + "="*30 + "\n")

    # 4. Raporti R2: Për çdo mësues
    print("--- RAPORTI I MËSUESVE ---")
    for teacher in teachers:
        taught_courses = [c.code for c in courses if c.teacher == teacher]
        print(f"- {teacher.full_name}: {', '.join(taught_courses)}")
    print("\n" + "="*30 + "\n")

    # 5. Raporti R3: Kursi me më shumë/pak regjistrime
    if not courses:
        print("Nuk ka kurse për të analizuar.")
        return
        
    max_course = min_course = courses[0]
    for course in courses[1:]:
        if len(course.students) > len(max_course.students):
            max_course = course
        if len(course.students) < len(min_course.students):
            min_course = course
            
    print("--- MAKS/MIN REGJISTRIME ---")
    print(f"- Max: {max_course.code} ({len(max_course.students)})")
    print(f"- Min: {min_course.code} ({len(min_course.students)})")
    print("\n" + "="*30 + "\n")


# Funksione ndihmëse (opsionale)
def find_student_by_name(students, query):
    """Finds students whose full name contains the query string."""
    return [s for s in students if query.lower() in s.full_name.lower()]

def courses_for_student(student, all_courses):
    """Returns a list of courses a student is enrolled in."""
    return [c for c in all_courses if student in c.students]


if __name__ == "__main__":
    # Testo rastet kufitare fillimisht
    test_edge_cases()

    # Krijo dataset-in dhe printo raportet
    teachers_data, students_data, courses_data = create_dataset()
    print_reports(teachers_data, students_data, courses_data)

    # Testimi i funksioneve ndihmëse
    print("--- TESTIMI I FUNKSIONEVE NDIHMËSE ---")
    student_to_find = students_data[2] # Ardi Leka
    student_courses = courses_for_student(student_to_find, courses_data)
    course_codes = [c.code for c in student_courses]
    print(f"Studenti '{student_to_find.full_name}' është regjistruar në kurset: {', '.join(course_codes)}")

    found = find_student_by_name(students_data, "deda")
    if found:
        print(f"Gjetur student me 'deda': {found[0].full_name}")
    print("----------------------------------------")