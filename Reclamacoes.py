from sqlite3 import Cursor
import mysql.connector


class Reclamacoes:
    connection = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'A01561313',
                    database = 'ouvidoria'         
                )   

    cursor = connection.cursor()
        
    def __init__(self):
         pass

    def adicionar_Reclamacoes(self, nome, texto):
        
        sql = 'INSERT INTO reclamacoes (nome, descri) values (%s, %s)'
        data = (nome, texto)

        self.cursor.execute(sql, data)
        self.connection.commit()
        

      
    def lista_reclamacoes(self):
        sql = 'SELECT * FROM reclamacoes'
        
        self.cursor.execute(sql)
        listareclamacoes = self.cursor.fetchall()
        

        print('-' * 50)
        print('Todas as reclamações:')

        for reclamacoes in listareclamacoes:
            print(reclamacoes[0], reclamacoes[1], reclamacoes[2])
           
        

    def deletar_reclamacoes(self,indice):
        
        self.lista_reclamacoes()
        sql = 'DELETE FROM reclamacoes where id= %s'
        data = (indice,)
        self.cursor.execute(sql,data)
        self.connection.commit()

    def deletar_allreclamacoes(self):
        
        sql = 'DELETE FROM reclamacoes'
        self.cursor.execute(sql)
        self.connection.commit()