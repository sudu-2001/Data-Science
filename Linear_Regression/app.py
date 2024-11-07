from flask import Flask,render_template,request,jsonify

from sklearn.linear_model import LinearRegression

from sklearn.model_selection import train_test_split

import joblib

import pandas as pd

app=Flask(__name__)

data=pd.read_csv('/home/sudarshan/work/Data-Science/Linear_Regression/Data/all_stocks_5yr.csv')

data['Date']=pd.to_datetime(data['date'])

data['Date']=data['Date'].map(pd.Timestamp.toordinal)

X=data[['Date']]

y=data['close']

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=LinearRegression()

model.fit(X_train,y_train)

joblib.dump(model,'model.plk')

@app.route('/')

def index():

        return render_template('index.html')

@app.route('/predict',methods=['post'])

def predict():

        date=request.json.get('date')

        date=pd.to_datetime(date)

        if pd.isnull(date):

                return jsonify({'error': 'Inavalid Error'}), 400

        date_ordinal=date.toordinal()

        model=joblib.load('model.pkl')

        prediction = model.predict([[date_ordinal]])

        return jsonify({'prediction': float(prediction[0])})

if __name__=="__main__":

        app.run(host='0.0.0.0',debug=True)
