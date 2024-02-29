from flask import Flask, redirect, url_for, request, render_template
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
from flask_bootstrap import Bootstrap
import os
app = Flask(__name__)
Bootstrap(app)
img = os.path.join('static')
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
   return render_template('upload.html',show_hidden=False)


@app.route("/uploader",methods=['GET','POST'])
def uploader():
      if request.method == 'POST':
         file = request.files['file']
         filename = secure_filename(file.filename)

         file.save('static/'+filename)
         filepath = os.path.join(img, filename)
         return render_template('upload.html', show_hidden=True,f=filepath)


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
