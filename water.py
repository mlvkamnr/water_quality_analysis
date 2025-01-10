import streamlit as st
import pandas as pd


# Load the dataset
@st.cache_data
def load_data():
    file_path = "water_quality_dataset.csv"
    data = pd.read_csv("water_potability.csv")
    data = data.dropna()
    return data

def analyze_water_quality(ph, turbidity, tds,temperature,dataset):
    """Analyze water quality based on input parameters and dataset"""
    conditions = []

    # Check pH levels
    if 6.5 <= ph <= 8.5:
        conditions.append("pH is within the healthy range.")
    else:
        conditions.append("pH is outside the healthy range.")

    # Check turbidity
    if turbidity <= 5:
        conditions.append("Turbidity is within the healthy range.")
    else:
        conditions.append("Turbidity is outside the healthy range.")

    # Check TDS
    if 50 <= tds <= 150:
        conditions.append("TDS is within the healthy range.")
    else:
        conditions.append("TDS is outside the healthy range.")
        
    # Check Temperature
    if if 10 <= Temperature <= 22:
        conditions.append("Temperature is within the healthy range.")
    else:
        conditions.append("Temperature is outside the healthy range.")

    # Determine overall water quality
    if all("within the healthy range" in condition for condition in conditions):
        overall_status = "Healthy"
    else:
        overall_status = "Unhealthy"

    return conditions, overall_status

# Streamlit App
st.set_page_config(page_title="Water Quality Analysis", page_icon="💧", layout="wide")

# Header
st.markdown(
    """
    <style>
    .title {
        font-size: 40px;
        text-align: center;
        color: #4CAF50;
    }
    .subtitle {
        font-size: 20px;
        text-align: center;
        color: #666;
    }
    </style>
    """, unsafe_allow_html=True
)

st.markdown("<div class='title'>Water Quality Analysis 💧</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Analyze the quality of your water using key parameters</div>", unsafe_allow_html=True)

# Load dataset
dataset = load_data()

# Dataset preview with styling
with st.expander("🔍 Dataset Preview"):
    st.dataframe(dataset.head(10).style.highlight_max(axis=0, color="#DFF0D8"))

# Sidebar for user inputs
st.sidebar.header("Input Parameters")
ph = st.sidebar.number_input("Enter pH value:", min_value=0.0, max_value=14.0, step=0.1, value=7.0)
turbidity = st.sidebar.number_input("Enter Turbidity (NTU):", min_value=0.0, step=0.1, value=1.0)
tds = st.sidebar.number_input("Enter TDS (mg/L):", min_value=0.0, step=1.0, value=100.0)
temperature = st.sidebar.number_input("Enter Temperature (degree Celsius):", min_value=0.0, step=1.0, value=100.0)

# Analyze Water Quality
if st.sidebar.button("Analyze Water Quality"):
    if ph > 0 and turbidity > 0 and tds > 0 and temperature > 0:
        conditions, overall_status = analyze_water_quality(ph, turbidity, tds, temperature ,dataset)

        st.subheader("📊 Analysis Report")
        for condition in conditions:
            st.write("-", condition)

        # Overall status
        st.markdown(
            f"""
            <div style="text-align: center; padding: 10px; border-radius: 5px; background-color: {'#DFF0D8' if overall_status == 'Healthy' else '#F2DEDE'};">
                <b>Overall Water Quality Status:</b> {overall_status}
            </div>
            """, unsafe_allow_html=True
        )


# Footer
st.markdown(
    """
    <hr style="border:1px solid #ddd;">
    <div style="text-align: center; color: #aaa; font-size: 12px;">
        © 2025 Water Quality Analysis App. Made by Aayat Aashir Jaineel Yasir using Streamlit.
    </div>
    """, unsafe_allow_html=True
)
