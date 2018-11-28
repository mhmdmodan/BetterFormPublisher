from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools


class Responses():

    scopes = 'https://www.googleapis.com/auth/spreadsheets.readonly'

    @staticmethod
    def __initialize_api():
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json',
                                                  Responses.scopes)
            creds = tools.run_flow(flow, store)
        service = build('sheets', 'v4', http=creds.authorize(Http()))
        return service.spreadsheets()

    sheets_api = __initialize_api()

    def __init__(self, sheet_id: str) -> None:
        pass

    @staticmethod
    def download_sheet(sheet_id: str):
        
