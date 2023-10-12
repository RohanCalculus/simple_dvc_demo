# Import libraries
import os
import yaml
import pandas as pd
import argparse

# This function reads a YAML configuration file and returns its contents as a dictionary
def read_params(config_path):
    with open(config_path) as yaml_file:
        config = yaml.safe_load(yaml_file)
    return config

# This function reads data from a source specified in the configuration file
def get_data(config_path):
    config = read_params(config_path)
    data_path = config["data_source"]["s3_source"]
    df = pd.read_csv(data_path, sep=",", encoding='utf-8')
    return df

# Initialize command-line argument parsing
if __name__=="__main__":
    args = argparse.ArgumentParser()
    args.add_argument("--config", default="params.yaml")
    parsed_args = args.parse_args()
    data = get_data(config_path=parsed_args.config)
    

