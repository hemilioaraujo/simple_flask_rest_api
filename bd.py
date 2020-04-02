import mysql.connector
from mysql.connector import errorcode

# SELECT PARA LIMITES MÉDIOS DIÁRIOS
# SELECT CO, NOX, THC, OPAC, SO2 FROM ambientallinha2_lme;

def pesquisaAmbientalLinha2Diario(data):
    try:
        db_connection = mysql.connector.connect(host='10.10.10.200', user='root', password='sa', database='nideal')
        print("Database connection made!")
        cursor = db_connection.cursor()
        cursor.callproc("PesquisaAmbientalLinha2Diario", [f'{data}',])
        for result in cursor.stored_results():
            print(result.fetchall())

        print("ok")

    except mysql.connector.Error as error:
        if error.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database doesn't exist")
        elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("User name or password is wrong")
        else:
            print(error)
    else:
        db_connection.close()

if __name__ == "__main__":
    pesquisaAmbientalLinha2Diario('2020-03-24')


