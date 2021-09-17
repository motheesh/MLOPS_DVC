from sklearn.ensemble import RandomForestRegressor
from get_data import get_params,get_data
from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import pandas as pd
import argparse
import numpy as np
import joblib
import os
import json

def writeJSON(filePath,content):
    with open(filePath,"w") as f:
        json.dump(content,f,indent=4)

def log_score(path,score):
    writeJSON(path,score)

def log_params(path,params):
    writeJSON(path,params)

def saveModel(params,model):
    model_save_folder=params["model_dir"]["folder"]
    model_name=params["model_dir"]["model_name"]
    prediction_model=params["webapp_model_dir"]["folder"]
    os.makedirs(model_save_folder, exist_ok=True)
    model_path = os.path.join(model_save_folder,model_name)
    predictionService=os.path.join(prediction_model,model_name)
    joblib.dump(model, model_path)
    joblib.dump(model, predictionService)

def eval_metrics(actual, pred):
    rmse = np.sqrt(mean_squared_error(actual, pred))
    mae = mean_absolute_error(actual, pred)
    r2 = r2_score(actual, pred)
    return rmse, mae, r2

def train_and_evaluate(config_path):
    params=get_params(config_path)
    test_data_path=params["split_data"]["test_dataset_path"]
    train_data_path=params["split_data"]["train_dataset_path"]
    seperator=params["data_format"]["seperator"]
    Target=params["base"]["target_column"]

    # get train test split
    train_data=get_data(train_data_path,seperator=seperator)
    test_data=get_data(test_data_path,seperator=seperator)
    train_x=train_data.drop(Target,axis=1)
    test_x=test_data.drop(Target,axis=1)
    train_y=train_data[Target]
    test_y=test_data[Target]

    #get params
    random_state=params["base"]["random_state"]
    alpha = params["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = params["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    # train model
    lr = ElasticNet(alpha=alpha, l1_ratio=l1_ratio, random_state=random_state)
    lr.fit(train_x, train_y)

    #predict using test data 
    predicted_Y = lr.predict(test_x)
    
    # evaluate predicted values accuracy
    (rmse, mae, r2) = eval_metrics(test_y, predicted_Y)
    score={
        "RMSE":rmse,
        "MAE":mae,
        "R2":r2
    }

    #log scores of trained model
    score_path=params["reports"]["scores"]
    log_score(score_path,score)

    #log parameters of trained models
    hyper_params={
        "alpha":alpha,
        "l1_ratio":l1_ratio
    }
    params_path=params["reports"]["params"]
    log_params(params_path,hyper_params)

    #save model
    saveModel(params,lr)



    
if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    config_path=parsed_args.config
    train_and_evaluate(config_path)



