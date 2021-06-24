import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'


from flask import Flask, redirect, url_for, render_template, Response
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'

blueprint = make_google_blueprint(client_id='create_your_own', client_secret='create_your_own', scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')


@app.route('/')
def index():
    # return render_template("main_page.html")
    if google.authorized:
        resp = google.get('/oauth2/v2/userinfo')
        assert resp.ok, resp.text
        name = resp.json()['name']

        return render_template('main_page.html', name=name)
    else:
        return render_template('home.html')


@app.route('/static_feed')
def static_feed():

    # return render_template('staticfeed.html')
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    name = resp.json()['name']

    return render_template('staticfeed.html', name=name)


@app.route('/live_feed')
def live_feed():

    # return render_template('live_feed.html')
    resp = google.get('/oauth2/v2/userinfo')
    assert resp.ok, resp.text
    name = resp.json()['name']

    return render_template('live_feed.html', name=name)


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
