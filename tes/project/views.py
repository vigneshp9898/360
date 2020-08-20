from os import abort

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
"""
from apiclient import discovery
import httplib2
from oauth2client import client
from google_auth_oauthlib.flow import Flow
# (Receive auth_code by HTTPS POST)


# If this request does not have `X-Requested-With` header, this could be a CSRF
from pip._vendor.urllib3.util import request

if not request.headers.get('X-Requested-With'):
    abort(403)

# Set path to the Web application client_secret_*.json file you downloaded from the
# Google API Console: https://console.developers.google.com/apis/credentials
CLIENT_SECRET_FILE = '/path/to/client_secret.json'

# Exchange auth code for access token, refresh token, and ID token
credentials = client.credentials_from_clientsecrets_and_code(
    CLIENT_SECRET_FILE,
    ['https://www.googleapis.com/auth/drive.appdata', 'profile', 'email'],
    auth_code)

# Call Google API
http_auth = credentials.authorize(httplib2.Http())
drive_service = discovery.build('drive', 'v3', http=http_auth)
appfolder = drive_service.files().get(fileId='appfolder').execute()

# Get profile info from ID token
userid = credentials.id_token['sub']
email = credentials.id_token['email']

"""
def index(request):
    return render(request,'index.html')
