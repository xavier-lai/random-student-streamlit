import streamlit as st

from src.constants import STUDENTS_CONFIG
from src.display import display_selected_candidates, set_custom_css, simulate_spinner
from src.inputs import get_input_fields
from src.random import get_random_student


def reset_selected_students():
    """
    Resets the selected students in session state.
    """
    st.session_state["selected_students"] = set()
    st.success("Selected students reset successfully!")


def main():
    """
    Main function that runs the Streamlit app.
    """

    set_custom_css()

    # App title
    st.write("# 🎲 Pick Your Students")

    # Get input fields
    number_of_students, student_group_to_exclude = get_input_fields()

    # Initialize session state
    if "selected_students" not in st.session_state:
        st.session_state["selected_students"] = set()

    # Main button to choose random students
    if st.button("Choose Random Students"):
        try:
            # Gather available students
            available_students = [
                student
                for group, students in STUDENTS_CONFIG.items()
                if group != student_group_to_exclude
                for student in students
            ]

            # Simulate spinner
            simulate_spinner(available_students)

            # Get the final selection of students
            chosen_students = get_random_student(
                number_of_students,
                student_group_to_exclude,
                selected_students=st.session_state["selected_students"],
            )

            # Display the final selection
            display_selected_candidates(chosen_students)

        except ValueError as e:
            st.error(str(e))

    # Reset button as a small icon
    if st.button("🔄", key="reset_button"):
        reset_selected_students()


if __name__ == "__main__":
    main()
