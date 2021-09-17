#USECASE
    # read data from raw data
    # split train and split data 
    # save train and test data in data/processed location
# Author: Motheesh Jay
# Created at: 16/09/2021

from get_data import get_params,get_data
import pandas as pd
import argparse
from sklearn.model_selection import train_test_split

def split_and_save(config_path):
    params=get_params(config_path)
    source_data_path=params["load_data"]["raw_dataset_path"]
    test_data_path=params["split_data"]["test_dataset_path"]
    train_data_path=params["split_data"]["train_dataset_path"]
    test_size=params["split_data"]["test_size"]
    seperator=params["data_format"]["seperator"]
    random_state=params["base"]["random_state"]
    data=get_data(source_data_path,seperator)
    train,test=train_test_split(data,test_size=test_size,random_state=random_state)
    train.to_csv(train_data_path,index=False,header=True)
    test.to_csv(test_data_path,index=False,header=True)
    


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    config_path=parsed_args.config
    split_and_save(config_path)