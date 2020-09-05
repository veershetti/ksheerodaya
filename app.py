from flask import Flask,render_template,request
app = Flask(__name__)
@app.route('/home',methods = ['POST', 'GET'])
def home():
   if request.method == 'POST':
      user = request.form['username']
      password = request.form['password']
      return render_template('home.html')
@app.route("/")
def login():
  print("i am inside the home")
  return render_template('login.html')
@app.route('/ho',methods = ['POST', 'GET'])
def ho():
   if request.method == 'POST':
      user = request.form['username']
      mobileno = request.form['mno']
      liters = request.form['liters']
      return 'Hello Flask'
@app.route('/flask')
def hello_flask():
   return 'Hello Flask'

@app.route('/python/')
def hello_python():
   return 'Hello Python'

if __name__== "__main__":
  app.run(host="0.0.0.0", port=int("5000"), debug=True)
