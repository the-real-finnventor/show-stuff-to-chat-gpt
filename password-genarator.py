import secrets
import string
import sys

def create_password(charecters_long) -> str:
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(alphabet) for i in range(int(charecters_long)))
    return password

def store_password(name, whatfor, password):
    text = f"{name.title()}'s password for {whatfor} = {password}\n"
    with open(f'{sys.path[0]}/passwords.txt', 'a') as file:
        file.write(text)

from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/run_it', methods=['GET'])
def run_it():
    name = request.args.get('name')
    whatfor = request.args.get('whatfor')
    characters = request.args.get('characters')
    password = create_password(int(characters))
    store_password(name,whatfor,password)
    result = {
        "password": password
    }
    return jsonify(result)

if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
