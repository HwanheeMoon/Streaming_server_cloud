from flask import Flask, session, render_template, redirect, request, url_for
from sqlalchemy.orm import sessionmaker
import pymysql

app = Flask(__name__)

val = 0
cansee = False

@app.route("/video1")
def view1():
    global cansee
    if cansee:
        return render_template("video1.html")
    else:
        return "잘못된 경로"

@app.route("/video2")
def view2():
    global cansee
    if cansee:
        return render_template("video2.html")
    else:
        return "잘못된 경로"


@app.route("/main")
def main():
    global cansee
    if cansee:
        return render_template("main.html")
    else:
        return "잘못된 경로"


@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = pymysql.connect(host='hwanhee.mysql.database.azure.com',port= 3306,user='hwanhee',passwd='ghksgml3517!', db='member',charset='utf8')
    error = None
    if request.method == 'POST':

        id = request.form.get('member_id')
        pw = request.form.get('pw')
        name = request.form.get('name')

        try:
            sql = "INSERT INTO member.member (member_id, pw, name) VALUES ('%s', '%s', '%s')" % (id, pw, name)
            cursor = conn.cursor()
            cursor.execute(sql)
            return render_template("login.html")
        except pymysql.err.IntegrityError:
            error = True
            print(error)
            return "아이디 혹은 비밀번호가 존재합니다."

        
        conn.commit()
        conn.close()

    return render_template('register.html', error=error)

@app.route('/', methods=['GET', 'POST'])
def login():
    global cansee
    conn = pymysql.connect(host='hwanhee.mysql.database.azure.com',port= 3306,user='hwanhee',passwd='ghksgml3517!', db='member',charset='utf8')
    cansee = False
    token = False
    if request.method == 'POST':
        
        id = request.form.get('member_id')
        pw = request.form.get('pw')

        try:
            sql = f"SELECT * FROM member.member WHERE member_id = {id} and pw = {pw}"
            cursor = conn.cursor()
            cursor.execute(sql)
            if not cursor.fetchone():
                return "일치 하지 않음"
            token = True
            cansee = True
            return render_template("main.html")
        except :
            return "회원이 아닙니다."
    conn.commit()
    conn.close()

    if token:
        return render_template("main.html")
    else:
        return render_template("login.html")



if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
