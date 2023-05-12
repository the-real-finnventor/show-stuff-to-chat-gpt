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

from flask import Flask

app = Flask(__name__)

@app.route('/run_it', methods=['GET'])
def run_it() -> str:
    name = request.args.get('name')
    whatfor = request.args.get('whatfor')
    characters = request.args.get('characters')

    password = create_password(charecters_long=characters)

    store_password(name=name, whatfor=whatfor, password=password)

    response = make_response(password)
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response

if __name__ == "__main__":
    app.run(port=8000)
    # name = input("What is your name?: ")
    # whatfor = input('What is this password for?: ')
    # charecters = input("How long whould you like your password to be?: ")
    # password = create_password(charecters_long=charecters)
    # print(f"Ok {name.title()}. Your password for {whatfor} is {password}")
    # store_password(name=name, whatfor=whatfor, password=password)