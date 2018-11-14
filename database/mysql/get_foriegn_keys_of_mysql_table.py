import pymysql  # conda install pymysql


# given a mysql table and schema. derive the foriegn keys of a table.
def get_foreign_key_references_of_mysql_table(ms_schema_name, ms_table_name):
    mysql_conn = get_mysql_creds()
    cur = mysql_conn.cursor()
    sql = '''
        SELECT
          COLUMN_NAME
        FROM INFORMATION_SCHEMA.KEY_COLUMN_USAGE
        WHERE CONSTRAINT_SCHEMA LIKE '<ms_schema_name>'
        AND REFERENCED_TABLE_NAME IS NOT NULL
        AND TABLE_NAME LIKE '<ms_table_name>'
        ;
    '''
    sql = sql.replace('<ms_schema_name>', str(ms_schema_name))
    sql = sql.replace('<ms_table_name>', str(ms_table_name))

    cur.execute(sql)

    cur.close()
    mysql_conn.close()
    foreign_key_tuple = cur.fetchall()
    return foreign_key_tuple


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
