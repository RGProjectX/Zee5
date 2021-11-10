from requests import get as g
from fastapi.responses import RedirectResponse as rr
from fastapi import FastAPI

app = FastAPI()

@app.get("/{channel}")
def read_root(channel: str):
	try:
		stream = g(f'https://catalogapi.zee5.com/v1/channel/{channel}').json()['stream_url_hls']
        token = g('https://useraction.zee5.com/token/live.php').json()['video_token']
        rr(f'{stream}{token}')
	except Exception as e:
    	return e
