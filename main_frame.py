from tkinter import Tk, RIGHT, BOTH, RAISED, messagebox, Label, Entry, StringVar
import tkinter
from tkinter.ttk import Frame, Button, Style
from pandastable import Table, TableModel
import pandas as pd
import company
from tkinter.filedialog import askopenfilename
import os

import model_generator
import prognosis_frame


class MainFrame(Tk):
    def __init__(self):
        super().__init__()
        #  Create DataFrame
        self.df = pd.DataFrame({'': ['']})
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=True, showstatusbar=True)
        #self.parent = parent
        self.mycompany = company.Company()
        self.initUI()
        self.style = Style()
        print(self.style.theme_names())
        self.style.theme_use('winnative')
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


    def initUI(self):
        self.title("Fluger Investor 1.00 2021")
        #self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.frame.pack(fill=BOTH, expand=True)
        #  Специальная таблица для DataFrame
        self.table.show()
        #self.pack(fill=BOTH, expand=True)

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
        modelgen = model_generator.ModelGenerator()
        modelgen.set_financials(self.mycompany.get_financials())
        model, score = modelgen.build_linear_regression_model('Price')
        self.mycompany.set_price_model(model)
        messagebox.showinfo("Модель", "Модель создана, score = "+str(score))

    def prognosis(self):
        f = self.entry_from.get()
        t = self.entry_to.get()
        years = [i for i in range(int(f), int(t))]
        fin = self.mycompany.get_financials()
        fin = fin.drop(["Price"], axis=1)
        modelgen = model_generator.ModelGenerator()
        features, predictions = modelgen.predict(self.mycompany.get_price_model(), fin, years)
        print(features)
        prognosis_frame.PrognosisFrame(self, predictions, years)






