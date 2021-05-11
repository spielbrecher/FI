from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from pandastable import Table, TableModel
import pandas as pd
import company
from tkinter.filedialog import askopenfilename
import os


class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        #  Create DataFrame
        self.df = pd.DataFrame({'': ['']})
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=True, showstatusbar=True)
        self.parent = parent
        self.initUI()
        self.style = Style()
        print(self.style.theme_names())
        self.style.theme_use('winnative')

    def initUI(self):
        self.parent.title("Fluger Investor 1.00 2021")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        self.frame.pack(fill=BOTH, expand=True)
        #  Специальная таблица для DataFrame
        self.table.show()


        closeButton = Button(self, text="Закрыть", command=self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        loadButton = Button(self, text="Загрузить", command=self.loadCompany)
        loadButton.pack(side=RIGHT)

        self.pack(fill=BOTH, expand=True)

    def centerWindow(self):
        w = 1200
        h = 800
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def loadCompany(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename(initialdir=os.getcwd(),
                                   title="Открыть компанию",
                                   filetypes=(("json", "*.json"), ("all files", "*.*")))
        mycompany = company.Company()
        mycompany.load_company_from_file(filename)
        mycompany.load_financials_from_file()
        self.df = mycompany.get_financials()
        print(self.df)
        self.table.model.df = self.df
        self.table.redraw()
        self.parent.title("Fluger Investor 1.00 2021 - "+mycompany.ticker)
        #self.table.show()

