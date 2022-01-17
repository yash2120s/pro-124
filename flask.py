from re import U
from flask import Flask, jsonify,request

app = Flask(__name__)
tasks = [{
 'id': 1,
 
 'title': u'Buy groceries',
 'description': u'Milk, Cheese, Pizza, Fruit, Tylenol', 
  'done': False
     
},
{

 'id': 2,
 
 'title': u'Learn Python',
 'description': u'Need to find good tutorial on web', 
  'done': False
     
}
] 
@app.route('/')
def hello_world():
    return 'HEllo WoRlD!'
    
if(__name__ == '__main__'):
    app.run(debug = True)
