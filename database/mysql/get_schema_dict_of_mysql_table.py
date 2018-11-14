import pymysql  # conda install pymysql


# given a table and schema. derive the schema of a mysql table.`
def get_mysql_schema_dict_of_table(table_name, ms_schema):
    mysql_conn = get_mysql_creds()
    cur = mysql_conn.cursor()
    sql = '''
        SELECT
          COLUMN_NAME
          , ORDINAL_POSITION
          , DATA_TYPE
          , CHARACTER_MAXIMUM_LENGTH
          , COLUMN_TYPE
          , COLUMN_KEY
        FROM INFORMATION_SCHEMA.COLUMNS
        WHERE TABLE_NAME LIKE '<table_name>'
        AND TABLE_SCHEMA LIKE '<schema_name>'
        ;
    '''
    sql = sql.replace('<schema_name>', str(ms_schema))
    sql = sql.replace('<table_name>', str(table_name))
    cur.execute(sql)

    cur.close()
    mysql_conn.close()
    table_schema_dict = {}
    for column_meta in cur:
        column_name = column_meta[0]
        table_schema_dict[column_name] = {
            'column_name': column_name,
            'ordinal_position': column_meta[1],
            'data_type': column_meta[2],
            'character_maximum_length': column_meta[3],
            'column_type': column_meta[4],
            'column_key': column_meta[5],
        }
    # print(table_schema_dict)
    return table_schema_dict


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
