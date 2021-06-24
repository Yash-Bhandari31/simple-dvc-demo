# Load train, test data files
# train the models
# evaluate the models

import os
import sys
import argparse
import joblib
import json
import pandas as pd
import numpy as np
from scipy.sparse.construct import random
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.model_selection import train_test_split
from sklearn.linear_model import ElasticNet
from get_data import read_params

def train_and_evaluate(config_path):
    config = read_params(config_path)
    test_data_path = config["split_data"]["test_path"]
    train_data_path = config["split_data"]["train_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dir"]

    alpha = config["estimators"]["ElasticNet"]["params"]["alpha"]
    l1_ratio = config["estimators"]["ElasticNet"]["params"]["l1_ratio"]

    target = [config["base"]["target_col"]]

    train = pd.read_csv(train_data_path, sep = ",")
    test = pd.read_csv(test_data_path, sep = ",")

    train_y = train[target]
    test_y = test[target]

    train_x = train.drop(target, axis = 1)
    test_x = test.drop(target, axis = 1)

    lr = ElasticNet(alpha=alpha, 
                    l1_ratio=l1_ratio, 
                    random_state=random_state)

    lr.fit(train_x, train_y)
    predicted_qualities = lr.predict(test_x)

def eval_metices(actual, pred):
    rmse = np.
    (rmse, mae, r2) = eval_metices(test_y, predicted_qualities)

















if __name__ == "__main__":
        args = argparse.ArgumentParser()
    args.add_argument("--config", default = "params.yaml")
    parsed_args = args.parse_args()
    split_and_saved_data(config_path=parsed_args.config)