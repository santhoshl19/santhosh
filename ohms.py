import streamlit as st

def calculate_voltage(current, resistance):
    return current * resistance

def calculate_current(voltage, resistance):
    return voltage / resistance

def calculate_resistance(voltage, current):
    return voltage / current

st.title('Ohm\'s Law Calculator')

option = st.selectbox('What do you want to calculate?', ('Voltage (V)', 'Current (I)', 'Resistance (R)'))

if option == 'Voltage (V)':
    current = st.number_input('Enter Current (I) in Amperes:', min_value=0.0, format="%.2f")
    resistance = st.number_input('Enter Resistance (R) in Ohms:', min_value=0.0, format="%.2f")
    if st.button('Calculate Voltage'):
        voltage = calculate_voltage(current, resistance)
        st.write(f'Voltage (V) = {voltage:.2f} V')
elif option == 'Current (I)':
    voltage = st.number_input('Enter Voltage (V) in Volts:', min_value=0.0, format="%.2f")
    resistance = st.number_input('Enter Resistance (R) in Ohms:', min_value=0.0, format="%.2f")
    if st.button('Calculate Current'):
        current = calculate_current(voltage, resistance)
        st.write(f'Current (I) = {current:.2f} A')
else:
    voltage = st.number_input('Enter Voltage (V) in Volts:', min_value=0.0, format="%.2f")
    current = st.number_input('Enter Current (I) in Amperes:', min_value=0.0, format="%.2f")
    if st.button('Calculate Resistance'):
        resistance = calculate_resistance(voltage, current)
        st.write(f'Resistance (R) = {resistance:.2f} Ω')
