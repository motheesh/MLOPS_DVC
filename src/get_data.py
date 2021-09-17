# usecase
    # Load parameters from yaml file
    # Get data source path 
    # Read the data and return
# Author: Motheesh Jay
# Created at: 16/09/2021


import os
import yaml
import argparse
import pandas as pd

def get_params(config_path):
    with open(config_path) as yaml_file:
        config=yaml.safe_load(yaml_file)
        return config

def get_data(path,seperator):
    data=pd.read_csv(path,sep=seperator)
    return data


if __name__=="__main__":
    args=argparse.ArgumentParser()
    args.add_argument("--config",default="params.yaml")
    parsed_args=args.parse_args()
