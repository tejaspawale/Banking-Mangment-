import pymysql
from flask import Flask,render_template,redirect,request
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("bankbody.html")
@app.route("/insertrecord",methods = ['POST'])
def insert():
    en = int(request.form["AccountNo"])
    n = request.form["Name"]
    a = request.form["MobileNo"]
    e = request.form["Email"]
    s = request.form["DateofBirth"]
    d = request.form["Nationalty"]
    f = request.form["Caste"]
    g = request.form["Gender"]
    h = request.form["Address"]
    j = request.form["AccountType"]
    k = request.form["SecurityQuestion"]
    #first create connection string
    try:
        conn = pymysql.connect(host='localhost',user='root',
                      password='',db='banking_management')
    except Exception as e:
        msg="Connection Error"
    else:
        msg="Connection Create Successfully"
        #fire insert query
    query="INSERT  into banking values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    val=(en,n,a,e,s,d,f,g,h,j,k) #val is a tuple
    #create cursor for run the SQL query
    cur=conn.cursor()
    #Query run then use inbuilt method execute() : it is define in cursor
    #call with object of cursor
    try:
        cur.execute(query,val)
    except Exception as e:
        msg="Query Error"
    else:
        msg="Record insert successfully"
        conn.commit()
        conn.close()
    return render_template("details1bank.html",msg=msg)

@app.route('/showrecord')
def show():
    #first create connection string
    try:
        conn = pymysql.connect(host='localhost',user='root',
                      password='',db='banking_management')
    except Exception as e:
        msg="Connection Error"
    else:
        msg="Connection Create Successfully"

    #fire select query
    query  = "select * from banking"    
    cur = conn.cursor()
    try:
        cur.execute(query)
    except Exception as e:
        msg = "query error"
    else:
        result = cur.fetchall()
        conn.commit()
        conn.close()
    return render_template("showbankdetails.html",result=result)

@app.route('/update/<int:AccountNo>')
def update(AccountNo):
    try:
        conn = pymysql.connect(host='localhost',user='root',
                      password='',db='banking_management')
    except Exception as e:
        msg="Connection Error"
    else:
        msg="Connection Create Successfully"

    cur = conn.cursor()
    query = "select * from banking where AccountNo = %s"
    cur.execute(query,AccountNo)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return render_template("bankupdate.html",result = result)
    else:
        msg = "Record Is Not Found"
        return render_template("result.html",msg=msg)
    
@app.route('/updaterecord',methods=['POST'])    
def updaterecord():
    try:
        conn=pymysql.connect(host='localhost',user='root',password='',
                db='banking_management')
    except Exception as e:
        msg="Connection Error"
    else:
        msg="Connection Create Successfully"
    msg = ''
    if request.method == 'POST':
        data = request.form
        ac = data["AccountNo"]
        na = data["Name"]
        mb = data["MobileNo"]
        em = data["Email"]
        db = data["DateofBirth"]
        na = data["Nationalty"]
        ca = data["Caste"]
        ge = data["Gender"]
        ad = data["Address"]
        act = data["AccountType"]
        seq = data["SecurityQuestion"]

        val = (ac,na,mb,em,db,na,ca,ge,ad,act,seq)
        cur = conn.cursor()
        query = "update banking set Name=%s,MobileNo=%s,Email=%s,DateofBirth=%s,Nationalty=%s,Caste=%s,Gender=%s,Address=%s,AccountType=%s,SecurityQuestion=%s where AccountNo=%s"
        cur.execute(query,val)
       
        conn.commit()
        msg = 'bank Record Updated !'
        return redirect('/showrecord')

    return render_template('bankupdate.html')
@app.route("/delete/<int:AccountNo>")
def delete(AccountNo):
    try:
        conn = pymysql.connect(host = "localhost",user = "root",
                               password="",db = "banking_management")
    except Exception as e:
        msg = "Connection Error"
    else:
        msg = "connection create successfully"
    query = "DELETE FROM banking where AccountNo = %s"
    cursor = conn.cursor()
    cursor.execute(query,AccountNo)
    conn.commit()
    conn.close()
    return redirect("/showrecord")
@app.route('/search/<int:AccountNo>')
def search(AccountNo):
    try:
         conn = pymysql.connect(host = "localhost",user = "root",
                               password="",db = "banking_management")
    except Exception as e:
        msg = "Connection Error"
    else:
        msg = "connection create successfully"
    cur = conn.cursor()
    query = "select * FROM banking where AccountNO=%s"
    cur.execute(query,AccountNo)
    result = cur.fetchall()
    conn.commit()
    conn.close()
    if result:
        return render_template("search.html",result=result)
    else:
         msg="Record Not found"
         return render_template("result.html",msg=msg)

    return redirect('/showrecord')
        

    






#main program
app.run(debug=True,use_reloader=False)
