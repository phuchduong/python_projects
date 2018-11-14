import pymysql  # conda install pymysql


# Get the pk column name of a mysql table, given the
# table name.
def get_pk_of_table(table_name):
    mysql_conn = get_mysql_creds()
    cur = mysql_conn.cursor()
    sql = '''
        SELECT column_name
        FROM information_schema.columns
        WHERE table_schema = \'spear_reporting\'
        AND table_name = \'<table_name>\'
        AND column_key = \'PRI\'
        ;
    '''
    sql = sql.replace('<table_name>', str(table_name))
    cur.execute(sql)

    cur.close()
    mysql_conn.close()
    result = cur.fetchone()
    pk_column_name = result[0]
    return pk_column_name


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
