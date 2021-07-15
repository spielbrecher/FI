import os
import tkinter
from tkinter import Tk, Entry, StringVar, Label, BOTH, LEFT, CENTER, RIGHT, RAISED, FLAT, messagebox, Frame
from tkinter.filedialog import askopenfilename
from tkinter.ttk import Button
import company


class AddCompanyFrame(tkinter.Toplevel):

    def __init__(self, parent):
        super().__init__(parent)

        self.company_financials = ""  # file path to financials
        self.company = company.Company()  # new Company object

        self.frame_name = Frame(self, relief=FLAT, borderwidth=0)
        self.frame_ticker = Frame(self, relief=FLAT, borderwidth=0)
        self.frame_financials = Frame(self, relief=FLAT, borderwidth=0)
        self.frame_controls = Frame(self, relief=FLAT, borderwidth=0)

        self.l_name = Label(self.frame_name, text="Company Name")
        self.entry_name = Entry(self.frame_name, width=25, textvariable=StringVar(self, 'New Company Name'))
        self.l_ticker = Label(self.frame_ticker, text="Company Ticker")
        self.entry_ticker = Entry(self.frame_ticker, width=25, textvariable=StringVar(self, 'ABCD'))
        self.l_financials = Label(self.frame_financials, text="Файл финансовых данных")
        self.entry_financials = Entry(self.frame_financials, width=25, textvariable=StringVar(self, ''))
        self.btn_open = Button(self.frame_financials, text="Open Excel file", command=self.open_file)
        self.btn_save_company = Button(self.frame_controls, text="Save Company", command=self.save_company)
        self.btn_close = Button(self.frame_controls, text="Close", command=self.destroy)

        self.initUI()

    def initUI(self):
        self.title("Fluger Investor 1.00 2021 - Add Company")
        self.l_name.pack(side=LEFT, padx=5, pady=5)
        self.entry_name.pack(side=LEFT, padx=5, pady=5)
        self.l_ticker.pack(side=LEFT, padx=5, pady=5)
        self.entry_ticker.pack(side=LEFT, padx=5, pady=5)
        self.l_financials.pack(side=LEFT, padx=5, pady=5)
        self.entry_financials.pack(side=LEFT, padx=5, pady=5)
        self.btn_open.pack(side=LEFT, padx=5, pady=5)
        self.btn_save_company.pack(side=LEFT, padx=5, pady=5)
        self.btn_close.pack(side=RIGHT, padx=5, pady=5)

        self.frame_name.pack(fill=BOTH, expand=False)
        self.frame_ticker.pack(fill=BOTH, expand=False)
        self.frame_financials.pack(fill=BOTH, expand=False)
        self.frame_controls.pack(fill=BOTH, expand=False)


    def open_file(self):
        Tk().withdraw()  # we don't want a full GUI, so keep the root window from appearing
        # show an "Open" dialog box and return the path to the selected file
        filename = askopenfilename(initialdir=os.getcwd(),
                                   title="Open financials file",
                                   filetypes=(("Excel", "*.xlsx"), ("Old Excel", "*.xls"), ("all files", "*.*")))
        self.entry_financials.delete(0, tkinter.END)
        self.entry_financials.insert(0, str(filename))

    def save_company(self):
        self.company.set_company_name(self.entry_name.get())
        self.company.set_ticker(self.entry_ticker.get())
        self.company_financials = self.entry_financials.get()
        self.company.set_financials_excel(self.company_financials)
        filename = os.getcwd()+"/"+self.company.get_company_name()+".json"
        self.company.save_company_to_file(filename)
