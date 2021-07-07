import requests
import spotipy
import os
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine


def get_input():
    CLIENT_ID = input("Enter Client ID: ")
    CLIENT_SECRET = input("Enter Client Secret: ")
    return CLIENT_ID, CLIENT_SECRET


# this is needed to get access token
def get_auth_response(CLIENT_ID, CLIENT_SECRET):
    AUTH_URL = 'https://accounts.spotify.com/api/token'  # endpoint for auth;
# we just created info about login n gave server to authenticate
    auth_response = requests.post(AUTH_URL, {
      'grant_type': 'client_credentials',
      'client_id': CLIENT_ID,
      'client_secret': CLIENT_SECRET,
    })

    print(auth_response.status_code)
    return auth_response


#   this is needed for headers
def get_access_token(auth_response):
    auth_response_data = auth_response.json()
    access_token = auth_response_data['access_token']
    return access_token


# generate url
def get_url(access_token):
    headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
    url = 'https://api.spotify.com/v1/' +
    'audio-features/' + '6mFkJmJqdDVQ1REhVfGgd1', headers = headers
    return url


# test if response was good
def get_json(url):
    r = requests.get(url)
    return r.json()


# creating data frame to add data to
def get_df():
    col_names = ['energy', 'liveness', 'type']
    df = pd.DataFrame(columns=col_names)
    df.loc[len(df.index)] = [1, 2, 3]
    return df


def write_table(df, dbName):
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    engine = create_engine('mysql://root:codio@localhost/{}'.format(dbName))
    df.to_sql('table_name', con=engine, if_exists='replace', index=False)

def save_file(df,dbName, fileName):
    engine = create_engine('mysql://root:codio@localhost/{}'.format(dbName))
    df.to_sql('table_name', con=engine, if_exists='replace', index=False)
    os.system("mysqldump -u root -pcodio {} > {}.sql".format(dbName,fileName))

def load():
    os.system('mysql -u root -pcodio -e "CREATE DATABASE IF NOT EXISTS '
              + dbName + '; "')
    os.system("mysql -u root -pcodio {} < {}.sql".format(dbName,fileName))

def main():

    database = 'api'
    filename = 'dump'

    write_table(df, database)

    save_file(df, database, filename)


if __name__ == "__main__":
    main()

# import requests
# import spotipy
# import pandas as pd
# import sqlalchemy
# from sqlalchemy import create_engine


# creating data frame to add data to
# col_names = ['energy', 'liveness', 'type']
# df = pd.DataFrame(columns = col_names)
# engine = create_engine('mysql://root:codio@localhost/api')
# df.to_sql('table_name', con=engine, if_exists='replace', index=False)
# df.loc[len(df.index)] = [1, 2, 3]

# CLIENT_ID = '88b434d8d4554bd3a609fe8b844dab97'
# CLIENT_SECRET = '13576ce408514f11ab629fb9f7db7ce7'

# AUTH_URL = 'https://accounts.spotify.com/api/token'
#  endpoint for auth; we just created info about login
#  n gave server to authenticate
# auth_response = requests.post(AUTH_URL,{
#   'grant_type': 'client_credentials',
#   'client_id' : CLIENT_ID,
#   'client_secret': CLIENT_SECRET,
# })

# print(auth_response.status_code)
# auth_response_data = auth_response.json()

# auth_response_data

# access_token = auth_response_data['access_token']

# headers = {'Authorization': 'Bearer {token}'.format(token=access_token)}
# BASE_URL = 'https://api.spotify.com/v1/'
# endpoint to get track info; when your program communicates w the api
# track_id = '6mFkJmJqdDVQ1REhVfGgd1' --resource not query

# r = requests.get(BASE_URL + 'audio-features/' + track_id, headers=headers)

# r = r.json()
# print(r)
