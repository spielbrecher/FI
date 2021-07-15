from tkinter import Tk, LEFT, RIGHT, BOTH, TOP, RAISED, messagebox, Label, Entry, StringVar
from tkinter.ttk import Frame, Button, Style
import tkinter
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
from pandastable import Table, TableModel
import pandas as pd


class CorrelationFrame(tkinter.Toplevel):

    def __init__(self, parent, dataframe: pd.DataFrame):
        super().__init__(parent)
        self.correl = dataframe.corr()
        print(self.correl)
        self.plot = plt.matshow(self.correl)
        self.f = Figure(figsize=(6, 5), dpi=100)
        self.a = self.f.add_subplot(111)
        self.a.matshow(self.correl)

        self.canvas = FigureCanvasTkAgg(self.f, master=self)
        self.plot_widget = self.canvas.get_tk_widget()

        self.correl_features = self.correl
        self.correl_features["Features"] = self.correl.columns

        self.df = pd.DataFrame(self.correl_features)
        self.frame = Frame(self, relief=RAISED, borderwidth=1)
        self.table = Table(self.frame, dataframe=self.df,
                           showtoolbar=False, showstatusbar=False)

        self.initUI()

    def initUI(self):
        self.title("Fluger Investor 1.00 2021 - Correlation")
        self.centerWindow()
        # Graphics
        self.canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)
        self.canvas._tkcanvas.pack(side=TOP, fill=BOTH, expand=1)

        #  Специальная таблица для DataFrame
        self.frame.pack(fill=BOTH, expand=True)
        self.table.show()

        self.protocol("WM_DELETE_WINDOW", self.on_closing)

    def centerWindow(self):
        w = 1250
        h = 1000
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.geometry('%dx%d+%d+%d' % (w, h, x, y))

    def on_closing(self):
        self.destroy()