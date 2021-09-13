from FI.company import Company
from FI.model_generator import ModelGenerator
import json

mycompany = Company()

mycompany.set_financials_excel('./FI/data/xlsx/tatneft.XLSX')

mycompany.load_financials_from_file()

mycompany.save_company_to_file('./FI/data/json/tatneft.json')

mycompany.load_company_from_file('./FI/data/json/tatneft.json')
mycompany.load_financials_from_file()
modelgen = ModelGenerator()
modelgen.set_financials(mycompany.get_financials())

model, score = modelgen.build_linear_regression_model('Price')

years = [i for i in range(2021, 2026)]
fin = mycompany.get_financials()
fin = fin.drop(["Price"], axis=1)
featuresList, predictions = modelgen.predict(model, fin, years)
print("-------------")
# print(type(str(predictions)))
data = list(map(lambda x: x[0], predictions))
