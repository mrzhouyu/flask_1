from flask import Flask,render_template,request,session
from config import ManyConfig

import os
from flask_script import Manager

app = Flask(__name__,static_url_path='/static/Image')

app.config.from_object(ManyConfig)

app.config.update(
    DEBUG=True,
    SECRET_KEY=os.urandom(24)
)

@app.route('/form',methods=['GET','POST'])
def session_text():
    #
    if request.method=='GET':
        return render_template('index2.html',id=session.get('id'))
    session['id']=request.form.get('id')
    return render_template('index2.html',id=session.get('id'))

@app.route('/')
def hello_world():
    return 'hello YuCHOU'
@app.route('/next')
def index():
    return render_template('index.html',name="nothing",test="i am test",test2="other test",image_bytes=return_image())

@app.route('/three')
def from_request():
    host=request.host
    header=request.headers
    print(header.get('host'))
    print(request.environ)
    return render_template("index.html",header=header)


def return_image():
    import base64
    image_bytes=''
    with open(r'E:\PythonPrJ\flask_1\static\Image\face++.jpg','r') as f:
        image_bytes=f.read()
        image_bytes=base64.b64encode(image_bytes)
    return image_bytes


if __name__ == '__main__':
    app.debug=True
    app.run(host='127.0.0.1',port=8888)
#运行命令 : python app.py (terminal 环境下)