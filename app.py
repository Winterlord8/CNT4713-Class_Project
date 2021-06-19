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

blueprint = make_google_blueprint(client_id='56700923608-f692rhb11m2qrp8csahn298g2ri3qq5q.apps.googleusercontent.com', client_secret='yesM8mmWGcCMlnFkOzYD8G7g', scope=['profile', 'email'])

socketio.register_blueprint(blueprint, url_prefix='/login')

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
    socketio.run(app, host="0.0.0.0", port="8080")
