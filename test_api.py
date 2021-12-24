import mysql.connector
from flask import Flask ,request,url_for,jsonify,redirect,render_template
import mysql.connector
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_app")
databasecoursor = mydatabase.cursor()
app = Flask (__name__)
@app.route("/test/<int:d1>-<string:d2>-<string:d3>-<string:d4>-<int:d5>-<string:d6>-<int:d7>-<int:d8>")
def nias (d1,d2,d3,d4,d5,d6,d7,d8):
    sqlquery = "INSERT INTO products_details(productid, imgurl, title, description, rating, cetegory, percentage, price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_value = (f"{d1}", f"{d2}", f"{d3}", f"{d4}",f"{d5}",f"{d6}",f"{d7}",f"{d8}")
    databasecoursor.execute(sqlquery, sql_value)
    mydatabase.commit()
    return "nais"
if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=4444, debug=True)