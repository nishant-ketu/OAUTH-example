from flask import Flask, redirect, url_for
#from flask_dance.contrib.twitter import make_twitter_blueprint, twitter 
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'


github_blueprint = make_github_blueprint(client_id='CLIENT_ID', client_secret='CLIENT_SECRET')



app.register_blueprint(github_blueprint, url_prefix='/github_login')


def github_login():
    if not github.authorized:
        return redirect(url_for('github.login'))

    account_info = github.get('/user')

    if account_info.ok:
        account_info_json = account_info.json()

        return '<h1>Your Github name is {}'.format(account_info_json['login'])

    return '<h1>Request failed!</h1>'

if __name__ == '__main__':
    app.run(debug=True)
