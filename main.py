import company
import model_generator
from main_frame import MainFrame
from tkinter import Tk, Frame, BOTH


def main():
    mycompany = company.Company()

    mycompany.set_company_name('Татнефть')
    mycompany.set_ticker('TATN')
    mycompany.set_financials_excel('tatneft.XLSX')

    mycompany.load_financials_from_file()

    mycompany.save_company_to_file('tatneft.json')

    mycompany.load_company_from_file('tatneft.json')
    modelgen = model_generator.ModelGenerator()
    modelgen.set_financials(mycompany.get_financials())

    model = modelgen.build_linear_regression_model('Price')
    years = [i for i in range(2021, 2026)]
    fin = mycompany.get_financials()
    fin = fin.drop(["Price"], axis=1)

    modelgen.predict(model, fin, years)

    root = Tk()
    app = MainFrame(root)
    root.mainloop()


if __name__ == "__main__":
    # execute only if run as a script
    main()