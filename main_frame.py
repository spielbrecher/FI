from tkinter import Tk, LEFT, RIGHT, BOTH, RAISED, messagebox, Label, Entry, StringVar
import tkinter
from tkinter.ttk import Frame, Button, Style, Combobox
from pandastable import Table, TableModel
import pandas as pd
import company
from tkinter.filedialog import askopenfilename
import os

import correlation_frame
import model_generator
import prognosis_frame
import add_company_frame

from sklearn.preprocessing import StandardScaler

class MainFrame(Tk):
    def __init__(self):
        super().__init__()
        #  Create DataFrame with financials at the North of the window
        self.df = pd.DataFrame({'': ['']})
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=True, showstatusbar=True)

        # Link to the company for analysis
        self.mycompany = company.Company()

        # Model generator
        self.modelgen = model_generator.ModelGenerator()

        # Initialize the user interface
        self.initUI()
        self.style = Style()

        # Just printing in console list of available styles
        print(self.style.theme_names())

        # By default - windows native style
        self.style.theme_use('winnative')

        # Create buttons at South of the frame
        self.closeButton = Button(self, text="Закрыть", command=self.quit)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)
        self.loadButton = Button(self, text="Загрузить", command=self.loadCompany)
        self.loadButton.pack(side=RIGHT)
        self.modelButton = Button(self, text="Модель", command=self.createModel)
        self.modelButton.pack(side=RIGHT)
        self.prognosisButton = Button(self, text="Прогноз", command=self.prognosis)
        self.prognosisButton.pack(side=RIGHT)
        self.l1 = Label(self, text='От')
        self.l2 = Label(self, text='До')
        self.entry_from = Entry(self, width=4, textvariable=StringVar(self, '2021'))
        self.entry_to = Entry(self, width=4, textvariable=StringVar(self, '2026'))
        self.entry_to.pack(side=RIGHT, padx=5)
        self.l2.pack(side=RIGHT)
        self.entry_from.pack(side=RIGHT, padx=5)
        self.l1.pack(side=RIGHT)
        # List of accessible models for price prognosis
        self.combo_model_type = Combobox(self, values=["Linear", "Random Forest", "MLP"])
        self.combo_model_type.current(0) # Linear by default
        self.combo_model_type.pack(side=RIGHT)
        self.newCompanyButton = Button(self, text="Новая компания", command=self.newCompany)
        self.newCompanyButton.pack(side=LEFT, padx=5)
        self.correlationButton = Button(self, text="Корреляции", command=self.correlation)
        self.correlationButton.pack(side=LEFT, padx=5)


    def initUI(self):
        self.title("Fluger Investor 1.00 2021")
        self.centerWindow()
        self.frame.pack(fill=BOTH, expand=True)
        # Special table for DataFrame
        self.table.show()


    def centerWindow(self):
        w = 1200
        h = 800
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def loadCompany(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename(initialdir=os.getcwd(),
                                   title="Открыть компанию",
                                   filetypes=(("json", "*.json"), ("all files", "*.*")))
        self.mycompany = company.Company()
        self.mycompany.load_company_from_file(filename)
        self.mycompany.load_financials_from_file()
        self.df = self.mycompany.get_financials()
        print(self.df)
        self.table.model.df = self.df
        self.table.redraw()
        self.title("Fluger Investor 1.00 2021 - "+self.mycompany.ticker)

    def createModel(self):
        #modelgen = model_generator.ModelGenerator()
        self.modelgen.set_financials(self.mycompany.get_financials())
        # Get the type of model needed
        model_type = self.combo_model_type.get()
        # Create model according to choice
        if (model_type=="Linear"):
            model, score = self.modelgen.build_linear_regression_model('Price')
            messagebox.showinfo("Модель", "Линейная модель создана, score = " + str(score))
            self.mycompany.set_price_model(model)
        elif (model_type=="Random Forest"):
            model, score = self.modelgen.build_random_forest_regression_model('Price')
            messagebox.showinfo("Модель", "Random Forest модель создана, score = " + str(score))
            self.mycompany.set_price_model(model)
        elif (model_type=="MLP"):
            model, score = self.modelgen.build_mlp_model('Price')
            messagebox.showinfo("Модель", "Модель многослойного перцептрона создана, score = " + str(score))
            self.mycompany.set_price_model(model)

    def prognosis(self):
        # Years from form fields From and To
        f = self.entry_from.get()
        t = self.entry_to.get()
        years = [i for i in range(int(f), int(t))]
        fin = self.mycompany.get_financials()
        fin = fin.drop(["Price"], axis=1)
        #modelgen = model_generator.ModelGenerator()
        features, predictions = self.modelgen.predict(self.mycompany.get_price_model(), fin, years)

        print("-- prediction --")
        print(predictions)
        print(features)
        prognosis_frame.PrognosisFrame(self, predictions, years)

    def newCompany(self):
        add_company_frame.AddCompanyFrame(self)

    def correlation(self):
        correlation_frame.CorrelationFrame(self, self.df)







