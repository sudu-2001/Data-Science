from flask import Flask,render_template

import pandas as pd

app=Flask(__name__)

def load_data():

	data_path=('/home/sudarshan/work/Data-Science/Diagnostic-Analysis/Data/SampleSuperstore.csv')

	data=pd.read_csv(data_path)

	return data

def data_analytic(data):

	sales_by_region=data.groupby('Region')['Sales'].sum()

	sales_by_category=data.groupby('Category')['Sales'].sum()

	sales_by_discount=data.groupby('Region')['Discount'].sum()

	sales_by_region_category=(

		data.groupby(['Region','Category'])['Sales']

		.sum()

		.unstack(fill_value=0)

		.to_dict(orient='index')

	)

	return{

		'sales_by_region':sales_by_region.to_dict(),

		'sales_by_category':sales_by_category.to_dict(),

		'sales_by_discount':sales_by_discount.to_dict(),

		'sales_by_region_category':sales_by_region_category

	}

@app.route('/')

def index():

	data=load_data()

	analytic_data=data_analytic(data)

	return render_template('index.html',**analytic_data)

if __name__=='__main__':

	app.run(host='0.0.0.0',port=5000,debug=True)
