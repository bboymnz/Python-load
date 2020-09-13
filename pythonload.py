import pandas as pd 
import sqlite3
import os
import sys


def insert_data_into_table(csv_filename):
    """ Creates and Inserts Data given in CSV to sqlite"""
    try:
        database_name = "nba.sqlite"
        csv_filepath = os.path.join(os.getcwd(),csv_filename)
        if os.path.exists(csv_filepath):
            if os.path.exists(database_name):
                os.remove(database_name)
            conn = sqlite3.connect(database_name)
            curr = conn.cursor()
            curr.execute('''CREATE TABLE IF NOT EXISTS  nba ([ ] integer primary key,[Date] text,[Start (ET)] text,[Visitor/Neutral]
            text,[PTS] integer,[Home/Neutral] text,[PTS.1] integer,[Unnamed: 6] text,[Unnamed: 7] text,
            [Attend.] integer,[Notes] text )''')

            conn.commit()

            data = pd.read_csv (csv_filepath)
            df = pd.DataFrame(data, columns= ['Date','Start (ET)','Visitor/Neutral','PTS','Home/Neutral','PTS.1','Unnamed: 6','Unnamed: 7','Attend.','Notes'])
            df.to_sql(name="nba", con=conn,if_exists='append', index=False)
    except Exception as e:
        print(e)



if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Mandatory command line argument missing:- csv filename")
    else:
        csv_filename = sys.argv[1]
        insert_data_into_table(csv_filename)
        






