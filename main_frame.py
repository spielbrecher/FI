from tkinter import Tk, RIGHT, BOTH, RAISED
from tkinter.ttk import Frame, Button, Style
from pandastable import Table, TableModel


class MainFrame(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
        self.style = Style()
        print(self.style.theme_names())
        self.style.theme_use('clam')

    def initUI(self):
        self.parent.title("Fluger Investor 1.00 2021")
        self.pack(fill=BOTH, expand=1)
        self.centerWindow()
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        df = TableModel.getSampleData()
        self.table = pt = Table(frame, dataframe=df,
                                showtoolbar=True, showstatusbar=True)
        pt.show()

        closeButton = Button(self, text="Закрыть")
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self, text="Готово")
        okButton.pack(side=RIGHT)

        self.pack(fill=BOTH, expand=True)



    def centerWindow(self):
        w = 1024
        h = 768
        sw = self.parent.winfo_screenwidth()
        sh = self.parent.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        self.parent.geometry('%dx%d+%d+%d' % (w, h, x, y))
