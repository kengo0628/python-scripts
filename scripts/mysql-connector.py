# coding: utf-8
import mysql.connector
import pandas as pd

#mysql接続情報
user = 'YOUR USER NAME HERE'
password = 'YOUR PASSWORD HERE'
host = 'YOUR HOST HERE'
port = 3306 #Default
database = 'YOUR DATABASE NAME HERE'

#クエリを実行した結果を返す
def do_query(query):
    conn = mysql.connector.connect(user=user, password=password, host=host, port=port, database=database)
    if not conn.is_connected():
        conn.ping(True)
    cur = conn.cursor()
    cur.execute(query)
    ret = cur.fetchall()
    cur.close
    conn.close
    return ret

#テーブルのカラムを出力する
def show_columns(table):
    query = 'SHOW COLUMNS FROM %s' % table
    return do_query(query)

#テーブルのカラムを配列で返す
def get_columns(table):
    columns = show_columns(table)
    tmp = []
    for column in columns:
        tmp.append(column[0])
    return tmp

#テーブルのデータをDataFtrameで返す
def select_all(table):
    query = 'SELECT * FROM %s' % table
    return pd.DataFrame(do_query(query), columns=get_columns(table))