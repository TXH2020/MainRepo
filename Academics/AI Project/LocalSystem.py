from oauth2client import client, file, tools
SCOPES = "https://www.googleapis.com/auth/assistant-sdk-prototype"
DISCOVERY_DOC = "https://forms.googleapis.com/$discovery/rest?version=v1"

store = file.Storage('token.json')
creds = None
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets(r'C:\Users\1001t\Desktop\cs.json', SCOPES)
    creds = tools.run_flow(flow, store)