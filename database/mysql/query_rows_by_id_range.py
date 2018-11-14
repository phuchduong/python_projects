# Query a mysql table with a start and end id. Must be a numeric
#   dat type.
def mysql_query_rows_by_id_range(table_name, column_name, start, end):
    mysql_conn = get_mysql_creds()
    cur = mysql_conn.cursor()
    sql = '''
        SELECT
          *
        FROM '<table_name>'
        WHERE <column_name>
            BETWEEN '<start>'
                AND '<end>'
        ;
    '''
    sql = sql.replace('<start>', str(start))
    sql = sql.replace('<end>', str(end))
    sql = sql.replace('<table_name>', table_name)
    sql = sql.replace('<column_name>', column_name)
    cur.execute(sql)

    cur.close()
    mysql_conn.close()
    return cur


def get_mysql_creds():
    # Reference:
    # https://github.com/PyMySQL/PyMySQL/blob/master/example.py
    conn = pymysql.connect(
        host='<mysql_name>.<ec2_hash>.us-west-2.rds.amazonaws.com',
        port=3306,
        user='<my_username>',
        passwd='<my_pass>',
        db='my_db_name',
        charset='utf8'
    )
    return conn
