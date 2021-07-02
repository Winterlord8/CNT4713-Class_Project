import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

from flask import Flask, redirect, url_for, render_template, Response
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

# setting up the google blueprint & registring it
blueprint = make_google_blueprint(
                            client_id='CLIENT_ID',
                            client_secret='CLIENT_SECRET',
                            reprompt_consent=True,
                            # offline=True,
                            scope=['profile', 'email']
                            )
app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    if google.authorized:
        resp = google.get('/oauth2/v2/userinfo')
        assert resp.ok, resp.text
        name = resp.json()['name']
        return render_template('main_page.html', name=name)
    else:
        return render_template('home.html')


@app.route('/static_feed')
def static_feed():
    if google.authorized:
        resp = google.get('/oauth2/v2/userinfo')
        assert resp.ok, resp.text
        name = resp.json()['name']
        return render_template('staticfeed.html', name=name)
    else:
        return redirect(url_for('index'))


@app.route('/live_feed')
def live_feed():
    if google.authorized:
        resp = google.get('/oauth2/v2/userinfo')
        assert resp.ok, resp.text
        name = resp.json()['name']
        return render_template('live_feed.html', name=name)
    else:
        return redirect(url_for('index'))

@app.route('/login/google')
def login():
    if not google.authorized:
        return render_template(url_for('google.login'))
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    name = resp.json()['name']

    return redirect('main_page.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
