from __future__ import print_function

import datetime
import os.path
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('calendar', 'v3', credentials=creds)

        # Call the Calendar API
        now = datetime.datetime.today()
        weekend = now+datetime.timedelta(days=5)
        now = now.isoformat() + 'Z'  # 'Z' indicates UTC time
        weekend = weekend.isoformat() + 'Z'  # 'Z' indicates UTC time
        events_result = service.events().list(calendarId='primary', timeMin=now,timeMax=weekend,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            return []

        # Prints the start and name of the next 10 events
        all_cours = []
        all_cours_start = []
        for event in events:
            start = event['start'].get('dateTime')
            end = event['end'].get('dateTime')
            duree = [(datetime.datetime.strptime(start, "%Y-%m-%dT%H:%M:%S+01:00")),(datetime.datetime.strptime(end, "%Y-%m-%dT%H:%M:%S+01:00"))]
            all_cours.append(duree)

    except HttpError as error:
        print('An error occurred: %s' % error)

    salle_libre=[[8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                [8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                [8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                [8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                [8,9,10,11,12,13,14,15,16,17,18,19,20,21],
                [],
                [10,11,12,13,14,15,16,17,18]]

    week=[[],[],[],[],[],[],[]]

    for cours in all_cours:
        intervalle = [cours[0].hour,cours[1].hour]
        week[cours[0].weekday()].append(intervalle)

    for i in range(len(week)):
        for hour in week[i]:
            heure = hour[0]
            while heure<=hour[1]:
                if heure in salle_libre[i]:
                    salle_libre[i].remove(heure)
                heure+=1

    return salle_libre
