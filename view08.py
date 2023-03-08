import sqlite3 as lite

con = lite.connect("Form.db")

#CRUD

#inserir dados
def inserir_form(i):
    
    with con:
        cur = con.cursor()
        query = "INSERT INTO formulario(DTREGISTRO,NUMBONUS,DTENTRADA,NUMNOTAENT,NUMLOTE,CODPROD,FABRICANTE,DTFABRICACAO,DTVALIDADE,QT) VALUES(?,?,?,?,?,?,?,?,?,?)"
        cur.execute(query,i)

#Atualizar dados
def atualizar_formu(i):
    with con:
        cur = con.cursor()
        query = "UPDATE formulario SET DTREGISTRO=?, NUMBONUS=? ,DTENTRADA=?, NUMNOTAENT=?, NUMLOTE=?, CODPROD=?, FABRICANTE=?, DTFABRICACAO=?, DTVALIDADE=?, QT=? WHERE ID=?"
        cur.execute(query,i)

#deletar dados
def deletar_formu(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM formulario WHERE id=?"
        cur.execute(query,i)


#ver dados
def ver_formu():
    ver_dados = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario"
        cur.execute(query)

        rows = cur.fetchall()
        for row in rows:
            ver_dados.append(row)
    return ver_dados

#ver dados
def ver_item(id):
    ver_dados_individual= []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM formulario WHERE id=?"
        cur.execute(query,id)

        rows = cur.fetchall()
        for row in rows:
            ver_dados_individual.append(row)