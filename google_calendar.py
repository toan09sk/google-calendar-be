from lib2to3.pgen2 import token
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import requests
import json
from flask import session

SCOPES = ['https://www.googleapis.com/auth/calendar']
SCOPE = ['https://www.googleapis.com/auth/calendar']

CLIENT_SECRET = "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"

CLIENT_ID = "260457260524-8ka16c9gbrbu872mg2nh6upf1ngjpj1u.apps.googleusercontent.com"

REDIRECT_URI = "http://localhost:5000/oauth/callback"

API_KEY = "AIzaSyAj6xEAZE1XunaPHYAgzRe48pHRdFgvYlo"


def oauth2_callback():
    redirect_url = "https://accounts.google.com/o/oauth2/auth?" +\
        "scope=https://www.googleapis.com/auth/calendar+https://www.googleapis.com/auth/calendar.events&" +\
        "access_type=offline&" +\
        "include_granted_scopes=true&" +\
        "response_type=code&" +\
        "state=there&" +\
        "redirect_uri=http://localhost:5000/oauth/callback&" +\
        "client_id=260457260524-8ka16c9gbrbu872mg2nh6upf1ngjpj1u.apps.googleusercontent.com"
    return redirect_url


def get_token(auth_code):
    data = {
        'code': auth_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI,
        'grant_type': 'authorization_code'
    }

    response = requests.post('https://oauth2.googleapis.com/token', data=data)

    if response.status_code == 200:
        session['credentials'] = response.text
        with open('token.json', 'w') as f:
            json.dump(response.json(), f)


def auth_uri():
    auth_uri = ('https://accounts.google.com/o/oauth2/v2/auth?response_type=code'
                '&client_id={}&redirect_uri={}&scope={}').format(CLIENT_ID, REDIRECT_URI, SCOPE)
    return auth_uri


def refresh_token():
    credentials = json.loads(session['credentials'])

    with open('token.json', 'w') as f:
        tokens = json.load(f)

    data = {
        'client_id': credentials['client_id'],
        'client_secret': credentials['client_secret'],
        'grant_type': 'refresh_token',
        'refresh_token': tokens['refresh_token']
    }

    response = requests.post('https://oauth2.googleapis.com/token', data=data)

    if response.status_code == 200:
        with open('token.json', 'w') as f:
            json.dump(response.json(), f)


def revoke_token():
    with open('token.json') as f:
        tokens = json.load(f)

    data = {
        'token': tokens['access_token']
    }

    requests.post('https://oauth2.googleapis.com/revoke', data=data)


def create_event():
    # with open('token.json') as f:
    #     tokens = json.load(f)
    tokens = json.loads(session['credentials'])

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": "Bearer " + tokens["access_token"]
    }

    params = {
        'key': API_KEY
    }

    event = {
        'summary': 'Google I/O 2015',
        'location': '800 Howard St., San Francisco, CA 94103',
        'description': 'A chance to hear more about Google\'s developer products.',
        'start': {
            'dateTime': '2015-05-28T09:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': '2015-05-28T17:00:00-07:00',
            'timeZone': 'America/Los_Angeles',
        },
        'recurrence': [
            'RRULE:FREQ=DAILY;COUNT=2'
        ],
        'attendees': [
            {'email': 'lpage@example.com'},
            {'email': 'sbrin@example.com'},
        ],
        'reminders': {
            'useDefault': False,
            'overrides': [
                {'method': 'email', 'minutes': 24 * 60},
                {'method': 'popup', 'minutes': 10},
            ],
        },
    }

    calendar_id = 'primary'

    response = requests.post(
        'https://www.googleapis.com/calendar/v3/calendars/{}/events'.format(calendar_id), headers=headers, params=params, json=event)

    if response.status_code == 200:
        return response.json()

    return 'failed!'


def get_all_event():
    tokens = json.loads(session['credentials'])

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": "Bearer " + tokens["access_token"]
    }

    params = {
        'key': API_KEY
    }

    calendar_id = 'primary'

    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/{}/events'.format(calendar_id), headers=headers, params=params)

    if response.status_code == 200:
        return response.json()

    return 'failed!'

def get_event_by_id():
    credentials = json.loads(session['credentials'])

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": "Bearer " + credentials["access_token"]
    }

    params = {
        'key': API_KEY
    }

    calendar_id = 'primary'
    event_id = 'ea616kbfqv80jdrre3mm5r41ek'

    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/{}/events/{}'.format(calendar_id, event_id), headers=headers, params=params)

    if response.status_code == 200:
        return response.json()

    return 'failed!'


def get_instances():
    tokens = json.loads(session['credentials'])

    headers = {
        "Content-Type": "application/json; charset=utf-8",
        "Accept": "application/json",
        "Authorization": "Bearer " + tokens["access_token"]
    }

    params = {
        'key': API_KEY
    }

    calendar_id = 'primary'
    event_id = 'ea616kbfqv80jdrre3mm5r41ek'

    response = requests.get(
        'https://www.googleapis.com/calendar/v3/calendars/{}/events/{}/instances'.format(calendar_id, event_id), headers=headers, params=params)

    if response.status_code == 200:
        return response.json()

    return 'failed!'

