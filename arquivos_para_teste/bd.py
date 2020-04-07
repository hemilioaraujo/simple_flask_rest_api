import mysql.connector
from mysql.connector import errorcode

class ConectorBD:
    def __init__(self):
        self._conexao = None
        self._cursor = None


    def conectar(self):
        try:
            conn = mysql.connector.connect(host='10.10.10.200', user='root', password='sa',
                                                    database='nideal')
            self._conexao = conn
            self._cursor = conn.cursor()
            print('Conectado!')
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)


    def desconectar(self):
        self._cursor.close()
        self._conexao.close()
        print('Desconectado!')


    def pesquisa_ambiental_linha2_diario(self, data):
        self.conectar()
        self._cursor.callproc("PesquisaAmbientalLinha2Diario", [f'{data}', ])

        for result in self._cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)

        self.desconectar()


    def pesquisa_ambiental_linha2_lme(self):
        self.conectar()
        self._cursor.callproc("PesquisaAmbientalLinha2_LME", [])

        for result in self._cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)

        self.desconectar()


    def pesquisa_ambiental_linha2_diario_total(self, data):
        self.conectar()
        self._cursor.callproc("PesquisaAmbientalLinha2Diario_Total", [f'{data}', ])

        for result in self._cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)

        self.desconectar()


    def pesquisa_ambiental_linha2_mensal(self, data):
        self.conectar()
        self._cursor.callproc("PesquisaAmbientalLinha2Mensal", [f'{data}', ])

        for result in self._cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)

        self.desconectar()


    def pesquisa_ambiental_linha2_estatistica_lme(self, inicio, fim):
        self.conectar()
        self._cursor.callproc("PesquisaAmbientalLinha2_Estatistica_LME", [f'{inicio}', f'{fim}' ])

        for result in self._cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)

        self.desconectar()


if __name__ == "__main__":
    con = ConectorBD()
    # con.conectar()
    # print('conectou')
    # con.desconectar()
    # print('desconectou')
        # PRIMEIRA PLANILHA LINHA 2 - DIÁRIO
    # con.pesquisa_ambiental_linha2_lme()
    # con.pesquisa_ambiental_linha2_diario('2020-04-06')
    # con.pesquisa_ambiental_linha2_diario_total('2020-04-06')
        # SEGUNDA PLANÍLHA LINHA 2 - MENSAL
    # con.pesquisa_ambiental_linha2_mensal('2020-03-01')
    con.pesquisa_ambiental_linha2_estatistica_lme('2020-03-01 00:00:00', '2020-03-31 23:59:59')