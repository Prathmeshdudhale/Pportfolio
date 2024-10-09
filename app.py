from flask import Flask, render_template, request, redirect, url_for
from flask_pymongo import PyMongo

app = Flask(__name__)

# Configure MongoDB
app.config["MONGO_URI"] = "mongodb+srv://prathmesh:prathmesh@portfolio.8mrws.mongodb.net/db" 
mongo = PyMongo(app)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        mobile = request.form['mobile']
        message = request.form['message']
        
        # Save data to MongoDB
        mongo.db.contacts.insert_one({
            'name': name,
            'email': email,
            'mobile': mobile,
            'message': message
        })
        return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
