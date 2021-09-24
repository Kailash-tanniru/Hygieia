from django.shortcuts import render
from django.http import HttpResponse

import numpy as np
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import StandardScaler
import joblib


# Create your views here.
def home(request):
    return render(request,'home.html')

def service(request):
    return render(request,'pages/services.html')

def predictions(request):
    return render(request,'pages/predictions.html')
    
def diabetes(request):
    return render(request,'pages/diabetes.html')


def predict(request):
    dt = pd.read_csv('diabetes.csv')
    X = dt.drop(columns='Outcome',axis=1)
    Y = dt['Outcome']
  
    scaler = StandardScaler()
    scaler.fit(X)
    standardized_data = scaler.transform(X)
    X = standardized_data
    from sklearn.model_selection import train_test_split
    X_train,X_test,Y_train,Y_test = train_test_split(X,Y,test_size = 0.2,stratify = Y,random_state=2)
    classifier = svm.SVC(kernel='linear')
    classifier.fit(X_train, Y_train)
    model = joblib.load('model.sav')
   
    if request.method=='POST':
        pregnancies=int(request.POST['pregnancies'])
        glucose = int(request.POST['glucose level'])
        bp = int(request.POST['blood pressure'])
        skin_thickness = int(request.POST['skinthickness'])
        insulin = int(request.POST['insulin'])
        bmi = float(request.POST['bmi'])
        dpf = float(request.POST['dpf'])
        age = int(request.POST['age'])

        input_data = [pregnancies,glucose,bp,skin_thickness,insulin,bmi,dpf,age]
        # changing the input_data to numpy array
        input_data_as_numpy_array = np.asarray(input_data)

        # reshape the array as we are predicting for one instance
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1) 
        std_data = scaler.transform(input_data_reshaped)
        output = classifier.predict(std_data)
        if output[0]==0:
            return render(request,"pages/diabetes/diabetic.html",{'content':'A'})
        else:
            return render(request,"pages/diabetes/non_diabetic.html",{'content':'NON'})

    

