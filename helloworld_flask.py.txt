from flask import Flask

# Creating a flask application instance
app = Flask(__name__)

# decorator, perform a action before execution of a function
@app.route("/")
def hello():
    return "Hello World"

app.run('0.0.0.0')