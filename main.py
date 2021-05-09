import company


def main():
    mycompany = company.Company()

    mycompany.set_company_name('Сбербанк')
    mycompany.set_ticker('SBER')
    mycompany.save_company_to_file('sber.json')

    mycompany.load_company_from_file('sber.json')




if __name__ == "__main__":
    # execute only if run as a script
    main()