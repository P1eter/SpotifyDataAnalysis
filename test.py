"""
Before use do the following:

export SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
export SPOTIPY_CLIENT_SECRET='c02f97ddd119470d8e24b290722c7490'
export SPOTIPY_CLIENT_ID='647ffb8c163b4882be0cafe4bf1352d5'
"""
import sys
import spotipy
import spotipy.util as util


SPOTIPY_REDIRECT_URI='http://localhost:8888/callback'
SPOTIPY_CLIENT_SECRET='c02f97ddd119470d8e24b290722c7490'
SPOTIPY_CLIENT_ID='647ffb8c163b4882be0cafe4bf1352d5'
USERNAME='lh7smhcywr18vctg4xmnoehzu'
SCOPE='user-library-read'

def show_tracks(tracks):
    for i, item in enumerate(tracks['items']):
        track = item['track']
        print("   %d %32.32s %s" % (i, track['artists'][0]['name'],
            track['name']))


if __name__ == '__main__':
    # if len(sys.argv) > 1:
    #     username = sys.argv[1]
    # else:
    #     print("Whoops, need your username!")
    #     print("usage: python test.py [username]")
    #     sys.exit()
    username = USERNAME

    # token = util.prompt_for_user_token(username)
    token = util.prompt_for_user_token(username=USERNAME,
                               scope=SCOPE,
                               client_id=SPOTIPY_CLIENT_ID,
                               client_secret=SPOTIPY_CLIENT_SECRET,
                               redirect_uri=SPOTIPY_REDIRECT_URI)

    if token:
        sp = spotipy.Spotify(auth=token)
        playlists = sp.user_playlists(username)
        for playlist in playlists['items']:
            if playlist['owner']['id'] == username:
                print()
                print(playlist['name'])
                print('  total tracks', playlist['tracks']['total'])
                results = sp.user_playlist(username, playlist['id'],
                    fields="tracks,next")
                tracks = results['tracks']
                show_tracks(tracks)
                while tracks['next']:
                    tracks = sp.next(tracks)
                    show_tracks(tracks)
    else:
        print("Can't get token for", username)