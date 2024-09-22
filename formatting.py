import time
import streamlit as st
from PIL import Image
from streamlit_extras.add_vertical_space import add_vertical_space

if "my_bar" not in st.session_state:
    st.session_state["my_bar"] = None


def resize_image(scale_factor, posix_path):
    # open image
    image = Image.open(posix_path)
    # Calculate new size maintaining aspect ratio
    new_size = (
        int(image.width * scale_factor),
        int(image.height * scale_factor)
    )
    # Resize the image
    resized_img = image.resize(new_size, Image.Resampling.LANCZOS)
    return resized_img


def display_progress():
    if "progress" not in st.session_state:
        st.session_state["progress"] = 0
    total_steps = 35  # Adjust this value as needed
    progress_percent = min((st.session_state["progress"] * 100) // total_steps, 100)
    # Display progress bar
    progress_text = f"{progress_percent}% completion"
    st.session_state["my_bar"] = st.progress(progress_percent, text=progress_text)
    time.sleep(0.2)  # Simulate a delay
    st.session_state["my_bar"].progress(progress_percent, text=progress_text)
    add_vertical_space(1)


def update_progress(added_portion=0):
    st.session_state["progress"] += added_portion


def write_footer_hide_menu():
    st.markdown(
        """
        <style>
            footer {
                position: absolute;
                float: right;
                left: 0;
                bottom: 0;
                width: 100%;
                height: 18%;
                background-color: #f5f5f5;
                color: #666;
                text-align: right;
                padding: 30px;
                font-size: 16px;
            }
           
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="footer"><a href="https://gif-selector.informatik.uni-bremen.de/Goodbye">Imprint</a> | <a '
        'href="https://www.uni-bremen.de/en/data-privacy">Privacy Policy</a></div>',
        unsafe_allow_html=True
    )
    st.markdown(""" <style>
    #MainMenu {visibility: hidden;}
    </style> """, unsafe_allow_html=True)
    st.markdown("""
        <style>
            div[data-testid="stSidebar"] {visibility: hidden;}

            section[data-testid="stSidebar"][aria-expanded="true"]{
                display: none;
            }

            div[data-testid="collapsedControl"]{
                display: none;
            }
            """ div[data-testid="InputInstructions"]{
                display: none;
            }
            div[data-testid="stToolbar"]{
                display: none;
            } """
        </style>
        """, unsafe_allow_html=True)
    hide_img_fs = '''
        <style>
        button[title="View fullscreen"]{
            visibility: hidden;}
        </style>
        '''

    st.markdown(hide_img_fs, unsafe_allow_html=True)
    # hides the first option in a radio group
    # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
    st.markdown(
        """ <style>
                div[role="radiogroup"] >  :first-child{
                    display: none !important;
                }
            </style>
            """,
        unsafe_allow_html=True
    )
    return ""


# def format_sidebar_intro():
#     no_sidebar_style = """
#             <style>
#                 div[data-testid="stSidebarNav"] {display: none;}
#             </style>
#         """
#     st.markdown(no_sidebar_style, unsafe_allow_html=True)
#
#     # hides button to close sidebar, open settings
#     no_button_style = """
#             <style>
#                 button[kind="header"] {display:none;}
#             </style>
#         """
#     st.markdown(no_button_style, unsafe_allow_html=True)
#     num_users = display_num_participants()
#     with st.sidebar:
#         add_vertical_space(8)
#         pages = """
#             ### <span style="color: #F4AA08">Introduction</span>
#
#             ### GIF Evaluation
#
#             ### Questionnaire
#
#             ### Goodbye
#             """
#         st.markdown(pages, unsafe_allow_html=True)
#         add_vertical_space(3)
#         # add content to show number of prompts
#         st.write(f"Number of participants: {num_users}")


# def format_sidebar_goodbye():
#     no_sidebar_style = """
#             <style>
#                 div[data-testid="stSidebarNav"] {display: none;}
#             </style>
#         """
#     st.markdown(no_sidebar_style, unsafe_allow_html=True)
#
#     # hides button to close sidebar, open settings
#     no_button_style = """
#             <style>
#                 button[kind="header"] {display:none;}
#             </style>
#         """
#     st.markdown(no_button_style, unsafe_allow_html=True)
#
#     num_users = display_num_participants()
#     with st.sidebar:
#         add_vertical_space(8)
#         pages = """
#             ### Introduction
#
#             ### GIF Evaluation
#
#             ### Questionnaire
#
#             ### <span style="color: #F4AA08">Goodbye</span>
#             """
#         st.markdown(pages, unsafe_allow_html=True)
#         add_vertical_space(3)
#         # add content to show number of prompts
#         st.write(f"Number of participants: {num_users}")


# def format_sidebar_radio_eval():
#     no_sidebar_style = """
#                 <style>
#                     div[data-testid="stSidebarNav"] {display: none;}
#                 </style>
#             """
#     st.markdown(no_sidebar_style, unsafe_allow_html=True)
#
#     # hides button to close sidebar, open settings
#     no_button_style = """
#                 <style>
#                     button[kind="header"] {display:none;}
#                 </style>
#             """
#     st.markdown(no_button_style, unsafe_allow_html=True)
#     # hides the first option in a radio group
#     # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
#     st.markdown(
#         """ <style>
#                 div[role="radiogroup"] >  :first-child{
#                     display: none !important;
#                 }
#             </style>
#             """,
#         unsafe_allow_html=True
#     )
#
#     num_users = display_num_participants()
#     with st.sidebar:
#         add_vertical_space(8)
#         pages = """
#                         ### Introduction
#
#                         ### <span style="color: #F4AA08">GIF Evaluation</span>
#
#                         ### Questionnaire
#
#                         ### Goodbye
#                         """
#         st.markdown(pages, unsafe_allow_html=True)
#         add_vertical_space(3)
#         # add content to show number of prompts
#         st.write(f"Number of participants: {num_users}")


# def format_sidebar_radio_question():
#     no_sidebar_style = """
#                 <style>
#                     div[data-testid="stSidebarNav"] {display: none;}
#                 </style>
#             """
#     st.markdown(no_sidebar_style, unsafe_allow_html=True)
#
#     # hides button to close sidebar, open settings
#     no_button_style = """
#                 <style>
#                     button[kind="header"] {display:none;}
#                 </style>
#             """
#     st.markdown(no_button_style, unsafe_allow_html=True)
#     # hides the first option in a radio group
#     # note: this applies to ALL radio groups across the app; it cannot be done for an individual button!
#     st.markdown(
#         """ <style>
#                 div[role="radiogroup"] >  :first-child{
#                     display: none !important;
#                 }
#             </style>
#             """,
#         unsafe_allow_html=True
#     )
#
#     num_users = display_num_participants()
#     with st.sidebar:
#         add_vertical_space(8)
#         pages = """
#                         ### Introduction
#
#                         ### GIF Evaluation
#
#                         ### <span style="color: #F4AA08">Questionnaire</span>
#
#                         ### Goodbye
#                         """
#         st.markdown(pages, unsafe_allow_html=True)
#         add_vertical_space(3)
#         # add content to show number of prompts
#         st.write(f"Number of participants: {num_users}")
#     return ""
