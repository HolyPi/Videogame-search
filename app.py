from flask import Flask, render_template, request
import requests
import json

import os

app = Flask(__name__)
# @app.route('/login')
# def login():
#     "Prompts user to log-in"
#
@app.route('/profile')
def profile():
    "Shows user profile"

# @app.route('/favorites')
# def favorites():
#     "Shows favorite list."

@app.route('/')
def index():
    """Return homepage."""
    # TODO: Extract query term from url
    q = request.args.get("search")
    url = 'https://chicken-coop.p.rapidapi.com/games'

    querystring = {"title": q}

    headers = {
        'x-rapidapi-host': "chicken-coop.p.rapidapi.com",
        'x-rapidapi-key': "56727ba773msh7928ed78d71e9dap14f58ajsn8ac0d86569f3"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)

    return render_template("index.html", headers=headers, params=querystring)



if __name__ == '__main__':
    app.run(debug=True)
