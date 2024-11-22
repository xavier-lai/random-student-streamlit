import random
from typing import List, Optional

from .constants import STUDENTS_CONFIG


def get_random_student(
    number_of_students: int,
    student_group: Optional[str],
    selected_students: set,
    reset: bool = False,
) -> List[str]:
    if reset:
        selected_students.clear()

    available_students = [
        student
        for group, students in STUDENTS_CONFIG.items()
        if group != student_group
        for student in students
        if student not in selected_students
    ]

    if number_of_students > len(available_students):
        raise ValueError("Number of students to choose exceeds available students")

    chosen_students = random.sample(available_students, k=number_of_students)

    selected_students.update(chosen_students)

    return chosen_students
