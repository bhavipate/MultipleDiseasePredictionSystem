import pickle
import streamlit as st
import sqlite3
from streamlit_option_menu import option_menu

# loading the saved models
diabetes_model = pickle.load(open("C:\MultipleDiseasePredictionSystem\saved models\diabetes_model.sav", 'rb'))

heart_disease_model = pickle.load(open("C:\MultipleDiseasePredictionSystem\saved models\heart_disease_model.sav",'rb'))

parkinsons_model = pickle.load(open('C:\MultipleDiseasePredictionSystem\saved models\parkinsons_model.sav', 'rb'))

conn=sqlite3.connect("Disease.db")
cursor1=conn.cursor()
cursor2=conn.cursor()
cursor3=conn.cursor()

# sidebar for navigation
with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['activity','heart','person'],
                          default_index=0)
    
def add_value_diabetes(no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, result):
    try:
        cursor1.execute("""
            INSERT INTO tabDiabetes 
            (no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (no_of_pregnancies, glucose_level, blood_pressure_value, skin_thickness, insulin_level, BMI, diabetes_pedigree, age, result))
        print("Added successfully to 'tabDiabetes'!")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error:", e)
        return False
# Diabetes Prediction Page
if (selected == 'Diabetes Prediction'):
    
    # page title
    st.title('Diabetes Prediction using ML')
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies',key="noofpre")
        
    with col2:
        Glucose = st.text_input('Glucose Level',key="gluco")
    
    with col3:
        BloodPressure = st.text_input('Blood Pressure value',key="bpval")
    
    with col1:
        SkinThickness = st.text_input('Skin Thickness value',key="skint")
    
    with col2:
        Insulin = st.text_input('Insulin Level',key="insulinlv")
    
    with col3:
        BMI = st.text_input('BMI value',key="bmi")
    
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value',key="dia")
    
    with col2:
        Age = st.text_input('Age of the Person',key="age")
    
    
    # code for Prediction
    diab_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])
        if (diab_prediction[0] == 1):   
          diab_diagnosis = 'The person is diabetic'
        else:
          diab_diagnosis = 'The person is not diabetic'
        
        noofpre=st.session_state["noofpre"]
        gluco=st.session_state["gluco"]
        bpval=st.session_state["bpval"]
        skint=st.session_state["skint"]
        insulinlv=st.session_state["insulinlv"]
        bmi=st.session_state["bmi"]
        dia=st.session_state["dia"]
        age=st.session_state["age"]
        store=add_value_diabetes(noofpre,gluco,bpval,skint,insulinlv,bmi,dia,age,diab_diagnosis)
        if(store):
            st.toast("Data Stored Sucessfully.....!!!!")
        else:
            st.warning("Enble to store Data...!!!")
    st.success(diab_diagnosis)


def add_value_heart(age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, result):
    try:
        cursor2.execute("""
            INSERT INTO tabHeart 
            (age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (age, sex, chestpain, bp, cholestoral, BS, EleCardo, HR, EIA, Depression, ST, flouroscopy, thal, result))
        print("Added successfully to 'tabHeart'!")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error:", e)
        return False
# Heart_Disease Prediction Page
if (selected == 'Heart Disease Prediction'):
    
    # page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age',key="age")
        
    with col2:
        sex = st.text_input('Sex  ' ,placeholder="Male(0)/Female(1)/Other(2)" ,key="sex")
        
    with col3:
        cp = st.text_input('Chest Pain types',key="chestpain")
        
    with col1:
        trestbps = st.text_input('Resting Blood Pressure',key="bp")
        
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl',key="cholestoral")
        
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl',key="BS")
        
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results',key="EleCardo")
        
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved',key="HR")
        
    with col3:
        exang = st.text_input('Exercise Induced Angina',key="EIA")
        
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise',key="Depression")
        
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment',key="ST")
        
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy',key="flouroscopy")
        
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',key="thal")
        
        
     
     
    # code for Prediction
    heart_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict([[int(age), int(sex), int(cp), int(trestbps), int(chol), int(fbs),int( restecg) ,int(thalach), int(exang), int(oldpeak), int(slope), int(ca) ,int(thal)]])                          

        
        if (heart_prediction[0] == 1):
          heart_diagnosis = 'The person is having heart disease'
        else:
          heart_diagnosis = 'The person does not have any heart disease'

        age=st.session_state["age"]
        sex=st.session_state["sex"]
        chestpain=st.session_state["chestpain"]
        bp=st.session_state["bp"]
        cholestoral=st.session_state["cholestoral"]
        BS=st.session_state["BS"]
        EleCardo=st.session_state["EleCardo"]
        HR=st.session_state["HR"]
        EIA=st.session_state["EIA"]
        Depression=st.session_state["Depression"]
        ST=st.session_state["ST"]
        flouroscopy=st.session_state["flouroscopy"]
        thal=st.session_state["thal"]
        store=add_value_heart(age,sex,chestpain,bp,cholestoral,BS,EleCardo,HR,EIA,Depression,ST,flouroscopy,thal,heart_diagnosis)
        if(store):
            st.toast("Data Stored Sucessfully.....!!!!")
        else:
            st.warning("Enble to store Data...!!!")
            

            

        
    st.success(heart_diagnosis)
        


def add_value_parkinson(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, result):
    try:
        cursor3.execute("""
            INSERT INTO tabPark 
            (fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, Result) 
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        """, (fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE, result))
        print("Added successfully to 'tabPark'!")
        conn.commit()
        return True
    except sqlite3.Error as e:
        print("Error for Park:", e)
        return False
# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction using ML")
    
    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)'  , key="A")
        
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)' , key="B")
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)' , key="C")
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)' , key="D")
        
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)' , key="E")
        
    with col1:
        RAP = st.text_input('MDVP:RAP' , key="F")
        
    with col2:
        PPQ = st.text_input('MDVP:PPQ' , key="G")
        
    with col3:
        DDP = st.text_input('Jitter:DDP' , key="H")
        
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer' , key="I")
        
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)' , key="J")
        
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3' , key="K")
        
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5' , key="L")
        
    with col3:
        APQ = st.text_input('MDVP:APQ' , key="M")
        
    with col4:
        DDA = st.text_input('Shimmer:DDA' , key="N")
        
    with col5:
        NHR = st.text_input('NHR' , key="O")
        
    with col1:
        HNR = st.text_input('HNR' , key="P")
        
    with col2:
        RPDE = st.text_input('RPDE' , key="Q")
        
    with col3:
        DFA = st.text_input('DFA' , key="R")
        
    with col4:
        spread1 = st.text_input('spread1' , key="S")
        
    with col5:
        spread2 = st.text_input('spread2' , key="T")
        
    with col1:
        D2 = st.text_input('D2' , key="U")
        
    with col2:
        PPE = st.text_input('PPE' , key="V")
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
        fo=st.session_state["A"]
        fhi=st.session_state["B"]
        flo=st.session_state["C"]
        Jitter_percent=st.session_state["D"]
        Jitter_Abs=st.session_state["E"]
        RAP=st.session_state["F"]
        PPQ=st.session_state["G"]
        DDP=st.session_state["H"]
        Shimmer=st.session_state["I"]
        Shimmer_dB=st.session_state["J"]
        APQ3=st.session_state["K"]
        APQ5=st.session_state["L"]
        APQ=st.session_state["M"]
        DDA=st.session_state["N"]
        NHR=st.session_state["O"]
        HNR=st.session_state["P"]
        RPDE=st.session_state["Q"]
        DFA=st.session_state["R"]
        spread1=st.session_state["S"]
        spread2=st.session_state["T"]
        D2=st.session_state["U"]
        PPE=st.session_state["V"]
        store=add_value_parkinson(fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE,parkinsons_diagnosis)
        print(store)
        if(store):
            st.toast("Data Stored Sucessfully.....!!!!")
        else:
            st.warning("Enble to store Data...!!!")


        
    st.success(parkinsons_diagnosis)
