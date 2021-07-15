from tkinter import Tk, RIGHT, BOTH, RAISED, TOP, BOTTOM
import tkinter
from tkinter.ttk import Frame, Button, Style
from pandastable import Table, TableModel
import pandas as pd
import company
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


class PrognosisFrame(tkinter.Toplevel):

    def __init__(self, parent, predictions, years):
        super().__init__(parent)
        self.parent = parent

        pred = {}
        i = 0
        for p in predictions:
            pred[years[i]] = p
            i+=1

        self.df = pd.DataFrame(pred)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=False, showstatusbar=False)
        # График
        self.f = Figure(figsize=(5, 4), dpi=100)
        self.a = self.f.add_subplot(111)
        years_str = [str(y) for y in years]
        self.a.plot(years_str, predictions)
        # a tk.DrawingArea
        self.canvas = FigureCanvasTkAgg(self.f, master=self)

        self.mycompany = company.Company()

        self.style = Style()
        print(self.style.theme_names())
        self.style.theme_use('winnative')
        self.closeButton = Button(self, text="Закрыть", command=self.on_closing)
        self.closeButton.pack(side=BOTTOM, padx=5, pady=5)

        self.initUI()

    def initUI(self):
        self.title("Fluger Investor 1.00 2021 - Prognosis")
        self.centerWindow()
        # Graphics
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)
        #  Специальная таблица для DataFrame
        self.frame.pack()
        self.table.show()
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def on_closing(self):
        self.destroy()

    def centerWindow(self):
        w = 800
        h = 600
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))


