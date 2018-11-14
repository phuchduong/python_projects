import pymysql  # conda install pymysql


def get_max_id_of_table(table_name, column_name):
    mysql_conn = get_mysql_creds()
    cur = mysql_conn.cursor()
    sql = '''
        SELECT
          max(<pk_column_name>)
        FROM <table_name>
        ;
    '''
    sql = sql.replace('<table_name>', str(table_name))
    sql = sql.replace('<pk_column_name>', str(column_name))
    cur.execute(sql)

    cur.close()
    mysql_conn.close()
    result = cur.fetchone()
    max_id = result[0]
    return max_id


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
