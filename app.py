from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_bootstrap import Bootstrap
app = Flask(__name__)
Bootstrap(app)

from demo import translatetext
@app.route('/success')
def success():
   text=translatetext()

   return 'Hello %s as Guest' % text

# @app.route('/login',methods = ['POST', 'GET'])
# def login():
#    if request.method == 'POST':
#       user = request.form['nm']
#       return redirect(url_for('success',name = user))
#    else:
#       user = request.args.get('nm')
#       return redirect(url_for('success',name = user))


@app.route("/student")
def student():
   return render_template('student.html')


@app.route('/upload')
def upload():
   return render_template('upload.html')


@app.route("/uploader",methods=['GET','POST'])
def uploader():
      if request.method == 'POST':
         f = request.files['file']
         
         return 'file uploaded successfully'


@app.route("/result",methods=['POST','GET'])
def result():
   if request.method=='POST':
      result=request.form
      return render_template('result.html',result=result)
@app.route("/")
def index():
    return render_template('index.html')
if __name__ == '__main__':
   app.run(debug=True)
