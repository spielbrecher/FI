import sqlite3
import config


class SQLExecuter:
    def __init__(self, path_to_db):
        self.conn = sqlite3.connect(path_to_db, check_same_thread=False)
        self.cur = self.conn.cursor()

    def get_companys(self):
        self.cur.execute("""
                SELECT *
                FROM companys;
            """)

        companys_raw = self.cur.fetchall()
        companys = []

        for company_raw in companys_raw:
            companys.append({
                "id": int(company_raw[0]),
                "name": str(company_raw[1])
            })

        return companys

    def get_company_by_id(self, company_id):
        self.cur.execute(f"""
                SELECT *
                FROM companys
                WHERE company_id = {company_id};
            """)

        company_raw = self.cur.fetchone()

        company = {
            "id": int(company_raw[0]),
            "name": str(company_raw[1]),
            "file_name": str(company_raw[2])
        }

        return company



