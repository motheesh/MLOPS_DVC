#USECASE
    # read data from data source
    # save it in data/raw location
# Author: Motheesh Jay
# Created at: 16/09/2021

from get_data import get_params,get_data
import pandas as pd
import argparse


def load_and_save(config_path):
    params=get_params(config_path)
    source_data_path=params["data_source"]["source_path"]
    load_data_path=params["load_data"]["raw_dataset_path"]
    seperator=params["data_format"]["seperator"]
    data=get_data(source_data_path,seperator)
    new_cols=[col.replace(" ","_") for col in data.columns]
    data.to_csv(load_data_path,index=False,header=new_cols)
    


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
    config_path=parsed_args.config
    load_and_save(config_path)