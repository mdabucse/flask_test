from flask import Flask , jsonify , request

app = Flask(__name__)

# Initialize the Values for GET method
items = [
    {'id':1,'name':'Abu','des':"Nalla Paiyan"},
    {'id':2,'name':'Thahi','des':"Nalla Ponnu"}
]

@app.route('/')
def home():
    return "<h1>Welcome to TODOLIST</h1>"

@app.route('/items',methods=['GET'])
def items():
    return jsonify({'items':'Abu'})

# POST Request
@app.route('/items',methods=['POST'])
def create_item():
    if not request.json or not 'name' in request.json:
        return jsonify({"Error":"Error da dai"})
    new_item={
        'id':items[-1]['id'] + 1 if items else 1,
        'name':request.json['name'],
        'des':request.json['des']
    }
    items.append(new_item)


if __name__=='__main__':
    app.run(debug=True)
