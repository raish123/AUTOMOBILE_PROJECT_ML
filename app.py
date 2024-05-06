#this file we used to display the features and prediction on web page(we r using flask module) through form!!!
#so importing all the important library which is used in this files
from flask import Flask,render_template,request,url_for,session
from source.exceptions import CustomException
from source.loggers import logging
import os,sys
from source.pipelines.predict_pipelines import CustomData,PredictPipeline

#creating an object of Flask class of flask module!!
app = Flask(__name__,template_folder='templates')


#creating a route() built in method of flask class generally we used route for mapping the URL with specific function
#route we will create follow by decorator function
@app.route('/',methods=['GET','POST'])
def index():
    return render_template('base.html')

#creating another route for prediction 
@app.route('/Prediction',methods=['GET','POST'])

def predict():
    if request.method == 'POST':
        try:
            logging.info('User has submitted a form!')

            symboling = int(request.form.get("symboling"))
            normalized_losses = int(request.form.get('normalized_losses'))
            make = request.form.get("make")
            fuel_type = request.form.get("fuel_type")
            body_style = request.form.get("body_style")
            drive_wheels = request.form.get("drive_wheels")
            engine_location = request.form.get("engine_location")
            width = float(request.form.get("width"))
            height = float(request.form.get("height"))
            engine_type = request.form.get("engine_type")
            engine_size = int(request.form.get("engine_size"))
            horsepower = int(request.form.get("horsepower"))
            city_mpg = int(request.form.get("city_mpg"))
            highway_mpg = int(request.form.get("highway_mpg"))

            # Create CustomData object
            data = CustomData(symboling, normalized_losses, make, fuel_type, body_style, drive_wheels,
                              engine_location, width, height, engine_type, engine_size, horsepower,
                              city_mpg, highway_mpg)

            # Get data as DataFrame
            pred_df = data.get_data_as_dataframe()
            logging.info('Prediction datapoint coming from webpage\n%s', pred_df)

            # Create PredictPipeline object
            pred = PredictPipeline()

            # Make prediction
            result = pred.predict(pred_df)

            return render_template('result.html', result=result[0])
            
        except Exception as e:
            raise CustomException(e, sys) 
    
    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)