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
    od.download("https://www.kaggle.com/datasets/darkmatternet/nasa-near-earth-asteroids-and-close-approaches")
    

if __name__ == "__main__":
    main()