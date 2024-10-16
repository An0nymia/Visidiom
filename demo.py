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
if "idiom_idx" not in st.session_state:
    st.session_state["idiom_idx"] = ""


def display_intro():
    st.title("Exhibition: Visualised Idioms")
    st.write("This is a demonstration of the results that were produced for the paper"
             " *Let Me Picture This: Understanding Idiom Visualization in Generative AI Models*. ")
    st.write("The displayed image will change based on the number of nouns from the prompt that "
             "reoccur in the generated image and the idiomatic meaning rating from the annotation study.")

    add_vertical_space(3)

def find_closest_match(df, slider1_value, slider2_value):
    # Calculate the Euclidean distance between the slider values and the DataFrame values
    df['all_counts'] = df['count_nouns_present_dreamlike'] + df['count_nouns_present_GPT']
    df['distance'] = np.sqrt((df['all_counts'] - slider1_value) ** 2 + (df['rating'] - slider2_value) ** 2)

    # Find the index of the minimum distance
    closest_index = df['distance'].idxmin()
    st.session_state["idiom_idx"] = df.loc[closest_index]["idiom"]

    # Return the corresponding row
    return df.loc[closest_index]["ImageID"]


def update_image(slider1_value, slider2_value, df_path, abs_path):
    df = pd.read_csv(df_path)
    df = df.drop_duplicates()
    id_select = find_closest_match(df, slider1_value, slider2_value)
    id_split= str(id_select).split("_")
    dir_id = "_".join(id_split[0:2])
    file_id = "_".join(id_split[2:])
    current_path = f"{abs_path}/{dir_id}/{file_id}"
    st.image(current_path, use_column_width="auto")




def select_vals_display(df_path, abs_path):
    col1, col2, col3= st.columns(3, gap="small")
    with col1:
        st.markdown("<p style='font-size: 18px;'><b>Number of nouns found in the prompt and the image</b></p>",
                    unsafe_allow_html=True)
        add_vertical_space(2)
        st.slider(label="la", min_value=1, max_value=10, key="literal", label_visibility="hidden")
        add_vertical_space(3)
        st.markdown("<p style='font-size: 18px;'><b>Rating for the idiomatic meaning in the image</b></p>",
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
    select_vals_display(
        "https://raw.githubusercontent.com/An0nymia/Visidiom/refs/heads/main/data/all_data_new.csv",
        "https://raw.githubusercontent.com/An0nymia/Visidiom/refs/heads/main/data/gen_resized/")

main()