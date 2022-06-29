from flask import Flask, jsonify, request, render_template
from app import app
from app import LoginForm



app = Flask(__name__)
app.static_folder = 'static'

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)

@app.route('/', methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        some_json = request.get_json()
        return jsonify({"you sent": some_json}), 201
    else:
        return jsonify({"about": "Hello!"})

@app.route('/home', methods=['GET'])
def home():
    user = {'username': 'Shawaz'}
    return render_template('index.html', title='Home', user=user)
    
@app.route('/multi/<int:num>', methods=['GET'])
# Write an exception handler inside /multi/<num:int> route to handle invalid data type input
def get_mult10(num):
    try:
        return jsonify({'result': num*10})
    except ValueError(400):
        return 'Type error, you must enter an integer.'
    
@app.route('/asfd', methods=['GET'])
def test():
    return jsonify(1, 2, 3)

@app.errorhandler(404)
def page_not_found(e):
# note that we set the 404 status explicitly
# return render_template('404.html'), 404
    return "No route exists."

if __name__ == "__main__":
    app.run(debug=True)
    