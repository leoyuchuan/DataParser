import sqlite3
import pandas as pd

if __name__ != '__main__':
    exit("Please use this script an main!")

class DataParser(object):
    def load_data(self, path):
        df = pd.read_csv(path, sep="\t", keep_default_na=False)
        if "id" in list(df.columns.values):
            df.set_index("id")
        return df

    def get_db_connection(self, path):
        conn = sqlite3.connect(path)
        conn.text_factory = str
        return conn

    def generate_db(self,
                    input_path="http://www.zurionlinestore.com/sites/all/modules/zurionlinestore/files/google/googlebase.txt",
                    output_path="temp.db",
                    output_table_name="googlebase"):
        df = self.load_data(input_path)
        conn = self.get_db_connection(output_path)
        df.to_sql(output_table_name, conn, if_exists="replace", index=False)

dp = DataParser()
dp.generate_db()




