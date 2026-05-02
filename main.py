import numpy as np

import pandas as pd

import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split, KFold, StratifiedKFold, GridSearchCV
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import Perceptron, LogisticRegression
from sklearn.metrics import confusion_matrix, precision_score, recall_score, f1_score
from sklearn.tree import DecisionTreeClassifier, export_text, plot_tree
from sklearn.pipeline import Pipeline

from os import path

from urllib.request import urlretrieve

import opendatasets as od


def main():
    if not path.exists("nasa-near-earth-asteroids-and-close-approaches/asteroid_close_approaches_2015_2035 (1).csv") or not path.exists("nasa-near-earth-asteroids-and-close-approaches/near_earth_asteroids_2025 (1).csv"):
        od.download("https://www.kaggle.com/datasets/darkmatternet/nasa-near-earth-asteroids-and-close-approaches")
    
    data = pd.read_csv("nasa-near-earth-asteroids-and-close-approaches/asteroid_close_approaches_2015_2035 (1).csv").drop("full_name")
    print(data.head(5))
    

if __name__ == "__main__":
    main()