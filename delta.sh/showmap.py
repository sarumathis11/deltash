import streamlit as st

# Display the map inline using IFrame
st.write("## My Map")
st.write("Here's the map:")
st.write("")
st.write("")
st.write('<iframe width="1000" height="500" src="my_map.html"></iframe>', unsafe_allow_html=True)
