import json
import config
from typing import Optional
from fastapi import FastAPI
from src.db.Executer import SQLExecuter
from FI.company import Company
from FI.model_generator import ModelGenerator

app = FastAPI()
ex = SQLExecuter(config.DB_NAME)


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


@app.get("/analysis")
def read_item(id: Optional[int] = None):
    company_data = ex.get_company_by_id(id)

    mycompany = Company()

    mycompany.set_financials_excel(f'./FI/data/xlsx/{company_data["file_name"]}.XLSX')

    mycompany.load_financials_from_file()

    mycompany.save_company_to_file(f'./FI/data/json/{company_data["file_name"]}.json')

    mycompany.load_company_from_file(f'./FI/data/json/{company_data["file_name"]}.json')
    mycompany.load_financials_from_file()
    modelgen = ModelGenerator()
    modelgen.set_financials(mycompany.get_financials())

    model, score = modelgen.build_linear_regression_model('Price')

    years = [i for i in range(2021, 2026)]
    fin = mycompany.get_financials()
    fin = fin.drop(["Price"], axis=1)
    featuresList, predictions = modelgen.predict(model, fin, years)

    data = list(map(lambda x: x[0], predictions))

    return {"data": json.dumps(data)}

@app.get("/companys/")
def get_companys():
    companys = ex.get_companys()

    return {"companys": json.dumps(companys)}