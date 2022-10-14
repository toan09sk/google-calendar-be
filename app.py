from os import stat
from flask import Flask,redirect,request, url_for, session
from google_calendar import *

app = Flask(__name__)

@app.route('/')
def index():
#   if 'credentials' not in session:
#     return redirect(url_for('oauth_callback'))

#   credentials = json.loads(session['credentials'])
#   if credentials['expires_in'] <= 0:
#     return redirect(url_for('oauth_callback'))
#   else:
#     headers = {'Authorization': 'Bearer {}'.format(credentials['access_token'])}
#     req_uri = 'https://www.googleapis.com/drive/v2/files'
#     r = requests.get(req_uri, headers=headers)
#     return r.text
    return "Hello!"

@app.route('/oauth/redirect', methods = ["GET"])
def oauth_redirect():
    url_redirect = oauth2_callback()
    return redirect(url_redirect)

@app.route('/oauth/callback', methods = ["GET"])
def oauth_callback():
    code = request.args.get('code')
    state = request.args.get('state')
    scope = request.args.get('scope')
    error = request.args.get('error')
    # print(code, error, state, scope)
    if 'code' not in request.args:
        auth_uri = auth_uri()
        return redirect(auth_uri)

    else:
        get_token(code)

    return redirect(url_for('index'))

@app.route('/oauth/refresh-token', methods = ["GET"])
def oauth_refresh_token():
    refresh_token()
    return redirect(url_for('index'))

@app.route('/oauth/revoke-token', methods = ["GET"])
def oauth_revoke_token():
    revoke_token()
    return redirect(url_for('index'))

@app.route('/calendar/create-event', methods = ["GET"])
def calendar_create_event():
    result = create_event()
    return result

@app.route('/calendar/get-all-event', methods = ["GET"])
def calendar_get_all_event():
    result = get_all_event()
    return result
    

if __name__ == "__main__":
    import uuid
    app.secret_key = str(uuid.uuid4())
    app.run(debug=True, port=5000)
