import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.preprocessing import StandardScaler


class ModelGenerator:

    def __init__(self):
        self.linear_regression_models = []  # List of linear regressions
        self.random_forest_regression_models = []  # List of random forest regressions
        self.mlp_models = []  # List of MLP models

        self.financials = pd.DataFrame()  # financials

    def set_financials(self, financials: pd.DataFrame):
        self.financials = financials

    def get_financials(self):
        return self.financials

    def build_linear_regression_model(self):
        pass

    def build_linear_regression_models_for_all_features(self):
        pass

