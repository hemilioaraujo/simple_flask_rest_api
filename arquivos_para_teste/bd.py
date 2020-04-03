import mysql.connector
from mysql.connector import errorcode


def pesquisa_ambiental_linha2_diario(data):
    try:
        db_connection = mysql.connector.connect(host='10.10.10.200', user='root', password='sa', database='nideal')
        print("Database connection made!")
        cursor = db_connection.cursor()
        cursor.callproc("PesquisaAmbientalLinha2Diario", [f'{data}',])

        for result in cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)
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


def pesquisa_ambiental_linha2_lme():
    try:
        db_connection = mysql.connector.connect(host='10.10.10.200', user='root', password='sa',
                                                database='nideal')
        print("Database connection made!")
        cursor = db_connection.cursor()
        cursor.callproc("PesquisaAmbientalLinha2_LME", [])

        for result in cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)
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


def pesquisa_ambiental_linha2_diario_total(data):
    try:
        db_connection = mysql.connector.connect(host='10.10.10.200', user='root', password='sa',
                                                database='nideal')
        print("Database connection made!")
        cursor = db_connection.cursor()
        cursor.callproc("PesquisaAmbientalLinha2Diario_Total", [f'{data}',])

        for result in cursor.stored_results():
            # print(result.fetchall())
            for i in result:
                print(i)
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
    # pesquisa_ambiental_linha2_diario('2020-04-01')
    # pesquisa_ambiental_linha2_lme()
    pesquisa_ambiental_linha2_diario_total('2020-04-01')


