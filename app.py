from flask import Flask, redirect, url_for
#from flask_dance.contrib.twitter import make_twitter_blueprint, twitter 
from flask_dance.contrib.github import make_github_blueprint, github

app = Flask(__name__)
app.config['SECRET_KEY'] = 'thisissupposedtobeasecret'
#twitter_blueprint = make_twitter_blueprint(api_key='API_KEY', api_secret='API_SECRET')

github_blueprint = make_github_blueprint(client_id='cc39486b294af8437655', client_secret='6bcf1f60975d61a0b596e33a2c012016c630ce3b')

#app.register_blueprint(twitter_blueprint, url_prefix='/twitter_login')

app.register_blueprint(github_blueprint, url_prefix='/github_login')

'''@app.route('/twitter')
def twitter_login():
    if not twitter.authorized:
        return redirect(url_for('twitter.login'))
    account_info = twitter.get('account/settings.json')

    if account_info.ok:
        account_info_json = account_info.json()

        return '<h1>Your Twitter name is @{}'.format(account_info_json['screen_name'])

    return '<h1>Request failed!</h1>'
    '''

@app.route('/github')
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