# coding:utf-8
import os

from flask import Flask, render_template, request, redirect, url_for, make_response
from werkzeug.utils import secure_filename

app = Flask(__name__)


@app.route('/')  # 代表首页
def index():  # 视图函数
    return render_template('register.html')

@app.route('/center/add')  # 代表个人中心页
def center():  # 视图函数
    if request.method == 'GET':  # 请求方式是get
        name = request.args.get('name')  # args取get方式参数
        age = request.args.get('age')
        hobby = request.args.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)



@app.route('/register', methods=['GET', 'POST'])  # 支持get、post请求
def register():  # 视图函数
    if request.method == 'POST':
        print(request.form)
        name = request.form.get('name')  # form取post方式参数
        age = request.form.get('age')
        hobby = request.form.getlist('hobby')  # getlist取一键多值类型的参数
        return "姓名：%s 年龄：%s 爱好：%s" % (name, age, hobby)
    return render_template('register.html')  # 返回模板


@app.route('/upload', methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, 'static/uploads',
                                   secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('upload'))
    return render_template('upload.html')


@app.route("/set_cookies")
def set_cookie():
    resp = make_response("success")
    resp.set_cookie("w3cshool", "w3cshool123", max_age=3600)
    return resp


@app.route("/get_cookies")
def get_cookie():
    cookie_1 = request.cookies.get("w3cshool")  # 获取名字为Itcast_1对应cookie的值
    return cookie_1


@app.route("/delete_cookies")
def delete_cookie():
    resp = make_response("del success")
    resp.delete_cookie("w3cshool")

    return resp


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)