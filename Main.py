import sqlite3
from flask import *
from datetime import datetime
app = Flask(__name__)



@app.route('/')
def search():
    print(request.remote_addr)
    print(request.user_agent)
    return render_template('search.html')



@app.route('/result',methods = ['GET','POST'])
def result():
    name = request.form.get('name')
    if name in ['200208潘明杰','200301毕丁骁技7']:
        return render_template('114514.html',name=name[6:9])
    conn = sqlite3.connect('data/Oj.db')
    cur = conn.cursor()
    cur.execute('select * from data where username=?',(name,))
    r = cur.fetchall()
    cur.close()
    conn.close()
    print(r)
    if len(r) > 0:
        r=list(r[0])
        r[2]='114.55.172.240:180'+r[2]
        print(r)
        return render_template('r.html',dic = r)
    else:
        return '''<h1 align='center'>418 error : I AM A TEAPOT<h1>'''



@app.route('/chun')
def chun():
    return render_template('孝经·春约.html')


IMG_PATH = "img/"
@app.route('/img/<string:filename>', methods=['GET'])
def display_img(filename):
    request_begin_time = datetime.today()
    print("request_begin_time", request_begin_time)
    if request.method == 'GET':
        #print(filename)
        if filename[::-1][0:4]=='gnp.':
            image_data = open(IMG_PATH + filename, "rb").read()
        else:
            image_data = open(IMG_PATH + filename+'.png', "rb").read()
        response = make_response(image_data)
        response.headers['Content-Type'] = 'image/jpg'
        return response
    else:
        pass



if __name__ == '__main__': 
    app.run(debug=True,host='0.0.0.0', port=80) 
