from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/index')
def index():  # put application's code here
    return render_template('index.html')

@app.route('/baijian.html')
def baijian():  # put application's code here
    return render_template('baijian.html')

@app.route('/baici.html')
def baici():  # put application's code here
    return render_template('baici.html')

@app.route('/baiqing.html')
def baiqing():  # put application's code here
    return render_template('baiqing.html')

@app.route('/baishe.html')
def baishe():  # put application's code here
    return render_template('baishe.html')

@app.route('/qiangjian.html')
def qiangjian():  # put application's code here
    return render_template('qiangjian.html')

@app.route('/qiangci.html')
def qiangci():  # put application's code here
    return render_template('qiangci.html')

@app.route('/qiangqing.html')
def qiangqing():  # put application's code here
    return render_template('qiangqing.html')

@app.route('/qiangshe.html')
def qiangshe():  # put application's code here
    return render_template('qiangshe.html')

@app.route('/tajianjie.html')
def tajianjie():  # put application's code here
    return render_template('tajianjie.html')



@app.route('/taci.html')
def tajian():  # put application's code here
    return render_template('taci.html')

@app.route('/taqing.html')
def taqing():  # put application's code here
    return render_template('taqing.html')

@app.route('/tashe.html')
def tashe():  # put application's code here
    return render_template('tashe.html')

if __name__ == '__main__':
    app.run()

