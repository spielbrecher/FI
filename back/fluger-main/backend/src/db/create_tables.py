import sqlite3
import config


def create_company(conn, cur):
    cur.execute("""
        CREATE TABLE IF NOT EXISTS companys(
            company_id INT PRIMARY KEY,
            name TEXT,
            file_name TEXT);
    """)

    conn.commit()


def main():
    conn = sqlite3.connect(config.DB_NAME)
    cur = conn.cursor()

    create_company(conn, cur)


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)