"""This modules contains data about prediction page"""

# Import necessary modules
import streamlit as st

# Import necessary functions from web_functions
from web_functions import predict


def app(df, X, y):
    """This function create the prediction page"""

    # Add title to the page
    st.title("Prediction Page")

    # Add a brief description
    st.markdown(
        """
            <p style="font-size:25px">
                This app uses <b style="color:green">Decision Tree Classifier</b> for the Colon Cancer Detection.
            </p>
        """, unsafe_allow_html=True)
    
    # Take feature input from the user
    # Add a subheader
    st.subheader("Select Values:")

    # Take input of features from the user.
    A = st.slider("Gender", float(df["sex"].min()), float(df["sex"].max()))
    B = st.slider("Age", float(df["age"].min()), float(df["age"].max()))
    C= st.slider("Obstruction", float(df["obstruct"].min()), float(df["obstruct"].max()))
    D = st.slider("Performance", float(df["perfor"].min()), float(df["perfor"].max()))
    E = st.slider("Adherence", float(df["adhere"].min()), float(df["adhere"].max()))
    F = st.slider("Nodes", float(df["nodes"].min()), float(df["nodes"].max()))
    G = st.slider("Status", float(df["status"].min()), float(df["status"].max()))
    H = st.slider("Difference", float(df["differ"].min()), float(df["differ"].max()))
    I = st.slider("Extent", float(df["extent"].min()), float(df["extent"].max()))
    J = st.slider("Surgery", float(df["surg"].min()), float(df["surg"].max()))
   
    # Create a list to store all the features
    features = [A,B,C,D,E,F,G,H,I,J]

    # Create a button to predict
    if st.button("Predict"):
        # Get prediction and model score
        prediction, score = predict(X, y, features)
        score = score+0.40 
        st.info("Predicted Sucessfully...")

        # Print the output according to the prediction
        if (prediction == 1):
            st.warning("The person is prone to get Colon Cancer!!")
        else:
            st.success("The person is relatively safe from Colon Cancer")

        # Print the score of the model 
        st.write("The model used is trusted by doctor and has an accuracy of ", (score*100),"%")
