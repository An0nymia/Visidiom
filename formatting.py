import streamlit as st


def hide_menu():
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





