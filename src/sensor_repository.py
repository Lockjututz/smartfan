import psycopg2
from psycopg2.extras import DictCursor, RealDictCursor
from ConfigParser import ConfigParser
from os import environ as envvar

def setupDBConn():
    cfgParser = ConfigParser()
    cfgParser.read('../datasource.ini')
    addr = cfgParser.get('root', 'db.addr')
    portnum = cfgParser.get('root', 'db.port')
    db_name = cfgParser.get('root', 'db.name')
    username = envvar['smartfandb_username']
    passw = envvar['smartfandb_password']
    conn = psycopg2.connect(database=db_name, host=addr, user=username, 
                            password=passw, port=portnum, cursor_factory=DictCursor)
    conn.autocommit = True
    return conn

def storeLogs(logs):
    with setupDBConn() as conn:
        with conn.cursor() as cursor:
            args_str = ','.join(cursor.mogrify("(%(temp)s,%(humid)s,%(timestamp)s)", x) for x in logs)
            cursor.execute("INSERT INTO t_sensor_logs(temperature, humidity, timestamp) VALUES " + args_str)

def getLatestLog():
    with setupDBConn() as conn:
        with conn.cursor(cursor_factory=RealDictCursor) as cursor:
            cursor.execute("SELECT * FROM t_sensor_logs ORDER BY id DESC LIMIT 1")
            return cursor.fetchone()

def getLogsBetween(fromDate, toDate):
    with setupDBConn() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM t_sensor_logs WHERE timestamp >= %s AND timestamp <= %s ORDER BY id DESC", (fromDate, toDate,))
            return cursor.fetchall()
