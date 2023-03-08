import sqlite3 as lite

con = lite.connect('Form.db')

def Table_Form():
    cur=con.cursor()

    Query = """CREATE TABLE formulario(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    DTREGISTRO NUMERIC NOT NULL, 
                    NUMBONUS NUMERIC NOT NULL, 
                    DTENTRADA DATE NOT NULL, 
                    NUMNOTAENT NUMERIC NOT NULL, 
                    NUMLOTE NUMERIC NOT NULL, 
                    CODPROD NUMERIC NOT NULL, 
                    FABRICANTE TEXT NOT NULL, 
                    DTFABRICACAO DATE NOT NULL, 
                    DTVALIDADE DATE NOT NULL, 
                    QT NUMERIC NOT NULL)"""
    
    cur.execute(Query)

def Table_User():
    cur = con.cursor()
    Query = """CREATE TABLE usuarios(
                    ID INTEGER PRIMARY KEY AUTOINCREMENT, 
                    NOME TEXT NOT NULL,
                    SENHA TEXT NOT NULL)""" 
    cur.execute(Query)

Table_Form()
Table_User()