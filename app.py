import streamlit as st
import pandas as pd
import joblib
from streamlit_lottie import st_lottie
import requests
import time

# ==============================
# Load the trained Random Forest
# ==============================
model = joblib.load("random_forest_model.pkl")

# ==============================
# Streamlit UI
# ==============================
st.set_page_config(page_title="Forest Cover Type Predictor", page_icon="🌲", layout="wide")

# ------------------------------
# Custom CSS for background & cards
# ------------------------------
st.markdown(
    """
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(to right, #013220, #00401a);
        color: white;
        font-family: 'Helvetica', sans-serif;
    }
    /* Card style for inputs */
    .stExpander {
        background: rgba(255, 255, 255, 0.1);
        border-radius: 12px;
        padding: 10px;
        margin-bottom: 10px;
    }
    /* Button hover effect */
    div.stButton > button:hover {
        background-color: #3e8e41;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------------------
# Lottie animation loader
# ------------------------------
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Forest animation
forest_anim = load_lottie_url("https://assets9.lottiefiles.com/packages/lf20_x62chJ.json")

st_lottie(forest_anim, speed=1, width=300, height=200, key="forest")

st.title("🌲 Forest Cover Type Prediction App")
st.write("Predict the **forest cover type** from cartographic variables using a trained Random Forest model.")

# ------------------------------
# User Inputs
# ------------------------------
st.header("📝 Input Features")

with st.expander("⛰️ Terrain Features", expanded=True):
    elevation = st.number_input("Elevation (meters)", min_value=0, max_value=5000, value=2000)
    aspect = st.number_input("Aspect (0-360°)", min_value=0, max_value=360, value=180)
    slope = st.number_input("Slope (degrees)", min_value=0, max_value=90, value=10)

with st.expander("💧 Hydrology Distances", expanded=True):
    hd_hydrology = st.number_input("Horizontal Distance to Hydrology (m)", value=100)
    vd_hydrology = st.number_input("Vertical Distance to Hydrology (m)", value=30)
    euclidean_hydrology = st.number_input("Euclidean Distance to Hydrology (m)", value=105)

with st.expander("🌞 Hillshade Values", expanded=True):
    hillshade_9am = st.number_input("Hillshade at 9am (0–255)", min_value=0, max_value=255, value=220)
    hillshade_noon = st.number_input("Hillshade at Noon (0–255)", min_value=0, max_value=255, value=230)
    hillshade_3pm = st.number_input("Hillshade at 3pm (0–255)", min_value=0, max_value=255, value=210)

with st.expander("🛣️ Infrastructure Distances", expanded=True):
    hd_roadways = st.number_input("Horizontal Distance to Roadways (m)", value=500)
    hd_firepoints = st.number_input("Horizontal Distance to Fire Points (m)", value=700)

with st.expander("🌳 Wilderness Area"):
    wilderness = st.selectbox("Choose Wilderness Area", [1, 2, 3, 4])
    wilderness_cols = {f"Wilderness_Area{i}": 1 if i == wilderness else 0 for i in range(1, 5)}

with st.expander("🪨 Soil Type"):
    soil = st.selectbox("Choose Soil Type", list(range(1, 41)))
    soil_cols = {f"Soil_Type{i}": 1 if i == soil else 0 for i in range(1, 41)}

# ------------------------------
# Build input dataframe
# ------------------------------
input_data = {
    "Elevation": elevation,
    "Aspect": aspect,
    "Slope": slope,
    "Horizontal_Distance_To_Hydrology": hd_hydrology,
    "Vertical_Distance_To_Hydrology": vd_hydrology,
    "Horizontal_Distance_To_Roadways": hd_roadways,
    "Hillshade_9am": hillshade_9am,
    "Hillshade_Noon": hillshade_noon,
    "Hillshade_3pm": hillshade_3pm,
    "Horizontal_Distance_To_Fire_Points": hd_firepoints,
    **wilderness_cols,
    **soil_cols,
    "Euclidean_Distance_To_Hydrology": euclidean_hydrology
}
input_df = pd.DataFrame([input_data])

# ------------------------------
# Prediction
# ------------------------------
st.header("🔮 Prediction")
if st.button("Predict Cover Type"):
    with st.spinner("Predicting 🌲..."):
        time.sleep(1.5)  # simulate loading
        prediction = model.predict(input_df)[0]
        st.success(f"🌲 Predicted Forest Cover Type: **{prediction}**")
        st.balloons()  # fun visual effect

# ------------------------------
# Footer
# ------------------------------
st.markdown("---")
st.caption("Built with ❤️ using Streamlit & Scikit-learn")
