# coding:utf-8
import flask

app = flask.Flask(__name__)#实列化产生一个flask对象


@app.route("/") #是一个函数装饰器，指定了哪个url客户端请求可以调用index函数
def index():
    try:
        openfile = open('index.htm', 'rb')
        data = openfile.read()
        data = data.decode()
    except Exception as err:
        print(err)
    return data #返回给客户端请求的响应数据


if __name__ == "__main__":
    app.run()