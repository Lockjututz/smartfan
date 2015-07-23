import psycopg2
from psycopg2.extras import DictCursor
from ConfigParser import ConfigParser
from datetime import datetime
from os import environ as envvar

def setupDBConn(self):
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
    pass

def getLatestLog():
    pass

def getLogsBetween(fromDate, toDate):
    pass
