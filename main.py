from pickle import TRUE
from flask import Flask, render_template, request
import sqlite3 as sql

# conn = sql.connect('databases/mydb.sqlite')
# print("Opened database successfully")

# conn.execute('CREATE TABLE Srecords (name TEXT)')
# print("Table created successfully")
#conn.close()

app = Flask(__name__)
 
@app.route('/')
def hello_name():
   # Ahmed = "Hello how are u"
   return render_template('index.html')
 
@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
   con=sql.connect("databases/mydb.sqlite") 
   msg=''
   if request.method == 'POST':
      
      try:
         nm = request.form['fname']
         print(nm)
      
         
         cur = con.cursor()
         cur.execute("INSERT INTO students values('"+nm+"');")
            
         con.commit()
         msg = "Record successfully added"
      except Exception as e:
         con.rollback()
         msg = "error in insert operation"
         print(e)
      finally:
         return render_template("result.html",msg = msg)
   con.close() 

@app.route('/list')
def list():
   con = sql.connect("databases/mydb.sqlite")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from students")
   
   rows = cur.fetchall(); 
   return render_template("list.html",rows = rows)


if __name__ == '__main__':
   app.run(host='0.0.0.0',port='8800',debug=True)