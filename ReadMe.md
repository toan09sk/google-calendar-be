```
python -m venv venv
pip freeze -l > requirements.txt
pip install -r requirements.txt
.\venv\Scripts\activate
```

```
pip install flask flask-sqlalchemy
export FLASK_APP=app.py
```

```
https://developers.google.com/oauthplayground
https://developers.google.com/identity/protocols/oauth2/web-server
https://myaccount.google.com/security
```

```
{
  "access_token": "ya29.a0Aa4xrXNFdn_Myw94TppJr5Z4lForOHgH1x_2eY4ZiiLRCH8uNvSeivw-XHwG9oVa5NM4XTqAsWyK-iiOa5W1yoCpUXfoU7L7DGpLuJg8IYXfZWfNTRYQgae3_EbLfozcMfZlwKp9MG3gj_ZmOVqXFdoeWiiFaCgYKATASARMSFQEjDvL9AIabQi-wlGRbBtpFcZYMLQ0163",
  "expires_in": 3599,
  "scope": "https://www.googleapis.com/auth/calendar https://www.googleapis.com/auth/calendar.events",
  "token_type": "Bearer"
}
```
```
http://localhost:5000/oauth/redirect
http://localhost:5000/calendar/create-event
 
```