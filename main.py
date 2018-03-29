from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>
<html>
    <head>
        <style>
            form{
                background-color: #eee;
                padding: 20 px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }
        </style>
    </head>
    <body>
        <form action="/rotate" method="post">
            <label>
                Rotate by
                <input type="text" name="rot" value="0"/>                
            </label>
            <input type="textarea" name="text"/>
            <input type="submit" value="Submit Query"/>

        </form>
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/rotate", methods=['POST'])
def encrypt():
    rotval = int(request.form['rot'])
    message = request.form['text']
    encrypted_message = rotate_string(message, rotval)
    return "<h1>" + encrypted_message + "</h1>"



app.run()
