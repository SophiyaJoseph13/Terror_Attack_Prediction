# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 16:36:12 2023

@author: 91721
"""

import streamlit as st
import pickle   
import pandas as pd

with open('best_logistic_model.pkl', 'rb') as model_file:
    loaded_model = pickle.load(model_file)

# Create a Streamlit web app
st.title('Terrorism Prediction App')

# Create input widgets for numerical features
known_associates = st.slider('Known Associates', min_value=0, max_value=10, value=5)
victims_injured = st.slider('Victims Injured', min_value=0, max_value=100, value=50)
victims_deceased = st.slider('Victims Deceased', min_value=0, max_value=100, value=25)
operatives_captured = st.slider('Operatives Captured', min_value=0, max_value=10, value=2)

# Create dropdown menus for categorical features
attack_type = st.selectbox('Attack Type', ['Shooting','Bombing','Hijacking','Arson','Stabbing','Kidnapping',
 'Assassination','Other'])
perpetrator = st.selectbox('Perpetrator', ['Group A', 'Group B', 'Group C', 'Group D'])
target_type = st.selectbox('Target Type', ['civilians','tourists','infrastructure','police',
 'government officials'])
training_location = st.selectbox('Training Location', ['Domestic', 'Abroad'])
intelligence_tip = st.selectbox('Intelligence Tip', ['Yes', 'No', 'Unknown'])
motive = st.selectbox('Motive', ['Political','Religious','Ethnic','Unknown','Retaliation'])
financial_support = st.selectbox('Financial Support', ['Local', 'International', 'Unknown'])
country = st.selectbox('Country', ['Turkey', 'Australia', 'Canada', 'Argentina', 'Brazil', 'China', 'Egypt', 'France', 'Paris', 'Germany', 'Greece', 'India', 'Indonesia', 'Italy', 'Japan', 'Kenya', 'Mexico', 'Peru', 'Russia', 'South Africa', 'South Korea', 'Spain', 'Thailand', 'UAE', 'UK', 'USA'])

# Create a button to make predictions
if st.button('Predict'):
    # Map categorical feature selections to one-hot encoded columns
    attack_type_encoded = {
        'Bombing': 1 if attack_type == 'Bombing' else 0,
        'Shooting': 1 if attack_type == 'Shooting' else 0,
        'Hijacking': 1 if attack_type == 'Hijacking' else 0,
        'Arson': 1 if attack_type == 'Arson' else 0,
        'Stabbing': 1 if attack_type == 'Stabbing' else 0,
        'Kidnapping': 1 if attack_type == 'Kidnapping' else 0,
        'Assassination': 1 if attack_type == 'Assassination' else 0,
        'Other': 1 if attack_type == 'Other' else 0
    }
    
    perpetrator_encoded = {
        'Group A': 1 if perpetrator == 'Group A' else 0,
        'Group B': 1 if perpetrator == 'Group B' else 0,
        'Group C': 1 if perpetrator == 'Group C' else 0,
        'Group D': 1 if perpetrator == 'Group D' else 0,
    }
                                   
    target_type_encoded = {
        'civilians': 1 if target_type == 'civilians' else 0,
        'tourists': 1 if target_type == 'tourists' else 0,
        'infrastructure': 1 if target_type == 'infrastructure' else 0,
        'police': 1 if target_type == 'police' else 0,
        'government officials': 1 if target_type == 'government officials' else 0,
    }
    
    training_location_encoded = {
        'Domestic': 1 if training_location == 'Domestic' else 0,
        'Abroad': 1 if training_location == 'Abroad' else 0,
    }
                                   
    intelligence_tip_encoded = {
        'Yes': 1 if intelligence_tip == 'Yes' else 0,
        'No': 1 if intelligence_tip == 'No' else 0,
        'Unknown': 1 if intelligence_tip == 'Unknown' else 0,
    }    
                                   
    motive_encoded = {
        'Political': 1 if motive == 'Political' else 0,
        'Religious': 1 if motive == 'Religious' else 0,
        'Ethnic': 1 if motive == 'Ethnic' else 0,
        'Unknown': 1 if motive == 'Unknown' else 0,
        'Retaliation': 1 if motive == 'Retaliation' else 0,
    }
                                   
    financial_support_encoded = {
        'Local': 1 if financial_support == 'Local' else 0,
        'International': 1 if financial_support == 'International' else 0,
        'Unknown': 1 if financial_support == 'Unknown' else 0,
    }
                                   
    country_encoded = {
    'Turkey': 1 if country == 'Turkey' else 0,
    'Australia': 1 if country == 'Australia' else 0,
    'Canada': 1 if country == 'Canada' else 0,
    'Argentina': 1 if country == 'Argentina' else 0,
    'Brazil': 1 if country == 'Brazil' else 0,
    'China': 1 if country == 'China' else 0,
    'Egypt': 1 if country == 'Egypt' else 0,
    'France': 1 if country == 'France' else 0,
    'Paris': 1 if country == 'Paris' else 0,
    'Germany': 1 if country == 'Germany' else 0,
    'Greece': 1 if country == 'Greece' else 0,
    'India': 1 if country == 'India' else 0,
    'Indonesia': 1 if country == 'Indonesia' else 0,
    'Italy': 1 if country == 'Italy' else 0,
    'Japan': 1 if country == 'Japan' else 0,
    'Kenya': 1 if country == 'Kenya' else 0,
    'Mexico': 1 if country == 'Mexico' else 0,
    'Peru': 1 if country == 'Peru' else 0,
    'Russia': 1 if country == 'Russia' else 0,
    'South Africa': 1 if country == 'South Africa' else 0,
    'South Korea': 1 if country == 'South Korea' else 0,
    'Spain': 1 if country == 'Spain' else 0,
    'Thailand': 1 if country == 'Thailand' else 0,
    'UAE': 1 if country == 'UAE' else 0,
    'UK': 1 if country == 'UK' else 0,
    'USA': 1 if country == 'USA' else 0,
    }                           
 
    # Use the loaded model to make predictions
    prediction = loaded_model.predict(pd.DataFrame({
        'Known_Associates': [known_associates],
        'Victims_Injured': [victims_injured],
        'Victims_Deceased': [victims_deceased],
        'Operatives_Captured': [operatives_captured],
        **attack_type_encoded,
        **perpetrator_encoded,
        **target_type_encoded,
        **training_location_encoded,
        **intelligence_tip_encoded,
        **motive_encoded,
        **financial_support_encoded,
        **country_encoded,
    }))

    # Display the prediction
    if prediction[0] == 1:
        st.write('The model predicts a major incident.')
    else:
        st.write('The model predicts a minor incident.')