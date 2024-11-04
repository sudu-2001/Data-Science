from flask import Flask,render_template

import pandas as pd

app = Flask(__name__)

def load_data():

	data_path = '/home/sudarshan/work/Data-Science/Descriptive-Analysis/Data/sales_data.csv'

	data=pd.read_csv(data_path)

	total_sales=data["Sales"].sum()

	avg_sales=data["Sales"].mean()

	total_customer=data["Customers"].sum()

	avg_customer=data["Customers"].mean()

	return{

		"total_sales":total_sales,

		"avg_sales":avg_sales,

		"total_customer":total_customer,

		"avg_customer":avg_customer,

		"records":data.to_dict(orient="records")

	}

@app.route("/")

def index():

	analytics_data=load_data()

	return render_template("index.html",data=analytics_data)

if  __name__=="__main__":

	app.run(host='0.0.0.0',port=5000,debug=True)
