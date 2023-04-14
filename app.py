#Importing Libraries
import streamlit as st
import pickle
import numpy as np
import pandas as pd

st.set_page_config(page_title="Laptop Price Predictor", page_icon="💻",
                   layout="wide")

# Background image
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://e0.pxfuel.com/wallpapers/398/350/desktop-wallpaper-nillia-webdesign-web-development-management.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )

add_bg_from_url()

st.markdown("<h1 style='text-align: center; color: white;'>Laptop Price Predictor 💻</h1>", unsafe_allow_html=True)
# st.title("Laptop Price Predictor 💻" )



#import model
pipe=pickle.load(open("pipe.pkl","rb"))
df = pd.read_csv("df.csv")

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # brand input
    company = st.selectbox("Brand", df["Company"].unique())

with middle_column:
    # laptop type
    type = st.selectbox("Type", df["TypeName"].unique())

with right_column:
    # Ram size
    ram = st.selectbox("Ram (in GB)", df["Ram"].unique())

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # Weight input
    weight = st.number_input("Weight of laptop in kg")

with middle_column:
    # Touchscreen
    touchscreen = st.selectbox("Touchscreen", ["No", "Yes"])

with right_column:
    # IPS display
    ips = st.selectbox("IPS Display", ["No", "Yes"])

# making 3 cols left_column, middle_column, right_column
left_column, middle_column, right_column = st.columns(3)
with left_column:
    # screen size
    Screen_size = st.number_input("Screen Size (in Inches)")

with middle_column:
    # resolution
  resolution = st.selectbox('Screen Resolution',['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600','2560x1440', '2304x1440'])
with right_column:
    # cpu input
    cpu = st.selectbox("Cpu Brand", df["Cpu brand"].unique())

# making 3 cols left_column, middle_column, right_column
left_column,  right_column = st.columns(2)
with left_column:
    # hdd input
    hdd = st.selectbox("HDD(in GB)", [0, 128, 256, 512, 1024, 2048])


with right_column:
    # ssd input
    ssd = st.selectbox("SSD(in GB)", [0, 8, 128, 256, 512, 1024])

# making 3 cols left_column, middle_column, right_column
left_column,  right_column = st.columns(2)
with left_column:
    #gpu input
    gpu=st.selectbox("Gpu Brand",df["Gpu brand"].unique())

with right_column:
    #os input
    os=st.selectbox("OS Type",df["os"].unique())

if st.button("Predict Price"):
    ppi = None
    if touchscreen=="Yes":
        touchscreen=1
    else:
        touchscreen=0

    if ips == "Yes":
        ips=1
    else:
        ips=0

    X_res=int(resolution.split("x")[0])
    Y_res=int(resolution.split('x')[1])
    ppi=((X_res ** 2)+(Y_res ** 2))**0.5/Screen_size
    query=np.array([company, type, ram, weight, touchscreen, ips, ppi, cpu, hdd, ssd, gpu, os])

    query=query.reshape(1, 12)
    st.title("The Predicted Price of Laptop = Rs "+str(int(np.exp(pipe.predict(query)[0]))))


ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made with <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/><span> by</span><a style='display: inline; text-align: left;' href="https://github.com/i-am-dinesh" target="_blank"> Dinesh</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)