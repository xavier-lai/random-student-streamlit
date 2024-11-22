import streamlit as st

from .constants import STUDENTS_CONFIG


def get_input_fields():
    """
    Renders the user input fields and returns the selected inputs.
    """
    number_of_students = st.number_input(
        "Number of students to choose", min_value=1, value=1
    )
    student_group_to_exclude_input = st.selectbox(
        "Group to exclude for selection",
        options=[""] + list(STUDENTS_CONFIG.keys()),
        index=0,
    )
    student_group_to_exclude = (
        None if student_group_to_exclude_input == "" else student_group_to_exclude_input
    )
    return number_of_students, student_group_to_exclude
