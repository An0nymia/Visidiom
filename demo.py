import pandas as pd
import numpy as np
import streamlit as st
from pathlib import Path
from streamlit_extras.add_vertical_space import add_vertical_space
from formatting import hide_menu


st.set_page_config(
    page_title="Visual Idioms: Exhibition",
    layout="wide",
    page_icon="🖼️",
)

# initialise session states
if "literal" not in st.session_state:
    st.session_state["literal"] = 0
if "idiomatic" not in st.session_state:
    st.session_state["idiomatic"] = 0
if "all_ids" not in st.session_state:
    st.session_state["all_ids"] = []
if "posix_path" not in st.session_state:
    st.session_state["posix_path"] = ""
if "idiom_idx" not in st.session_state:
    st.session_state["idiom_idx"] = ""


def display_intro():
    st.title("Exhibition: Visualised Idioms")
    st.write("Add some info on work and reference to paper")
    add_vertical_space(3)

def find_closest_match(df, slider1_value, slider2_value):
    # Calculate the Euclidean distance between the slider values and the DataFrame values
    df['distance'] = np.sqrt((df['count_literal'] - slider1_value) ** 2 + (df['rating_idiom'] - slider2_value) ** 2)

    # Find the index of the minimum distance
    closest_index = df['distance'].idxmin()
    st.session_state["idiom_idx"] = df.loc[closest_index]["idiom"]

    # Return the corresponding row
    return df.loc[closest_index]["image_ids"]


def update_image(slider1_value, slider2_value, df_path, abs_path):
    df = pd.read_csv(df_path)
    df = df.drop_duplicates()
    id_select = find_closest_match(df, slider1_value, slider2_value)
    id_split= str(id_select).split("_")
    dir_id = "_".join(id_split[0:2])
    file_id = "_".join(id_split[2:])
    current_path = f"{abs_path}\\{dir_id}\\{file_id}"
    st.session_state["posix_path"] = Path(current_path).as_posix()
    st.image(st.session_state["posix_path"], use_column_width="auto")




def select_vals_display(df_path, abs_path):
    col1, col2, col3= st.columns(3, gap="small")
    with col1:
        st.markdown("<p style='font-size: 18px;'><b>Number of literal elements in image</b></p>",
                    unsafe_allow_html=True)
        add_vertical_space(2)
        st.slider(label="", min_value=0, max_value=10, key="literal")
        add_vertical_space(3)
        st.markdown("<p style='font-size: 18px;'><b>Idiomatic meaning in image</b></p>",
                    unsafe_allow_html=True)
        add_vertical_space(2)
        st.select_slider(label="example",options=[round(x * 0.1, 2) for x in range(0, 101)], key="idiomatic",
         label_visibility="hidden", format_func=lambda x: '0' if x == 0 else '10' if x == 10 else x)
    with col2:
        pass
    with col3:
        update_image(st.session_state["literal"], st.session_state["idiomatic"], df_path, abs_path)
        st.markdown(f"<p style='font-size: 13px;'>Image generated for the idiom <i>{st.session_state['idiom_idx']}</i></p>",
            unsafe_allow_html=True)

        
        



def main():
    display_intro()
    hide_menu()
    select_vals_display("data/ratings_dummy.csv",
                        "data/gen_resized")

main()