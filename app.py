'''from flask import Flask 
app=Flask(__name__)
@app.route('/')
def welcome():
    return"Welcome to flask development"
#@app.route('/success/<int:score>')
#def success(score):
    #return "hi score is"+str(score)
if __name__=='main':
    app.run(debug=True)'''
from flask import Flask,render_template,request,url_for
#from flask_db2 import DB2
import ibm_db
dsn_hostname = "8e359033-a1c9-4643-82ef-8ac06f5107eb.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "dhx96267"
dsn_pwd = "ur9uHbNb9pOyD6z3" 
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"  
dsn_port = "30120"  
dsn_protocol = "TCPIP"  
dsn_security = "SSL"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,dsn_security)

conn = ibm_db.connect(dsn, "", "")

print(conn)
print("Connection Successful............")
'''createQuery = "create Table HI(ID INTEGER PRIMARY KEY NOT NULL,First_Name VARCHAR(20))"
create_table = ibm_db.exec_immediate(conn, createQuery)
insertQuery="insert into HI values(1,'hima')"
insert_table=ibm_db.exec_immediate(conn, insertQuery)'''
app=Flask(__name__)

@app.route('/')
def welcome():
    return render_template("index.html")
@app.route('/jobseeker',methods=['POST','GET'])
def jobseeker():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        #address = request.form['address']
        age = request.form['age']
        skills = request.form['skills']
        expectedjob = request.form['expectedjob']

        #if password!=cp:
            #return render_template('register.html')

        try:
            insert_sql = "INSERT INTO REGISTER_AS_REGISTER VALUES (?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, email)
            ibm_db.bind_param(prep_stmt, 3, password)
            ibm_db.bind_param(prep_stmt, 4, age)
            ibm_db.bind_param(prep_stmt, 5, skills)
            ibm_db.bind_param(prep_stmt, 6, expectedjob)
            ibm_db.execute(prep_stmt)
            #sql = "insert into REGISTER_AS_REGISTER values ('{}','{}','{}','{}','{}','{}')".format( name, email, password, age, skills, expectedjob)
            #stmt = ibm_db.exec_immediate(conn,sql)
            print("No of Affected rows: ",ibm_db.num_rows(prep_stmt))
        except:
            print("Error: ",ibm_db.stmt_errormsg())
    return render_template("registerasjobseeker.html")
@app.route('/organization',methods=['POST','GET'])
def organization():
    if request.method == 'POST':
        organization_name = request.form['organization_name']
        job_role = request.form['job_role']
        lpa = request.form['lpa']
        #address = request.form['address']
        city = request.form['city']
        email = request.form['email']
        mobile = request.form['mobile']

        #if password!=cp:
            #return render_template('register.html')

        try:
            insert_sql = "INSERT INTO REGISTER_AS_ORGANIZATION VALUES (?,?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, organization_name)
            ibm_db.bind_param(prep_stmt, 2, job_role)
            ibm_db.bind_param(prep_stmt, 3, lpa)
            ibm_db.bind_param(prep_stmt, 4, city)
            ibm_db.bind_param(prep_stmt, 5, email)
            ibm_db.bind_param(prep_stmt, 6, mobile)
            ibm_db.execute(prep_stmt)
            #sql = "insert into REGISTER_AS_REGISTER values ('{}','{}','{}','{}','{}','{}')".format( name, email, password, age, skills, expectedjob)
            #stmt = ibm_db.exec_immediate(conn,sql)
            print("No of Affected rows: ",ibm_db.num_rows(prep_stmt))
        except:
            print("Error: ",ibm_db.stmt_errormsg())
    return render_template("registerasorganization.html")
@app.route('/login',methods=['POST','GET'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        sql = "SELECT * FROM user REGISTER_AS_REGISTER email =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, email)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            if (password == str(account['PASS']).strip()):
                return render_template('index.html')
            else:
                return render_template('login.html', msg="Password is invalid")
        else:
            return render_template('registerasjobseeker.html')
    else:
        return render_template('login.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/recommend')
def recommend():
    return render_template('recommend.html')
@app.route('/manualrecommendation')
def manualrecommendation():
    return render_template("manual.html")
@app.route('/chatbotrecommendation')
def chatbotrecommendation():
    return render_template("chatbot.html")
@app.route('/chatbotrecon')
def chatbotcon():
    return render_template("chatconversation.html")
if __name__=='main':
    app.run(debug=True)



#from flask import Flask,render_template,request'''
'''from flask_db2 import DB2
import ibm_db
dsn_hostname = "0c77d6f2-5da9-48a9-81f8-86b520b87518.bs2io90l08kqb1od8lcg.databases.appdomain.cloud"
dsn_uid = "why11914"
dsn_pwd = "qMCrggTKEsZ8b54q" 
dsn_driver = "{IBM DB2 ODBC DRIVER}"
dsn_database = "bludb"  # e.g. "BLUDB"
dsn_port = "31198"  # e.g. "32733"
dsn_protocol = "TCPIP"  # i.e. "TCPIP"
dsn_security = "SSL"
dsn = (
    "DRIVER={0};"
    "DATABASE={1};"
    "HOSTNAME={2};"
    "PORT={3};"
    "PROTOCOL={4};"
    "UID={5};"
    "PWD={6};"
    "SECURITY={7};").format(dsn_driver, dsn_database, dsn_hostname, dsn_port, dsn_protocol, dsn_uid, dsn_pwd,
                            dsn_security)

conn = ibm_db.connect(dsn, "", "")

print(conn)
print("Connection Successful............")
#app = Flask(__name__,template_folder='templates')'''
'''
@app.route('/')
def welcome():
    return render_template("index.html")

@app.route('/jobseeker')
def jobseeker():
    return render_template("registerasjobseeker.html")


@app.route('/organization')
def organization():
    return render_template("registerasorganization.html")
@app.route('/recommend')
def recommend():
    return render_template("recommend.html")
@app.route('/manualrecommendation')
def manualrecommendation():
    return render_template("manual.html")
@app.route('/chatbotrecommendation')
def chatbotrecommendation():
    return render_template("chatconversation.html")
@app.route('/chatbotrecon')
def chatbotcon():
    return render_template('chatconversation.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        name = request.form['registerFullName']
        username = request.form['registerUsername']
        email = request.form['registerEmailid']
        password = request.form['registerPassword1']
        repass=request.form['registerPassword2']

        sql = "SELECT * FROM COUSTMER_DETAILS  WHERE name =?"
        stmt = ibm_db.prepare(conn, sql)
        ibm_db.bind_param(stmt, 1, name)
        ibm_db.execute(stmt)
        account = ibm_db.fetch_assoc(stmt)

        if account:
            return render_template('signup.html', msg="You are already a member, please login using your details")
        else:
            insert_sql = "INSERT INTO COUSTMER_DETAILS VALUES (?,?,?,?,?)"
            prep_stmt = ibm_db.prepare(conn, insert_sql)
            ibm_db.bind_param(prep_stmt, 1, name)
            ibm_db.bind_param(prep_stmt, 2, username)
            ibm_db.bind_param(prep_stmt, 3, email)
            ibm_db.bind_param(prep_stmt, 4, password)
            ibm_db.bind_param(prep_stmt, 5,  repass)
            ibm_db.execute(prep_stmt)

        return render_template('home.html', msg="Retailer Login successfuly..")
    
@app.route('/',methods=["GET","POST"])
def jobseeker_register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['age']
        password = request.form['password']
        address = request.form['address']
        skills = request.form['skills']
        expectedjob = request.form['expectedjob']

        #if password!=cp:
            #return render_template('register.html')

        try:
            sql = "INSERT into User values ('{}', '{}','{}', '{}','{}','{}','{}')".format( name, email, password,address,skills,expectedjob)
            stmt = ibm_db.exec_immediate(conn,sql)
            print("No of Affected rows: ",ibm_db.num_rows(stmt))
        except:
            print("Error: ",ibm_db.stmt_errormsg())
    return render_template("index.html")

if __name__=='main':
    app.run(debug=True)'''