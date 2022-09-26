import streamlit as st
import pickle
import pandas as pd
import os

# Settings

#Extraer los archivos pickle
with open(os.path.join('model','lin_reg.pkl'), 'rb') as li:
    lin_regr = pickle.load(li)
    
with open(os.path.join('model','log_reg.pkl'), 'rb') as li:
    log_regr = pickle.load(li)
    
with open(os.path.join('model','svc_m.pkl'), 'rb') as li:
    svc_model = pickle.load(li)


CLASSES = {0: "Setosa", 1: "Versicolor", 2: "Virginica"}
    
MODEL = {"Linear Regresion" : lin_regr , "Logistic Regresion" :log_regr , "SVM" : svc_model}


def main():
    st.title("Modelamient de Iris by @Fredy")
    
    st.sidebar.header('User Input Parameters')
    
    def user_input_parameters():
        sepal_length = st.sidebar.slider("Sepal length", min_value=4.3, max_value=7.9, value=5.4)
        sepal_width = st.sidebar.slider("Sepal width", min_value=2.0, max_value=4.4, value=3.4)
        petal_length = st.sidebar.slider("Petal length", min_value=1.0, max_value=6.9, value=1.3)
        petal_width = st.sidebar.slider("Petal length", min_value=0.1, max_value=2.5, value=0.2)
        data = {
            'sepal_length' : sepal_length,
            'sepal_width' : sepal_width,
            'petal_length' : petal_length,
            'petal_width' : petal_width
        }
        features = pd.DataFrame(data, index=[0])
        return features
    df = user_input_parameters()
    option = MODEL.keys()
    model = st.sidebar.selectbox("Witch model you like to uses?" , options=option)
    st.subheader("User Input Parameters")
    st.subheader(model)
    st.write(df)
    if st.button("RUN"):
        model = MODEL[model]
        predict = model.predict(df)
        print(predict)
        st.success(CLASSES[predict[0]])

if __name__ == "__main__":
    main()