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

        self.mlp_scaler = StandardScaler()  # Scaler
        self.scaled_financials = pd.DataFrame()  # Scaled financial data for MLP model

    def set_financials(self, financials: pd.DataFrame):
        self.financials = financials

    def get_financials(self):
        return self.financials

    def get_mlp_scaler(self):
        return self.mlp_scaler

    def get_scaled_financials(self):
        return self.scaled_financials

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
        return model, score

    def build_random_forest_regression_model(self, target):
        # Divide financials into target and predictors
        X = self.financials.drop([target], axis=1)
        y = self.financials[target]
        # Build model
        rf = RandomForestRegressor(n_estimators=1000, random_state=42)
        # Train the model on training data
        rf.fit(X, y)
        score = rf.score(X, y)
        # rf_prediction = rf.predict(X)
        print(score)
        return rf, score

    def build_mlp_model(self, target):
        # Divide financials
        X = self.financials.drop([target], axis=1)
        y = self.financials[target]

        # Для нейросети нужен Scaler для нормирования данных
        self.mlp_scaler = StandardScaler()
        self.mlp_scaler.fit(X)
        X2 = self.mlp_scaler.transform(X)
        self.scaled_financials = X2
        #  Строим модель
        mlp = MLPRegressor(random_state=None, hidden_layer_sizes=(100,),
                           activation='relu', max_iter=1000, solver='lbfgs')
        mlp.fit(X2, y)
        mlp_score = mlp.score(X2, y)
        #  mlp_prediction = mlp.predict(X2)
        print(mlp_score)
        return mlp, mlp_score

    def build_linear_regression_models_for_all_features(self):
        data = self.financials
        models = []
        for feature in data.columns:
            print(feature)
            model = self.build_linear_regression_model(feature)
            models.append(model)

    def predict(self, model, X: pd.DataFrame, years: list):
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
        featuresList = []
        for year in years:
            features = [year]
            for m in models:
                a = m.predict([[year]])
                features.append(a)
            # На основе спрогнозированных свойств мы прогнозируем курс акций
            featuresList.append(features)
            prediction = model.predict([features])

            # Rewrite prediction if the model is MLPRegressor: we need to scale data with StandardScaler
            if (type(model) is MLPRegressor):
                prediction = model.predict(self.get_mlp_scaler().transform([features]))

            print(f'{year} - {prediction}')
            predictions.append(prediction)

        return featuresList, predictions

