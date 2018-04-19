import sys
import sqlite3
import pandas as pd

if __name__ != '__main__':
    exit("Please use this script as main!")

class DataParser(object):
    '''
    This class provides a way to parse a tab delimited file into sqlite3 database.
    '''

    def load_data(self, path):
        '''
        This function loads data from specified path into a pandas DataFrame and returns it.
        If the keyword "id" (small case) exists in column headers, it will be treated as the index.

        Args:
            path (str): The path containing the data set.

        Returns:
            pandas.DataFrame: A pandas DataFrame.
        '''
        try:
            df = pd.read_csv(path, sep="\t", keep_default_na=False)
        except:
            exit("Unexpected Error: \n%s\n%s" % sys.exc_info()[0:2])
        if "id" in list(df.columns.values):
            df.set_index("id")
        return df

    def get_db_connection(self, path):
        '''
        This function creates a sqlite3 to connect to the given path and then return the connection.

        Args:
            path (str): The path that sqlite3 connects to.

        Returns:
            sqlite3.Connection: The connection to the sqlite3 database.

        '''
        try:
            conn = sqlite3.connect(path)
        except:
            exit("Unexpected Error: \n%s\n%s" % sys.exc_info()[0:2])
        conn.text_factory = str
        return conn

    def generate_db(self,
                    input_path="http://www.zurionlinestore.com/sites/all/modules/zurionlinestore/files/google/googlebase.txt",
                    output_path="temp.db",
                    output_table_name="googlebase"):
        '''
        This function generates a table in the sqlite3 database.

        Args:
            input_path (str): The path contains input data.
            output_path (str): The sqlite3 database output path.
            output_table_name (str): The table name in sqlite3 database.
        Returns:
            bool: Returns true if execute successfully.

        '''
        df = self.load_data(input_path)
        conn = self.get_db_connection(output_path)
        try:
            df.to_sql(output_table_name, conn, if_exists="replace", index=False)
        except:
            return False
        return True

params = sys.argv[1:]
help_info = "\n==================================================================================================\n" \
            "Please provide complete input parameters or provide nothing for default.\n\n" \
            "$ python DataParser.py[ <input_path> <output_path> <table_name>]\n\n" \
            "Examples:\n" \
            "$ python DataParser.py " \
            "http://www.zurionlinestore.com/sites/all/modules/zurionlinestore/files/google/googlebase.txt " \
            "temp.db googlebase\n" \
            "or \n" \
            "$ python DataParser.py\n" \
            "==================================================================================================\n"
flag = False
if len(params) == 1 and params[0] == "-h":
    print "Help: %s" % help_info
    exit()
if len(params) == 0:
    dp = DataParser()
    flag = dp.generate_db()
elif len(params) == 3:
    dp = DataParser()
    flag = dp.generate_db(params[0], params[1], params[2])
else:
    exit("Error: The input parameter is not sufficient. %s" % help_info)
if flag:
    exit("The code executed successfully.")
else:
    exit("An error occurs, please use -h argument to see help, correct errors and run again.")
