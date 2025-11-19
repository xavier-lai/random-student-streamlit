import os

STUDENTS_CONFIG = {
    1: os.getenv("STUDENT_NAMES_GROUP_1", "").split(","),
    2: os.getenv("STUDENT_NAMES_GROUP_2", "").split(","),
    3: os.getenv("STUDENT_NAMES_GROUP_3", "").split(","),
    4: os.getenv("STUDENT_NAMES_GROUP_4", "").split(","),
    5: os.getenv("STUDENT_NAMES_GROUP_5", "").split(","),
}
