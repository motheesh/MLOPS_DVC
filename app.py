from flask import Flask, request, render_template,jsonify,abort,g 
from flask_cors import CORS, cross_origin
import config
import pandas as pd
from src.get_data import get_params
import joblib

app=Flask(__name__)
CORS(app)
app.config.from_pyfile("config.py")

@app.route("/", methods=["GET", "POST"])
def index():
    labels=['fixed_acidity','volatile_acidity',
    'citric_acid','residual_sugar',
    'chlorides','free_sulfur_dioxide',
    'total_sulfur_dioxide','density',
    'pH','sulphates','alcohol']
    return render_template("index.html",labels=labels)

@app.route("/predict" , methods=['POST'])
def predict():
    try:
        req_data=request.get_json()
        df=pd.json_normalize(req_data)
        params=get_params(config.params_path)
        predict_model_path=params["webapp_model_dir"]["model_path"]
        prediction_model=joblib.load(predict_model_path)
        result=round(prediction_model.predict(df)[0],2)

        return jsonify({"result":result})
    except Exception as e:
        return jsonify({"status":"error","error":e,"message":"Something went wrong please try again"})

if __name__=="__main__":
    app.run(port=5000,debug=config.debug)