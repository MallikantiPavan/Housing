import streamlit as st
import requests
st.header("House Price Prediction App")

col1,col2,col3=st.columns([2,2,2])

with col1:
    OverallQual = st.slider("Overall Quality rating (1-10)", 1, 10, 5)
    GrLivArea = st.number_input("Above Ground Living Area (sq ft)", 500, 6000, 1500)
    GarageCars = st.slider("Garage Capacity (Cars)", 0, 4, 2)
with col2:
    TotalBsmtSF = st.number_input("Total Basement Area (sq ft)", 0, 3000, 800)
    FullBath = st.slider("Full Bathrooms(0-4)", 0, 4, 2)
    YearBuilt = st.number_input("Year Built", 1870, 2025, 2000)
with col3:
    YearRemodAdd = st.number_input("Year of Last Remodeled", 1950, 2023, 2005)
    Neighborhood = st.selectbox("Neighborhood", ["Blmngtn: Bloomington Heights", "BrDale: Briardale", 
                                                 "BrkSide: Brookside", "ClearCr: Clear Creek", "CollgCr: College Creek", 
"Crawfor: Crawford", "Edwards: Edwards", "Gilbert: Gilbert", "IDOTRR: Iowa DOT and Rail Road", "MeadowV: Meadow Village",
 "Mitchel: Mitchell", "Names: North Ames", "NoRidge: Northridge", "NPkVill: Northpark Villa", 
 "NridgHt: Northridge Heights", "NWAmes: Northwest Ames", "OldTown: Old Town", "Sawyer: Sawyer", "SawyerW: Sawyer West", 
 "Somerset: Somerset East", "Somerst: Somerset", "StoneBr: Stone Brook", "SWISU: South & West of Iowa State University", "Timber: Timberland", "Veenker: Veenker"])
    KitchenQual = st.selectbox("Kitchen Quality", ["Excellent", "Good", "Average", "Good", "bad", "worst"])
    CentralAir = st.selectbox("Central Air", ["Yes", "No"])
    MSZoning = st.selectbox("MS Zoning", ["A","C","FV","I","RH","RL","RP","RM"])


if st.button("predict Price"):
    Data={
        "OverallQual": OverallQual,
        "GrLivArea": GrLivArea,
        "GarageCars": GarageCars,
        "TotalBsmtSF": TotalBsmtSF,
        "FullBath": FullBath,
        "YearBuilt": YearBuilt,
        "YearRemodAdd": YearRemodAdd,
        "Neighborhood": Neighborhood,
        "KitchenQual": KitchenQual,
        "CentralAir": CentralAir,
        "MSZoning": MSZoning
        }
    url="https://housing-dh2c.onrender.com//predict"
    response=requests.post(url,json=Data)
    if response.status_code==200:
        result=response.json()
        st.success(f"The predicted price of the house is ${result['predicted_price']:,.2f}")
    else:
        st.error("Error Found")
