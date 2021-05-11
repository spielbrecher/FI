from tkinter import Tk, RIGHT, BOTH, RAISED
import tkinter
from tkinter.ttk import Frame, Button, Style
from pandastable import Table, TableModel
import pandas as pd
import company


class PrognosisFrame(tkinter.Toplevel):

    def __init__(self, parent, predictions, years):
        super().__init__(parent)
        pred = {}
        i = 0
        for p in predictions:
            pred[years[i]] = p
            i+=1

        #self.df = pd.DataFrame({'Name': ['Andy', 'Mary']})
        self.df = pd.DataFrame(pred)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=True, showstatusbar=True)
        self.parent = parent
        self.mycompany = company.Company()
        self.initUI()
        self.style = Style()
        print(self.style.theme_names())
        self.style.theme_use('winnative')
        self.closeButton = Button(self, text="Закрыть", command=self.quit)
        self.closeButton.pack(side=RIGHT, padx=5, pady=5)

    def initUI(self):
        self.parent.title("Fluger Investor 1.00 2021 - Prognosis")
        self.centerWindow()
        self.frame.pack(fill=BOTH, expand=True)
        #  Специальная таблица для DataFrame
        self.table.show()

    def centerWindow(self):
        w = 800
        h = 600
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


