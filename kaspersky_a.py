"""Pega IPs tenando invadir."""

import shutil
from datetime import date
from os import listdir

import pyodbc


def retornar_conexao_sql():
    """Retorna conexão com banco de dados."""
    server = "svexsa026.exsa.local"
    database = "ESL_SORTER"
    username = "esluser"
    password = "exsa@1234"
    string_conexao = (
        "Driver={ODBC Driver 11 for SQL Server};Server="
        + server
        + "\
                     ;Database="
        + database
        + ";UID="
        + username
        + ";PWD="
        + password
       + ";Trusted_Connection=yes;"
    )
    return pyodbc.connect(string_conexao)


if __name__ == "__main__":
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute("select * from pay010")
    all = cursor.fetchall()

    mdata = date.today()
    print(all)
    print(mdata)

conexao.close()
