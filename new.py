from flask import Flask, request
import pickle
import pandas as pd
import numpy as np
import flasgger
from flasgger import Swagger


app= Flask(__name__)
Swagger(app)
with open('classifier.pkl', 'rb') as f:
    classifier = pickle.load(f)

@app.route('/')
def welcome():
    return "Hello this is a new world of Dockers"
@app.route('/predict')
def predict_note_authentication():
    """Lets Check the Authenticity of your bank notes.
    ---
    parameters:
      - name: variance
        in: query
        type: number
        required: True
      - name: skewness
        in: query
        type: number
        required: True
      - name: curtosis
        in: query
        type: number
        required: True
      - name: Entropy
        in: query
        type: number
        required: True
    responses:
        200:
            description: The Output Values
 
    """

    variance=request.args.get('variance')
    skewness=request.args.get('skewness')
    curtosis=request.args.get('curtosis')
    Entropy=request.args.get('Entropy')
    prediction=classifier.predict([[variance,skewness,curtosis,Entropy]])
    return("The predicted value is " + str(prediction))


@app.route('/predict_file',methods=['POST'])
def predict_note_file():
    """Lets Check the Authenticity of your bank notes.
    ---
    parameters:
      - name: myfile
        in: formData
        type: file
        required: True
    responses:
        200:
            description: The Output Values
    """
    df_test=pd.read_csv(request.files.get('myfile'))
    prediction=classifier.predict(df_test)
    return("The output of the predict file" + str(list(prediction)))



if __name__=='__main__':
    app.run()