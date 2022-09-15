from flask import Flask, jsonify, request

app = Flask(__name__)

'''
@app.route('/')  #https:127.0.0.1/5000 or https:localhost/5000
def home():
    return "hello IBM"

@app.route('/blog')  #https:127.0.0.1/blog or https:localhost/images
def blog():
    return " IBM blogs"
'''
books_db = [
    {
        "name":"Secret",
        "price":200
        
    },
    {
        "name":"Deep work",
        "price":347
    }
]
#retrieve all book http://127.0.0.1:5000/books
@app.route('/books') # this app or browser will take GET request by default, retrieve data
def get_all_book():
    return jsonify({"books":books_db})

#retrieve one book http://127.0.0.1:5000/book/<enter_name_of_book> this app or browser will take GET request by default, retrieve data
@app.route("/book/<string:name>")
def get_book(name):
    for book in books_db:
        if book['name']== name:
            return jsonify(book)
    return jsonify({"message":"book not found"})

# create a book by using  POST 
# Add book name by using any API testing tool i have used POSTMAN, 
@app.route("/book",methods=['POST']) #store some persistent data
def create_book():
    body_data = request.get_json()
    books_db.append(body_data)

    return jsonify({"message":"book has been added "})

app.run(port=5000)


