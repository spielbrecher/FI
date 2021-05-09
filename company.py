import pandas as pd
import json


class Company:

    def __init__(self):
        self.company_name = 'None'
        self.ticker = 'None'
        self.financials = pd.DataFrame()
        self.models = []  # Прогностические модели. Список моделей для каждого показателя

    def set_company_name(self, company_name):
        self.company_name = company_name

    def set_ticker(self, ticker):
        self.ticker = ticker

    def set_financials(self, financials: pd.DataFrame):
        self.financials = financials

    def set_models(self, models: pd.DataFrame):
        self.models = models

    def add_model(self, model):
        self.models.append(model)

    def get_company_name(self):
        return self.company_name

    def get_ticker(self):
        return self.ticker

    def get_financials(self):
        return self.financials

    def load_company_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            self.company_name = data['company_name']
            self.ticker = data['ticker']
            print(self.company_name)
            print(self.ticker)

    def save_company_to_file(self, filename):
        data = {'company_name': self.company_name, 'ticker': self.ticker}
        with open(filename,'w') as file:
            json.dump(data, file)
