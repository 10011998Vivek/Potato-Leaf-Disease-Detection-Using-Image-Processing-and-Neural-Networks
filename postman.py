# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 10:43:13 2022

@author: vivek
"""


from flask import Flask, request
import numpy as np
import pickle
import pandas as pd
#import flasgger
#from flasgger import Swagger

app=Flask(__name__)
#Swagger(app)

from keras import models    
model = models.load_model('model.h5')

def model_predict(img_path, model):
    print(img_path)
    img = image.load_img(img_path, target_size=(224, 224))

    # Preprocessing the image
    x = image.img_to_array(img)
    # x = np.true_divide(x, 255)
    ## Scaling
    x=x/255
    x = np.expand_dims(x, axis=0)
   

    # Be careful how your trained model deals with the input
    # otherwise, it won't make correct prediction!
   # x = preprocess_input(x)

    preds = model.predict(x)
    preds=np.argmax(preds, axis=1)
    if preds==0:
        preds="The leaf is diseased Potato___Early_blight"
    elif preds==1:
        preds="The leaf is diseased Potato___healthy"
    elif preds==2:
        preds="The leaf is diseased Potato___Late_blight"
        
    return preds

@app.route('/predict', methods=["GET",'POST'])
def upload():
    if request.method == 'POST':
        # Get the file from post request
        f = request.files['file']

        # Save the file to ./uploads
        basepath = os.path.dirname(__file__)
        file_path = os.path.join(
            basepath, 'uploads', secure_filename(f.filename))
        f.save(file_path)

        # Make prediction
        preds = model_predict(file_path, model)
        result=preds
        return result
    return None


if __name__=='__main__':
    app.run()
    
    