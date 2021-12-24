from flask import Flask ,request,url_for,jsonify,redirect,render_template
import mysql.connector
app = Flask (__name__)
@app.route("/")
def homepage():
    return  "nais"
#product details

app = Flask(__name__)
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="classicmodels")
databasecoursor = mydatabase.cursor()
@app.route("/details/products", methods=["GET", "PUT", "PATCH","DELETE"])
def data():
    if request.method == "DELETE":
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
@app.route("/test/<int:d1>-<string:d2>-<string:d3>-<string:d4>-<int:d5>-<string:d6>-<int:d7>-<int:d8>")
#url : http://127.0.0.1:4444/test/223-ada-adad-ad-4554-adaf-34-45
def nias (d1,d2,d3,d4,d5,d6,d7,d8):
    sqlquery = "INSERT INTO products_details(productid, imgurl, title, description, rating, cetegory, percentage, price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_value = (f"{d1}", f"{d2}", f"{d3}", f"{d4}",f"{d5}",f"{d6}",f"{d7}",f"{d8}")
    databasecoursor.execute(sqlquery, sql_value)
    mydatabase.commit()
    return "nais"
if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=4444, debug=True)