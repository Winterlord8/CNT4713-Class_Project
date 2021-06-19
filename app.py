# import os
# os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'
# os.environ['OAUTHLIB_RELAX_TOKEN_SCOPE'] = '1'

# implement other auth method

import cv2
from flask import Flask, redirect, url_for, render_template, Response
from flask_socketio import SocketIO
from flask_dance.contrib.google import make_google_blueprint, google

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mysecret'
socketio = SocketIO(app)
camera = cv2.VideoCapture(0)

blueprint = make_google_blueprint(client_id='56700923608-25b89qud8ep7svm3qmk5t02sa53nuh4c.apps.googleusercontent.com', client_secret='sxZ9mO1zD4wS80PPKzgNEkD-', scope=['profile', 'email'])

app.register_blueprint(blueprint, url_prefix='/login')

# login_manager = LoginManager()
#
# login_manager.login_view = "login"
#
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#
#     form = LoginForm()
#     if form.validate_on_submit():
#         return redirect('main_page.html')
#     else:
#         render_template('login')

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


def gen_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


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
    socketio.run(app, debug=True)
