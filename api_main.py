import mysql.connector
from flask import Flask, redirect, url_for, render_template, request, jsonify

app = Flask(__name__)
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="classicmodels")
databasecoursor = mydatabase.cursor()
@app.route("/details/customers", methods=["POST", "GET", "PUT", "PATCH","DELETE"])
def data():
    if request.method == "POST":
        sqlquery = "INSERT INTO productlines(productLine,textDescription,htmlDescription,image) VALUES(%s,%s,%s,%s)"
        sql_value=("AbIR23","sadasdasd","Nika","sdsdd")
        databasecoursor.execute(sqlquery,sql_value)
        mydatabase.commit()
        return  "POST"
    elif request.method == "DELETE":
        return "DELETE"
    elif request.method == "PUT":
        return "PUT"
    elif request.method == "GET":
        databasecoursor.execute("SELECT * FROM customers")
        myresults = databasecoursor.fetchall()
        data_table = []
        content = {}
        i = 0
        for row in myresults:
            i = i + 1
            content = {
                "Customer No": i,
                "First Name": row[1],
                "Last Name": row[2],
                "Nickname": row[3],
                "Phone": row[4],
                "Address": row[5],
                "City :": row[7]
            }
            data_table.append(content)
        return jsonify(data_table)
    else:
        return "PATCH"
@app.route("/details/categories/<string:a>")
def categories_data(a):
    sql_query = f"SELECT * FROM productlines WHERE textDescription='{a}'"
    databasecoursor.execute(sql_query)
    myresults = databasecoursor.fetchall()
    data_table = []
    content = {}
    i = 0
    for row in myresults:
        i = i + 1
        content = {
            "Customer No": i,
            "First Name": row[1],
            "Last Name": row[2],
            "Nickname": row[3],
        }
        data_table.append(content)
    return jsonify(data_table)


if __name__ == "__main__":
    print("add")
    app.run(host="127.0.0.1", port=3333, debug=True)
