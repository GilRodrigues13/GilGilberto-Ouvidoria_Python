from sqlite3 import Cursor
import mysql.connector
 

class Sugestao:
    connection = mysql.connector.connect(
                    host = 'localhost',
                    user = 'root',
                    password = 'A01561313',
                    database = 'ouvidoria'          
                )   

    cursor = connection.cursor()
        
    def __init__(self):
         pass

    def adicionar_Ocorrencia(self, nome, texto):
        
        sql = 'INSERT INTO ocorrencias (nome, descri) values (%s, %s)'
        data = (nome, texto)

        self.cursor.execute(sql, data)
        self.connection.commit()
        

      
    def lista_sugestao(self):
        sql = 'SELECT * FROM ocorrencias'
        
        self.cursor.execute(sql)
        listasugestao = self.cursor.fetchall()
        

        print('-' * 50)
        print('Todas as sugestões:')

        for ocorrencia in listasugestao:
            print(ocorrencia[0], ocorrencia[1], ocorrencia[2])
           
        

    def deletar_sugestao(self,indice):
        
        self.lista_sugestao()
        sql = 'DELETE FROM ocorrencias where id= %s'
        data = (indice,)
        self.cursor.execute(sql,data)
        self.connection.commit()

    def deletar_allsugestao(self):
        
        sql = 'DELETE FROM ocorrencias'
        self.cursor.execute(sql)
        self.connection.commit()


            
            
          
            
            
            
            



