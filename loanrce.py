import streamlit as st
import joblib
st.title('Loan approval process Automation')
model=joblib.load('loan_data1.joblib')
gender=st.number_input('Enter gender male:0 ,female:1')
married=st.number_input('Enter martial status married:0 ,unmarried:1')
income=st.number_input('Enter applicant income in thousands')
la=st.number_input('Enter loan amount income in thousands')
if st.button('predict Approval'):
    predication=model.predict([[gender,married,income,la]])
    if prediction=='Y':
        st.text('loan approved')
    else:
        st.text('loan rejected')
