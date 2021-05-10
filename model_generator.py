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

    def build_linear_regression_model(self, target):
        # Divide financials
        X = self.financials.drop([target], axis=1)
        y = self.financials[target]
        # Build model
        model = LinearRegression()
        model.fit(X, y)
        # Score model
        score = model.score(X, y)
        # prediction = model.predict(X) - for prediction
        print(score)
        return model


    def build_linear_regression_models_for_all_features(self):
        data = self.financials
        models = []
        for feature in data.columns:
            print(feature)
            model = self.build_linear_regression_model(feature)
            models.append(model)

    def predict(self, model: LinearRegression, X: pd.DataFrame, years: list):
        X2 = []  # Хранилище для таблиц Год - Признак
        models = []  # Список обученных линейных регрессионных моделей для каждого признака
        i = 0
        for column in X.columns:
            # Формируем пары Год - Показатель в отдельных таблицах и помещаем в общий список
            if column == "Year":
                continue
            X2.append(X[["Year", column]])
            # Обучаем модель на каждой
            mod = LinearRegression()
            mod.fit(np.array(X2[i]["Year"]).reshape(-1, 1), X2[i][column])
            models.append(mod)
            i += 1
        # Прогнозируем все отобранные свойства для прогнозирования курса акций
        # и добавляем в список features
        predictions = []  # Прогнозы по линейной модели
        # Список лет прогноза
        for year in years:
            features = []
            features.append(year)
            for m in models:
                a = m.predict([[year]])
                features.append(a)
            # На основе спрогнозированных свойств на 2021 мы прогнозируем курс акций
            prediction = model.predict([features])

            print(f'{year} - {prediction}')
            predictions.append(prediction)

