def render_main_view(data):
    import streamlit as st

    st.title("Main View")
    st.write("Welcome to the Streamlit MVC Application!")
    
    if data:
        st.write("Here are the records from the database:")
        for record in data:
            st.write(record)
    else:
        st.write("No data available.")