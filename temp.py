from flask import Flask,request

app=Flask(__name__)

student={
    '1':{'id':1,'name':'nayeem','mark':100},
    '2':{'id':2,'name':'shyam','mark':10},
    '3':{'id':3,'name':'deepek','mark':20},
    '4':{'id':4,'name':'tharun','mark':15}
    }

@app.route('/ping')
def pingpong():
    return "<h1>pong</h1>"

@app.route("/")
def hello_world():
    return "Hello, World!"

@app.route('/get/students')
def disp():
    return student

@app.route('/get/students/<id>')
def index(id):
    #id = request.view_args['id']
    return student[id]

@app.route('/post/students')
def post():
    

if __name__=='__main__':
    app.run()
