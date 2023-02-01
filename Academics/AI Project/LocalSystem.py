from oauth2client import client, file, tools
import json
import os
import click
SCOPES = "https://www.googleapis.com/auth/assistant-sdk-prototype"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(r'path to downloaded credentials', SCOPES)
    creds = tools.run_flow(flow, store)

APP_NAME = 'google-oauthlib-tool'
DEFAULT_CREDENTIALS_FILENAME = 'credentials.json'

x=None
with open('token.json','r') as f:
    x=json.load(f)
y={}
y['client_id']=x['client_id']
y['client_secret'] = x['client_secret']
y['refresh_token'] = x['refresh_token']
y['token_uri'] = x['token_uri']
y['id_token'] = x['id_token']
y['scopes'] = x['scopes']

fname=os.path.join(
        click.get_app_dir(APP_NAME),
        DEFAULT_CREDENTIALS_FILENAME)
with open(fname,'w') as f:
    json.dump(y,f)
