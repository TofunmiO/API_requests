import requests
import spotipy

CLIENT_ID = '88b434d8d4554bd3a609fe8b844dab97'
CLIENT_SECRET = '13576ce408514f11ab629fb9f7db7ce7'

AUTH_URL = 'https://accounts.spotify.com/api/token' #endpoint for auth; we just created info about login n gave server to authenticate
auth_response = requests.post(AUTH_URL,{
  'grant_type': 'client_credentials',
  'client_id' : CLIENT_ID,
  'client_secret': CLIENT_SECRET,
})

print(auth_response.status_code)
auth_response_data = auth_response.json()

auth_response_data

access_token = auth_response_data['access_token']

headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
BASE_URL = 'https://api.spotify.com/v1/' #endpoint to get track info; when your program communicates w the api
track_id = '6mFkJmJqdDVQ1REhVfGgd1'

r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

r = r.json()
print(r)