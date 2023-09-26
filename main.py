from flask import Flask, render_template, request
import psycopg2



app = Flask(__name__)



@app.route("/", methods=["GET"])
def startpage():
    return render_template('startpage.html')






if __name__ == "__main__":
    app.run(debug=True)