"""Pega IPs tenando invadir."""

import shutil
from datetime import date
from os import listdir

import pyodbc


def retornar_conexao_sql():
    """Retorna conexão com banco de dados."""
    server = "svexsa020.exsa.local"
    database = "KAV"
    username = "USERKAV"
    password = "abc@1234"
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
       + ";Trusted_Connection=no;"
    )
    return pyodbc.connect(string_conexao)


if __name__ == "__main__":
    conexao = retornar_conexao_sql()
    cursor = conexao.cursor()
    cursor.execute("select * from ev_event where par5 like 'Bruteforce.Generic.Rdp%' and CONVERT(VARCHAR(25), rise_time, 126) like '2022-02-10%' order by rise_time")
    all = cursor.fetchall()

    mdata = date.today()
    print(all)
    print(mdata)

conexao.close()
