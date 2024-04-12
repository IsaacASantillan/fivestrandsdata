import streamlit as st 
import pandas as pd
from parser_1 import df, sizesselection, countiesselection
import seaborn as sns 
import numpy as np

st.title("""
    Correlation Between School District Size and Environmental and Climate Action Score
    """)

st.markdown("""
The data visualization shows larger districts have a slightly higher Environmental 
            and Climate Action Score on average, however size is not a significant factor in determining whether or not a school will have a lower or higher score. 
            The data alludes that scores are more dependent on the individual school’s commitment to environmental initiatives, rather than school district size. 
            """
            )


st.sidebar.header("User Input Features")



selected_county = st.sidebar.selectbox("County", countiesselection)
all_options = st.sidebar.checkbox("Select All Options")
if all_options:
    selected_county = countiesselection
else:
    selected_county = [selected_county]
selected_size = st.sidebar.multiselect("Size of District", sizesselection, sizesselection)


df = df[df["County"].isin(selected_county) & df["Size of District"].isin(selected_size)]
size_categories = ["Medium", "Large", "Very Large" ]
df["Size of District"] = pd.Categorical(df["Size of District"], categories = size_categories)
df = df.sort_values(by = "Size of District")
df.reset_index(drop=True, inplace=True)
st.write(df)

b = st.button('Barplot')
if b and not all_options:
    hue_order = ['Medium', 'Large', 'Very Large']
    pl = sns.catplot(data = df, y="District Name", hue="Size of District", x="Environmental and Climate Action Score (20 points)", kind="bar", palette="pastel", hue_order = hue_order)
    plt.xticks(np.arange(0, 21, step=2))
    st.pyplot(pl)

if all_options and b:
    hue_order = ['Medium', 'Large', 'Very Large']
    pl = sns.catplot(data = df, y="Size of District", hue="Size of District", x="Environmental and Climate Action Score (20 points)", kind="bar", palette="pastel", hue_order = hue_order)
    plt.xticks(np.arange(0, 21, step=2))
    st.pyplot(pl)


