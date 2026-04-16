import streamlit as st
import pickle
import numpy as np

# 1. Page Config
st.set_page_config(page_title="Iris Intelligence", page_icon="🌿", layout="wide")

# 2. Load the Model
try:
    with open('logreg_model.pkl', 'rb') as file:
        model = pickle.load(file)
except FileNotFoundError:
    st.error("Model file not found! Please ensure 'logreg_model.pkl' is in the repo.")

# 3. Bright & High-Contrast Custom UI Styling
st.markdown("""
    <style>
    /* 1. Overall App Background */
    .stApp {
        background-color: #0e1117;
    }

    /* 2. Force Input Label Text (Sepal Length, etc.) to be Bright White */
    .stNumberInput label p {
        color: white !important;
        font-size: 18px !important;
        font-weight: bold !important;
    }

    /* 3. Force the Number inside the box to be Bright White/Cyan */
    input {
        color: #00ffcc !important; /* This makes the digits bright cyan/white */
        font-size: 20px !important;
        font-weight: bold !important;
    }

    /* 4. Style the Input Box Border and Background */
    div[data-baseweb="input"] {
        background-color: #1e2129 !important;
        border: 2px solid #4CAF50 !important;
        border-radius: 10px !important;
    }

    /* 5. Style the + and - buttons */
    button[kind="secondary"] {
        color: white !important;
        border-color: #4CAF50 !important;
    }

    /* 6. Main Prediction Button */
    .stButton>button {
        background-color: #ff4b4b !important;
        color: white !important;
        border-radius: 10px !important;
        font-weight: bold !important;
        width: 100%;
    }

    .prediction-text { font-size: 32px; font-weight: bold; color: #2E7D32; }
    .info-card { background-color: #1e2129; padding: 20px; border-radius: 15px; border-left: 8px solid #4CAF50; color: white; }
    </style>
    """, unsafe_allow_html=True)

# 4. App Header
st.title("🔬 Botanical Diagnostic Tool: Iris Classification")
st.write("Professional biometric analysis for species identification.")
st.divider()

# 5. Main Interface
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.markdown("### 📏 Specimen Measurements")
    s_length = st.number_input("Sepal Length (cm)", min_value=0.1, max_value=10.0, value=5.1, step=0.1)
    s_width = st.number_input("Sepal Width (cm)", min_value=0.1, max_value=10.0, value=3.5, step=0.1)
    p_length = st.number_input("Petal Length (cm)", min_value=0.1, max_value=10.0, value=1.4, step=0.1)
    p_width = st.number_input("Petal Width (cm)", min_value=0.1, max_value=10.0, value=0.2, step=0.1)
    
    predict_btn = st.button("RUN DIAGNOSIS", type="primary", use_container_width=True)

    # Permanent Physiology Definitions (Always Visible on the left)
    st.markdown("### 📚 Botanical Key")
    st.info("**Sepals (Falls):** The outer, drooping protective layers. \n\n **Petals (Standards):** The inner, upright colorful layers.")

with col2:
    if predict_btn:
        # Prediction Logic
        features = np.array([[s_length, s_width, p_length, p_width]])
        prediction = model.predict(features)[0]
        
        species_info = {
            0: {
                "name": "Iris-Setosa", 
                "url": "https://upload.wikimedia.org/wikipedia/commons/5/56/Kosaciec_szczecinkowaty_Iris_setosa.jpg",
                "fact": "Physiologically, Setosa is adapted for cooler climates. Its reduced petal size minimizes energy expenditure while maintaining reproductive viability."
            },
            1: {
                "name": "Iris-Versicolor", 
                "url": "https://upload.wikimedia.org/wikipedia/commons/4/41/Iris_versicolor_3.jpg",
                "fact": "Also known as the 'Blue Flag'. Its physiological structure is a classic example of pollinator-specific evolution, favoring large-bodied insects."
            },
            2: {
                "name": "Iris-Virginica", 
                "url": "https://upload.wikimedia.org/wikipedia/commons/9/9f/Iris_virginica.jpg",
                "fact": "The largest of the three; its significant sepal ribbing acts as a physiological 'runway' for complex insect navigation."
            }
        }
        
        selected = species_info[prediction]
        
        # Display Results
        st.markdown(f"<p class='prediction-text'>Result: {selected['name']}</p>", unsafe_allow_html=True)
        st.image(selected['url'], caption=f"Specimen: {selected['name']}", use_container_width=True)
        
        # The Physiology Context Box (Specific to the predicted flower)
        st.markdown(f"""
        <div class="info-card">
            <h4 style='margin-top:0;'>🧪 Physiological Diagnostic Note:</h4>
            {selected['fact']}
        </div>
        """, unsafe_allow_html=True)
    else:
        st.warning("Awaiting biometric data. Please enter measurements and click 'Run Diagnosis'.")

st.divider()
st.caption("Developed by Omosomi Ann Hassan | AI Product Operations")