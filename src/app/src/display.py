import random
import time
from typing import List

import streamlit as st


def display_selected_candidates(candidates: List[str]):
    """
    Displays the selected candidates in a styled format, consistent with the app's color palette.
    """
    if candidates:
        st.markdown(
            "<h3 style='color:#8be9fd;'>🎉 Final Selection:</h3>",  # Cyan title for consistency
            unsafe_allow_html=True,
        )
        candidate_blocks = ""
        for candidate in candidates:
            candidate_blocks += f"""
            <div style="
                display: inline-block;
                margin: 10px;
                padding: 15px 25px;
                border: 2px solid #50fa7b; /* Vibrant green border */
                border-radius: 10px; /* Rounded corners for modern look */
                font-size: 18px;
                font-weight: bold;
                color: #ffffff; /* White text for contrast */
                background-color: #44475a; /* Dark gray-blue background */
                text-align: center;
                box-shadow: 2px 2px 10px rgba(80, 250, 123, 0.4); /* Subtle green glow */
                ">
                {candidate}
            </div>
            """
        st.markdown(candidate_blocks, unsafe_allow_html=True)
    else:
        st.warning("No candidates selected.")


def simulate_spinner(available_students, spin_duration=2, spin_interval=0.1):
    """
    Simulates a spinner effect by displaying random student names.
    """
    display_placeholder = st.empty()
    end_time = time.time() + spin_duration
    while time.time() < end_time:
        random_student = random.choice(available_students)
        display_placeholder.markdown(
            f"<h2 style='color:#FFD700;'>🥁 {random_student} 🥁</h2>",
            unsafe_allow_html=True,
        )
        time.sleep(spin_interval)
    display_placeholder.empty()


def set_custom_css():
    """
    Applies custom CSS for styling buttons and elements with an improved color palette.
    """
    st.markdown(
        """
        <style>
            /* General button styling */
            .stButton > button {
                color: #FFFFFF; /* White text */
                background-color: #44475a; /* Dark gray-blue for neutral base */
                border: 2px solid #8be9fd; /* Soft cyan border */
                border-radius: 10px; /* Rounded corners for modern look */
                font-size: 18px;
                font-weight: bold;
                padding: 12px 25px;
                margin: 10px 0;
                transition: background-color 0.3s ease, color 0.3s ease;
                box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.4); /* Subtle shadow */
            }
            
            /* Highlight effect for "Choose Random Students" button */
            .stButton > button:focus {
                background-color: #8be9fd; /* Cyan for attention */
                color: #282a36; /* Dark text for contrast */
                box-shadow: 0px 0px 15px rgba(139, 233, 253, 0.8); /* Glowing effect */
            }

            /* Hover effect for all buttons */
            .stButton > button:hover {
                background-color: #50fa7b; /* Vibrant green on hover */
                color: #282a36; /* Dark text for contrast */
            }

            /* Styling for reset icon */
            .stButton > button[key="reset_button"] {
                background-color: #282a36; /* Dark gray for subtlety */
                color: #ff79c6; /* Bright pink text/icon */
                border: none;
                border-radius: 50%; /* Circular shape */
                font-size: 22px;
                padding: 10px;
                margin: 10px;
                transition: background-color 0.3s ease, color 0.3s ease;
            }
            
            .stButton > button[key="reset_button"]:hover {
                background-color: #44475a; /* Slight gray highlight */
                color: #ff92df; /* Softer pink on hover */
            }
        </style>
        """,
        unsafe_allow_html=True,
    )
