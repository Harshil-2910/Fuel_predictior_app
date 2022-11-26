import pandas as pd
import numpy as np
import pickle
import streamlit as st

pickle_in = open('rf.pkl','rb')
rf = pickle.load(pickle_in)


def predict_price(Eng_Displ, No_Cyl, No_Gears,Max_Ethanol_Per_Gasoline, Intake_Valves_Per_Cyl,Exhaust_Valves_Per_Cyl, Trans_Creeper_Gear, Unqiue_Labels,Air_Aspiration_Method_Desc, Fuel_Metering_Sys_Desc, Cyl_Deact):
    prediction = rf.predict([[Eng_Displ, No_Cyl, No_Gears,Max_Ethanol_Per_Gasoline, Intake_Valves_Per_Cyl,Exhaust_Valves_Per_Cyl,                Trans_Creeper_Gear,Unqiue_Labels,Air_Aspiration_Method_Desc, Fuel_Metering_Sys_Desc, Cyl_Deact]])
    print (prediction)
    return prediction

def main():
    st.title("Conventional Fuel Prediction")
    Eng_Displ = st.slider("Engine Display", min_value = 0.900000, max_value = 8.400000, step = 0.1)
    No_Cyl = st.slider("No of cylinders", min_value = 3, max_value = 12, step =1)
    No_Gears = st.slider("No of Gears", min_value = 1, max_value = 9, step = 1)
    Max_Ethanol_Per_Gasoline = st.slider("Max_Ethanol Percent of Gasoline", min_value = 10.00, max_value = 85.00, step = 1.00)
    Intake_Valves_Per_Cyl = st.slider("Intake valves Per Cyl", min_value = 1, max_value = 2, step = 1)
    Exhaust_Valves_Per_Cyl = st.slider("Exhaust Valves Per Cyl", min_value = 1, max_value = 2, step = 1)
    Air_Aspiration_Method_Desc = st.slider("Air Aspiration Method Desc", min_value = 0, max_value = 4, step = 1)
    Trans_Creeper_Gear = st.slider("Trans Creeper Gear", min_value = 1, max_value = 2, step = 1)
    Unqiue_Labels = st.slider("Unqiue Labels", min_value = 0, max_value = 2, step = 1)
    Fuel_Metering_Sys_Desc = st.slider("Fuel Metering Sys Desc", min_value = 0, max_value = 5, step = 1)
    Cyl_Deact = st.slider("Cyl Deact", min_value = 0, max_value = 2, step = 1)
   
    result = ""
    if st.button("Predict"):
        result = predict_price(Eng_Displ, No_Cyl, No_Gears,Max_Ethanol_Per_Gasoline, Intake_Valves_Per_Cyl,Exhaust_Valves_Per_Cyl, Trans_Creeper_Gear, Unqiue_Labels,Air_Aspiration_Method_Desc, Fuel_Metering_Sys_Desc, Cyl_Deact)
    st.success('The output is {}'.format(result))

if __name__ == '__main__': #
    main()
