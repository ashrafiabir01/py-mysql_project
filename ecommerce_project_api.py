from flask import Flask ,request,url_for,jsonify,redirect,render_template
import mysql.connector
app = Flask(__name__)
mydatabase = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="ecommerce_app")
databasecoursor = mydatabase.cursor()
@app.route("/details/products")
#url : http://127.0.0.1:3333/details/products
def get_product_details():
    databasecoursor.execute("SELECT * FROM products_details")
    myresults = databasecoursor.fetchall()
    data_table = []
    content = {}
    i = 0
    for row in myresults:
        i = i + 1
        content = {
            "product id": row[0],
            "imgutl": row[1],
            "title": row[2],
            "descriptions": row[3],
            "rating": row[4],
            "category": row[5],
            "percentage": row[6],
            "price": row[7]
        }
        data_table.append(content)
    return jsonify(data_table)
@app.route("/details/categories/<string:a>")
#url : http://127.0.0.1:3333/details/categories/shirt
def categories_data(a):
    sql_query = f"SELECT * FROM products_details WHERE cetegory='{a}'"
    databasecoursor.execute(sql_query)
    myresults = databasecoursor.fetchall()
    data_table = []
    content = {}
    i = 0
    for row in myresults:
        i = i + 1
        content = {
            "product id": row[0],
            "imgutl": row[1],
            "title": row[2],
            "descriptions": row[3],
            "rating": row[4],
            "category": row[5],
            "percentage": row[6],
            "price": row[7]
        }
        data_table.append(content)
    return jsonify(data_table)
@app.route("/details/products/add/<int:d1>-<string:d2>-<string:d3>-<string:d4>-<int:d5>-<string:d6>-<int:d7>-<int:d8>")
#url : http://127.0.0.1:3333/details/products/add/223-ada-adad-ad-4554-adaf-34-45
def add_products (d1,d2,d3,d4,d5,d6,d7,d8):
    sqlquery = "INSERT INTO products_details(productid, imgurl, title, description, rating, cetegory, percentage, price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s)"
    sql_value = (f"{d1}", f"{d2}", f"{d3}", f"{d4}",f"{d5}",f"{d6}",f"{d7}",f"{d8}")
    databasecoursor.execute(sqlquery, sql_value)
    mydatabase.commit()
    return "ok"
@app.route("/details/products/delete/<string:a>")
# url : http://127.0.0.1:3333/details/products/delete/223
def delete_product (a):
    databasecoursor.execute(f"DELETE FROM products_details WHERE products_details.productid = {a}")
    mydatabase.commit()
    return "ok"
if __name__ == "__main__" :
    app.run(host="127.0.0.1", port=3333, debug=True)
