"""
Author:- Sameer Acholkar

User can use this utility to connect to any database on Pelican network
And take actions on that Database.
A user can
1. Insert into database
2. Search an entry into database
3. update Database
4. Delete Database
"""

import cx_Oracle

def connect(schema_name, schema_password, server_ip, container_db):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    #curr.execute("CREATE TABLE {} (table_name, name varchar2(20),roll_no number(20),contact_no number(20))")
    conn.commit()
    conn.close()

def insert(schema_name, schema_password, server_ip, container_db, table_name, LANGCODE, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    curr.execute("INSERT INTO {} VALUES('{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(table_name, LANGCODE, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4))
    conn.commit()
    conn.close()

def delete(schema_name, schema_password, server_ip, container_db, table_name, LANGCODE, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    curr.execute("DELETE FROM {} WHERE LANGCODE='{}' AND MODULECODE='{}' AND ITEMNO='{}' AND LANGDESC1='{}' AND LANGDESC2='{}' AND LANGDESC3='{}' AND LANGDESC4='{}'".format(table_name, LANGCODE, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4))
    conn.commit()
    conn.close()

def update(schema_name, schema_password, server_ip, container_db, table_name, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    curr.execute("UPDATE {} SET MODULECODE='{}' ,LANGDESC1='{}' ,LANGDESC2='{}' ,LANGDESC3='{}' ,LANGDESC4='{}' WHERE ITEMNO='{}'".format(table_name, MODULECODE, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4, ITEMNO))
    conn.commit()
    conn.close()

def view(schema_name, schema_password, server_ip, container_db, table_name):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    print(orcl)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    curr.execute("SELECT * FROM {}".format(table_name))
    rows=curr.fetchall()
    conn.close()
    return rows

def search(schema_name, schema_password, server_ip, container_db, table_name, LANGCODE="", MODULECODE="", ITEMNO="", LANGDESC1="", LANGDESC2="", LANGDESC3="", LANGDESC4=""):
    orcl='{}/{}@{}/{}'.format(schema_name, schema_password, server_ip, container_db)
    conn=cx_Oracle.connect(orcl)
    curr=conn.cursor()
    curr.execute("SELECT * FROM {} WHERE LANGCODE='{}' OR MODULECODE='{}' OR ITEMNO='{}' OR LANGDESC1='{}' OR LANGDESC2='{}' OR LANGDESC3='{}' OR LANGDESC4='{}'".format(table_name, LANGCODE, MODULECODE, ITEMNO, LANGDESC1, LANGDESC2, LANGDESC3, LANGDESC4))
    rows=curr.fetchall()
    conn.close()
    return rows